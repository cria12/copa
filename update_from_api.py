import json
import os
import urllib.request
import re
import subprocess
from datetime import datetime

# Mapeamento de nomes em inglês da API para português do dashboard
name_en_to_pt = {
    "Mexico": "México",
    "South Africa": "África do Sul",
    "South Korea": "Coreia do Sul",
    "Czech Republic": "Tchéquia",
    "Czechia": "Tchéquia",
    "Canada": "Canadá",
    "Bosnia and Herzegovina": "Bósnia e Herzegovina",
    "Qatar": "Catar",
    "Switzerland": "Suíça",
    "Brazil": "Brasil",
    "Morocco": "Marrocos",
    "Haiti": "Haiti",
    "Scotland": "Escócia",
    "United States": "Estados Unidos",
    "Paraguay": "Paraguai",
    "Australia": "Austrália",
    "Turkey": "Turquia",
    "Germany": "Alemanha",
    "Curaçao": "Curaçao",
    "Ivory Coast": "Costa do Marfim",
    "Ecuador": "Equador",
    "Netherlands": "Holanda",
    "Japan": "Japão",
    "Sweden": "Suécia",
    "Tunisia": "Tunísia",
    "Iran": "Irã",
    "New Zealand": "Nova Zelândia",
    "Spain": "Espanha",
    "Cape Verde": "Cabo Verde",
    "Belgium": "Bélgica",
    "Egypt": "Egito",
    "Saudi Arabia": "Arábia Saudita",
    "Uruguay": "Uruguai",
    "France": "França",
    "Senegal": "Senegal",
    "Norway": "Noruega",
    "Iraq": "Iraque",
    "Argentina": "Argentina",
    "Algeria": "Argélia",
    "Austria": "Áustria",
    "Jordan": "Jordânia",
    "Portugal": "Portugal",
    "Democratic Republic of the Congo": "RD Congo",
    "DR Congo": "RD Congo",
    "Uzbekistan": "Uzbequistão",
    "Colombia": "Colômbia",
    "England": "Inglaterra",
    "Croatia": "Croácia",
    "Ghana": "Gana",
    "Panama": "Panamá"
}

def clean_scorers(scorers_str):
    if not scorers_str or scorers_str == "null" or scorers_str == "None":
        return "Nenhum"
    for char in ['{', '}', '[', ']', '"', '“', '”', '`']:
        scorers_str = scorers_str.replace(char, '')
    scorers = [s.strip() for s in scorers_str.split(',') if s.strip()]
    return ", ".join(scorers) if scorers else "Nenhum"

def generate_summary(teamA, teamB, scoreA, scoreB, venue, group, date_str, home_scorers, away_scorers):
    months = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }
    date_parts = date_str.split('/')
    if len(date_parts) == 3:
        day = int(date_parts[0])
        month_name = months.get(date_parts[1], "Junho")
        year = date_parts[2]
        date_formatted = f"{day} de {month_name} de {year}"
    else:
        date_formatted = date_str

    md = f"""# ⚽ Resumo do Jogo: {teamA} {scoreA} - {scoreB} {teamB}
**Data:** {date_formatted}  
**Estádio:** {venue}  
**Fase:** Fase de Grupos - Grupo {group}

## 📝 Visão Geral do Jogo
A partida entre **{teamA}** e **{teamB}** terminou com o placar final de **{scoreA} a {scoreB}**. O confronto foi válido pela fase de grupos da Copa do Mundo de 2026.

## ⚽ Marcadores e Lances Importantes
- **Gols de {teamA}**: {home_scorers}
- **Gols de {teamB}**: {away_scorers}

---
*Atualizado automaticamente via GitHub Actions.*
"""
    return md

def parse_js_upcoming_matches(content):
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

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    data_path = os.path.join(base_dir, "data.js")

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

    # 3. Buscar jogos da API
    url = "https://worldcup26.ir/get/games"
    print(f"Buscando dados da API: {url}")
    api_data = None
    try:
        import ssl
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=context) as response:
            html = response.read().decode('utf-8')
            api_data = json.loads(html)
    except Exception as e:
        print(f"urllib falhou ({e}), tentando curl...")
        try:
            result = subprocess.run(["curl", "-s", "-k", url], capture_output=True, text=True, check=True)
            api_data = json.loads(result.stdout)
        except Exception as curl_err:
            print(f"Erro ao acessar a API com curl: {curl_err}")
            return

    if not api_data:
        print("Erro: Nenhum dado retornado da API.")
        return

    games = api_data.get("games", [])
    print(f"Total de jogos retornados pela API: {len(games)}")

    updated = False

    for game in games:
        # Só processamos se o jogo estiver finalizado
        # A API retorna finished como string "TRUE" ou "FALSE"
        if game.get("finished") != "TRUE":
            continue

        home_en = game.get("home_team_name_en")
        away_en = game.get("away_team_name_en")
        
        home_pt = name_en_to_pt.get(home_en, home_en)
        away_pt = name_en_to_pt.get(away_en, away_en)

        # Converter data do formato API (ex: 06/17/2026 12:00) para DD/MM/YYYY
        api_date_raw = game.get("local_date", "")
        if not api_date_raw:
            continue
        try:
            date_part = api_date_raw.split(" ")[0]
            month, day, year = date_part.split("/")
            api_date_formatted = f"{day}/{month}/{year}"
            status_date = f"{year}-{month}-{day}"
        except Exception:
            print(f"Erro ao formatar data: {api_date_raw}")
            continue

        # Encontrar jogo correspondente na nossa lista de próximos jogos
        matched_match = None
        for sched in upcoming_schedule:
            if sched["date"] == api_date_formatted:
                # Compara os nomes das seleções
                if (sched["teamA"]["name"] == home_pt and sched["teamB"]["name"] == away_pt) or \
                   (sched["teamA"]["name"] == away_pt and sched["teamB"]["name"] == home_pt):
                    matched_match = sched
                    break

        if not matched_match:
            # Tentar buscar sem a data, apenas pelos times caso haja descompasso de fuso/data
            for sched in upcoming_schedule:
                if (sched["teamA"]["name"] == home_pt and sched["teamB"]["name"] == away_pt) or \
                   (sched["teamA"]["name"] == away_pt and sched["teamB"]["name"] == home_pt):
                    matched_match = sched
                    break

        if not matched_match:
            continue

        match_id = matched_match["id"]

        # Se já está processado no status.json, pula
        if match_id in status.get("processed_matches", {}):
            continue

        print(f"Novo jogo finalizado encontrado! {home_pt} x {away_pt} (ID: {match_id})")

        # Organizar placar de acordo com a ordem do schedule (teamA e teamB)
        home_score = game.get("home_score", "0")
        away_score = game.get("away_score", "0")
        if matched_match["teamA"]["name"] == home_pt:
            score_str = f"{home_score}-{away_score}"
            teamA_scorers = clean_scorers(game.get("home_scorers"))
            teamB_scorers = clean_scorers(game.get("away_scorers"))
        else:
            score_str = f"{away_score}-{home_score}"
            teamA_scorers = clean_scorers(game.get("away_scorers"))
            teamB_scorers = clean_scorers(game.get("home_scorers"))

        # Criar o resumo da partida em markdown
        summary_md = generate_summary(
            matched_match["teamA"]["name"],
            matched_match["teamB"]["name"],
            score_str.split("-")[0],
            score_str.split("-")[1],
            matched_match["venue"],
            matched_match["group"],
            api_date_formatted,
            teamA_scorers,
            teamB_scorers
        )

        # Gravar arquivo de resumo
        partidas_dir = os.path.join(base_dir, "partidas")
        os.makedirs(partidas_dir, exist_ok=True)
        summary_path = os.path.join(partidas_dir, f"{match_id}.md")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_md)
        print(f"Resumo gravado em: {summary_path}")

        # Adicionar ao status.json
        status["processed_matches"][match_id] = {
            "date": status_date,
            "teams": [matched_match["teamA"]["name"], matched_match["teamB"]["name"]],
            "score": score_str,
            "summary_file": f"partidas/{match_id}.md"
        }
        updated = True

    if updated:
        # Gravar status.json
        status["last_check"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(status_path, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)
        print("status.json atualizado com sucesso.")

        # Rodar o rebuild chamando o update_helper.py
        print("Executando reconstrução do data.js...")
        try:
            # Chamamos o rebuild usando python
            subprocess.run(["python", "update_helper.py", "rebuild"], cwd=base_dir, check=True)
            print("Reconstrução concluída com sucesso!")
        except Exception as e:
            print(f"Erro ao chamar update_helper.py: {e}")
    else:
        print("Nenhum novo jogo para atualizar.")

if __name__ == "__main__":
    main()
