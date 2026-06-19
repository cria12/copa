#!/usr/bin/env python3
"""
Script de atualização automática da Copa do Mundo 2026.
Busca resultados via Google/fontes públicas usando requests.
Projetado para rodar via GitHub Actions a cada 5 horas.

Fluxo:
1. Lê status.json e data.js para saber quais jogos já foram processados
2. Verifica quais jogos do cronograma (upcoming_matches) já deveriam ter terminado
3. Busca resultados via scraping do Google
4. Cria resumos .md para jogos novos
5. Atualiza status.json
6. Chama update_helper.py rebuild (que faz git push automático)
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
import urllib.request
import urllib.parse
import ssl


# ============================================================
# Mapeamento completo de nomes em inglês → português
# ============================================================
NAME_EN_TO_PT = {
    "Mexico": "México", "South Africa": "África do Sul",
    "South Korea": "Coreia do Sul", "Czech Republic": "Tchéquia",
    "Czechia": "Tchéquia", "Canada": "Canadá",
    "Bosnia and Herzegovina": "Bósnia e Herzegovina", "Bosnia": "Bósnia e Herzegovina",
    "Qatar": "Catar", "Switzerland": "Suíça", "Brazil": "Brasil",
    "Morocco": "Marrocos", "Haiti": "Haiti", "Scotland": "Escócia",
    "United States": "Estados Unidos", "USA": "Estados Unidos",
    "Paraguay": "Paraguai", "Australia": "Austrália",
    "Turkey": "Turquia", "Türkiye": "Turquia", "Turkiye": "Turquia",
    "Germany": "Alemanha", "Curaçao": "Curaçao", "Curacao": "Curaçao",
    "Ivory Coast": "Costa do Marfim", "Côte d'Ivoire": "Costa do Marfim",
    "Ecuador": "Equador", "Netherlands": "Holanda", "Holland": "Holanda",
    "Japan": "Japão", "Sweden": "Suécia", "Tunisia": "Tunísia",
    "Iran": "Irã", "New Zealand": "Nova Zelândia",
    "Spain": "Espanha", "Cape Verde": "Cabo Verde",
    "Belgium": "Bélgica", "Egypt": "Egito",
    "Saudi Arabia": "Arábia Saudita", "Uruguay": "Uruguai",
    "France": "França", "Senegal": "Senegal",
    "Norway": "Noruega", "Iraq": "Iraque",
    "Argentina": "Argentina", "Algeria": "Argélia",
    "Austria": "Áustria", "Jordan": "Jordânia",
    "Portugal": "Portugal", "DR Congo": "RD Congo",
    "Democratic Republic of the Congo": "RD Congo",
    "Uzbekistan": "Uzbequistão", "Colombia": "Colômbia",
    "England": "Inglaterra", "Croatia": "Croácia",
    "Ghana": "Gana", "Panama": "Panamá",
}

# Mapeamento reverso: português → inglês (para buscas no Google)
NAME_PT_TO_EN = {v: k for k, v in NAME_EN_TO_PT.items()}
# Ajustar entradas duplicadas
NAME_PT_TO_EN["Tchéquia"] = "Czech Republic"
NAME_PT_TO_EN["Bósnia e Herzegovina"] = "Bosnia"
NAME_PT_TO_EN["Estados Unidos"] = "USA"
NAME_PT_TO_EN["Turquia"] = "Turkey"
NAME_PT_TO_EN["Costa do Marfim"] = "Ivory Coast"
NAME_PT_TO_EN["Holanda"] = "Netherlands"
NAME_PT_TO_EN["RD Congo"] = "DR Congo"


def parse_js_upcoming_matches(content):
    """Extrai a lista de upcoming_matches do data.js."""
    match = re.search(r"upcoming_matches:\s*\[([\s\S]*?)\]\s*,", content)
    if not match:
        return []
    block = match.group(1)

    pattern = re.compile(
        r'\{\s*id:\s*"([^"]+)"'
        r'[\s\S]*?date:\s*"([^"]+)"'
        r'[\s\S]*?time:\s*"([^"]+)"'
        r'[\s\S]*?group:\s*"([^"]+)"'
        r'[\s\S]*?teamA:\s*\{\s*name:\s*"([^"]+)"(?:,\s*code:\s*"([^"]*)")?\s*\}'
        r'[\s\S]*?teamB:\s*\{\s*name:\s*"([^"]+)"(?:,\s*code:\s*"([^"]*)")?\s*\}'
        r'[\s\S]*?venue:\s*"([^"]+)"'
        r'[\s\S]*?\}'
    )

    parsed = []
    for m in pattern.finditer(block):
        parsed.append({
            "id": m.group(1),
            "date": m.group(2),
            "time": m.group(3),
            "group": m.group(4),
            "teamA": {"name": m.group(5), "code": m.group(6) or ""},
            "teamB": {"name": m.group(7), "code": m.group(8) or ""},
            "venue": m.group(9)
        })
    return parsed


def search_google_result(team_a_en, team_b_en):
    """
    Busca resultado de um jogo da Copa do Mundo 2026 via Google.
    Retorna dict com score_a, score_b ou None se não encontrou.
    """
    query = urllib.parse.quote(f"FIFA World Cup 2026 {team_a_en} vs {team_b_en} score result")
    url = f"https://www.google.com/search?q={query}&hl=en"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        ctx = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')

        # Procurar padrões de placar no HTML do Google
        # Padrão comum: "Team A 2 - 1 Team B" ou "2-1" próximo dos nomes
        score_patterns = [
            # Padrão direto: "X - Y" ou "X-Y"
            re.compile(rf'{re.escape(team_a_en)}[^0-9]*?(\d+)\s*[-–]\s*(\d+)[^0-9]*?{re.escape(team_b_en)}', re.IGNORECASE),
            re.compile(rf'{re.escape(team_b_en)}[^0-9]*?(\d+)\s*[-–]\s*(\d+)[^0-9]*?{re.escape(team_a_en)}', re.IGNORECASE),
            # Padrão genérico em sports card do Google
            re.compile(r'data-df-team[^>]*>[^<]*' + re.escape(team_a_en) + r'[^<]*<[^>]*>[^<]*(\d+)[^<]*<', re.IGNORECASE),
        ]

        for i, pat in enumerate(score_patterns):
            m = pat.search(html)
            if m:
                if i == 0:
                    return {"score_a": int(m.group(1)), "score_b": int(m.group(2))}
                elif i == 1:
                    # Ordem invertida
                    return {"score_a": int(m.group(2)), "score_b": int(m.group(1))}

        # Fallback: procurar qualquer "Final" ou "FT" com placar
        ft_pattern = re.compile(r'(?:Final|FT|Full.?Time)[^0-9]*?(\d+)\s*[-–]\s*(\d+)', re.IGNORECASE)
        m = ft_pattern.search(html)
        if m:
            return {"score_a": int(m.group(1)), "score_b": int(m.group(2))}

    except Exception as e:
        print(f"  Erro ao buscar resultado no Google: {e}")

    return None


def search_espn_result(team_a_en, team_b_en):
    """Fallback: busca resultado via ESPN."""
    query = urllib.parse.quote(f"site:espn.com FIFA World Cup 2026 {team_a_en} {team_b_en}")
    url = f"https://www.google.com/search?q={query}&hl=en"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        ctx = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')

        # Buscar placar nos snippets
        score_pat = re.compile(r'(\d+)\s*[-–]\s*(\d+)', re.IGNORECASE)
        matches = score_pat.findall(html[:5000])
        if matches:
            # Pegar o primeiro resultado razoável (placar < 20 para cada lado)
            for sa, sb in matches:
                if int(sa) < 20 and int(sb) < 20:
                    return {"score_a": int(sa), "score_b": int(sb)}

    except Exception as e:
        print(f"  Erro ao buscar resultado via ESPN: {e}")

    return None


def generate_summary(team_a, team_b, score_a, score_b, venue, group, date_str):
    """Gera resumo em markdown para uma partida."""
    months = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }

    # Formatar data: "DD/MM/YYYY" → "DD de Mês de YYYY"
    date_parts = date_str.split('/')
    if len(date_parts) == 3:
        day = int(date_parts[0])
        month_name = months.get(date_parts[1], "Junho")
        year = date_parts[2]
        date_formatted = f"{day} de {month_name} de {year}"
    else:
        date_formatted = date_str

    # Determinar resultado
    if score_a > score_b:
        resultado = f"A partida terminou com vitória de **{team_a}** por **{score_a} a {score_b}**."
    elif score_b > score_a:
        resultado = f"A partida terminou com vitória de **{team_b}** por **{score_b} a {score_a}**."
    else:
        resultado = f"A partida terminou empatada em **{score_a} a {score_b}**."

    md = f"""# ⚽ Resumo do Jogo: {team_a} {score_a} - {score_b} {team_b}
**Data:** {date_formatted}  
**Estádio:** {venue}  
**Fase:** Fase de Grupos - Grupo {group}

## 📝 Visão Geral do Jogo
{resultado} O confronto foi válido pela fase de grupos da Copa do Mundo de 2026, Grupo {group}.

## 📊 Resultado Final
| {team_a} | Placar | {team_b} |
|:---:|:---:|:---:|
| {score_a} | X | {score_b} |

---
*Atualizado automaticamente via GitHub Actions.*
"""
    return md


def is_match_past(date_str, time_str):
    """
    Verifica se o jogo já deveria ter terminado baseado na data/hora.
    date_str: "DD/MM/YYYY", time_str: "HH:MM" (horário local Lisboa/UTC+1)
    Adiciona 3 horas de margem após o horário de início.
    """
    try:
        day, month, year = date_str.split('/')
        hour, minute = time_str.split(':')
        # Horário do jogo em UTC+1 (Lisboa)
        match_dt = datetime(int(year), int(month), int(day), int(hour), int(minute))
        # Adicionar 3 horas para garantir que o jogo já terminou
        match_end_estimate = match_dt + timedelta(hours=3)
        # Hora atual em UTC+1
        now = datetime.now(timezone(timedelta(hours=1))).replace(tzinfo=None)
        return now > match_end_estimate
    except Exception:
        return False


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    data_path = os.path.join(base_dir, "data.js")

    print(f"=== Atualização Copa 2026 - {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')} ===")

    # 1. Carregar status.json
    if os.path.exists(status_path):
        with open(status_path, "r", encoding="utf-8") as f:
            status = json.load(f)
    else:
        status = {"last_check": "", "processed_matches": {}}

    # 2. Carregar próximos jogos do data.js
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            data_content = f.read()
        upcoming_schedule = parse_js_upcoming_matches(data_content)
    else:
        print("Erro: data.js não encontrado.")
        return

    print(f"Jogos já processados: {len(status.get('processed_matches', {}))}")
    print(f"Jogos agendados restantes: {len(upcoming_schedule)}")

    processed_ids = set(status.get("processed_matches", {}).keys())
    updated = False

    # 3. Para cada jogo agendado, verificar se já deveria ter terminado
    for game in upcoming_schedule:
        match_id = game["id"]

        # Pular se já processado
        if match_id in processed_ids:
            continue

        # Verificar se o jogo já deveria ter terminado
        if not is_match_past(game["date"], game["time"]):
            continue

        print(f"\n🔍 Verificando: {game['teamA']['name']} vs {game['teamB']['name']} ({game['date']})")

        # Buscar nome em inglês para pesquisa
        team_a_en = NAME_PT_TO_EN.get(game["teamA"]["name"], game["teamA"]["name"])
        team_b_en = NAME_PT_TO_EN.get(game["teamB"]["name"], game["teamB"]["name"])

        # Buscar resultado via Google
        result = search_google_result(team_a_en, team_b_en)

        # Fallback via ESPN
        if not result:
            print("  Google não retornou resultado. Tentando ESPN...")
            result = search_espn_result(team_a_en, team_b_en)

        if not result:
            print(f"  ⚠️ Resultado não encontrado para {game['teamA']['name']} vs {game['teamB']['name']}. Pulando...")
            continue

        score_a = result["score_a"]
        score_b = result["score_b"]
        score_str = f"{score_a}-{score_b}"
        print(f"  ✅ Resultado encontrado: {game['teamA']['name']} {score_a} - {score_b} {game['teamB']['name']}")

        # Converter data DD/MM/YYYY para YYYY-MM-DD
        d_parts = game["date"].split("/")
        status_date = f"{d_parts[2]}-{d_parts[1]}-{d_parts[0]}"

        # Gerar resumo em markdown
        summary_md = generate_summary(
            game["teamA"]["name"], game["teamB"]["name"],
            score_a, score_b,
            game["venue"], game["group"],
            game["date"]
        )

        # Salvar arquivo de resumo
        partidas_dir = os.path.join(base_dir, "partidas")
        os.makedirs(partidas_dir, exist_ok=True)
        summary_path = os.path.join(partidas_dir, f"{match_id}.md")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_md)
        print(f"  📝 Resumo salvo: {summary_path}")

        # Adicionar ao status.json
        status["processed_matches"][match_id] = {
            "date": status_date,
            "teams": [game["teamA"]["name"], game["teamB"]["name"]],
            "score": score_str,
            "summary_file": f"partidas/{match_id}.md"
        }
        updated = True

    # 4. Salvar status.json e reconstruir data.js se houve atualização
    if updated:
        status["last_check"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(status_path, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)
        print(f"\n✅ status.json atualizado com sucesso.")

        # Reconstruir data.js (que também faz git push)
        print("🔄 Reconstruindo data.js...")
        try:
            subprocess.run([sys.executable, "update_helper.py", "rebuild"], cwd=base_dir, check=True)
            print("✅ Reconstrução concluída com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao reconstruir data.js: {e}")
    else:
        print("\n📋 Nenhum novo jogo para atualizar.")
        # Atualizar timestamp do last_check mesmo sem novos jogos
        status["last_check"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(status_path, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)

    print(f"\n=== Atualização finalizada ===")


if __name__ == "__main__":
    main()
