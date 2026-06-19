import json
import os
import sys
import re

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "rebuild":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        rebuild_data_js(base_dir, "2026-06-17")
        sys.exit(0)

    if len(sys.argv) < 10:
        print("Uso: python update_helper.py <id> <date> <group> <teamA> <codeA> <teamB> <codeB> <score> <venue> OU python update_helper.py rebuild")
        sys.exit(1)

    match_id = sys.argv[1]
    date = sys.argv[2]
    group = sys.argv[3]
    teamA = sys.argv[4]
    codeA = sys.argv[5]
    teamB = sys.argv[6]
    codeB = sys.argv[7]
    score = sys.argv[8]
    venue = sys.argv[9]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    data_path = os.path.join(base_dir, "data.js")
    summary_md_path = os.path.join(base_dir, "partidas", f"{match_id}.md")

    # 1. Ler o resumo em markdown
    if not os.path.exists(summary_md_path):
        print(f"Erro: Arquivo de resumo não encontrado em {summary_md_path}")
        sys.exit(1)
        
    with open(summary_md_path, "r", encoding="utf-8") as f:
        summary_md = f.read()

    # 2. Atualizar status.json
    if os.path.exists(status_path):
        with open(status_path, "r", encoding="utf-8") as f:
            status = json.load(f)
    else:
        status = {"last_check": "", "processed_matches": {}}

    status["last_check"] = date + "T12:00:00Z" # Simplificado
    status["processed_matches"][match_id] = {
        "date": date,
        "teams": [teamA, teamB],
        "score": score,
        "summary_file": f"partidas/{match_id}.md"
    }

    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)
    print("status.json atualizado com sucesso.")

    # 3. Atualizar data.js
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extrair o JSON do data.js usando regex
        match = re.search(r"const COPA_DATA = ({[\s\S]*});", content)
        if match:
            json_str = match.group(1)
            # Para evitar erros de parsing de JS puro (como strings com backticks) no Python,
            # vamos ler o arquivo data.js diretamente e atualizar as listas via manipulação de string ou parsing.
            # No entanto, como o data.js é gerado dinamicamente, podemos simplesmente ler o status.json
            # e a pasta partidas/ e reconstruir o data.js do zero!
            # Esta é uma abordagem muito mais limpa e robusta!
            rebuild_data_js(base_dir, date)
        else:
            print("Erro: Não foi possível encontrar a variável COPA_DATA no data.js")
            sys.exit(1)
    else:
        print("data.js não encontrado. Criando um novo...")
        rebuild_data_js(base_dir, date)

def rebuild_data_js(base_dir, current_date):
    status_path = os.path.join(base_dir, "status.json")
    data_path = os.path.join(base_dir, "data.js")
    
    with open(status_path, "r", encoding="utf-8") as f:
        status = json.load(f)
        
    matches_list = []
    
    # Próximos jogos padrão (os que ainda restam do cronograma fixo da fase de grupos)
    upcoming_schedule = [
        # Matchday 1 - 17 de Junho
        {"id": "20260617_portugal_drcongo", "date": "17/06/2026", "time": "18:00", "group": "K", "teamA": {"name": "Portugal", "code": "pt"}, "teamB": {"name": "RD Congo", "code": "cd"}, "venue": "NRG Stadium (Houston, TX)"},
        {"id": "20260617_england_croatia", "date": "17/06/2026", "time": "21:00", "group": "L", "teamA": {"name": "Inglaterra", "code": "gb-eng"}, "teamB": {"name": "Croácia", "code": "hr"}, "venue": "AT&T Stadium (Arlington, TX)"},
        {"id": "20260617_ghana_panama", "date": "17/06/2026", "time": "00:00", "group": "L", "teamA": {"name": "Gana", "code": "gh"}, "teamB": {"name": "Panamá", "code": "pa"}, "venue": "Toronto Stadium (Toronto)"},
        {"id": "20260617_uzbekistan_colombia", "date": "17/06/2026", "time": "03:00", "group": "K", "teamA": {"name": "Uzbequistão", "code": "uz"}, "teamB": {"name": "Colômbia", "code": "co"}, "venue": "Mexico City Stadium (Cidade do México)"},
        
        # Matchday 2 - 18 de Junho (Grupos A, B)
        {"id": "20260618_south_africa_czechia", "date": "18/06/2026", "time": "18:00", "group": "A", "teamA": {"name": "África do Sul", "code": "za"}, "teamB": {"name": "Tchéquia", "code": "cz"}, "venue": "Atlanta Stadium (Atlanta)"},
        {"id": "20260618_switzerland_bosnia", "date": "18/06/2026", "time": "21:00", "group": "B", "teamA": {"name": "Suíça", "code": "ch"}, "teamB": {"name": "Bósnia e Herzegovina", "code": "ba"}, "venue": "Miami Stadium (Miami)"},
        {"id": "20260618_canada_qatar", "date": "18/06/2026", "time": "00:00", "group": "B", "teamA": {"name": "Canadá", "code": "ca"}, "teamB": {"name": "Catar", "code": "qa"}, "venue": "BC Place (Vancouver)"},
        {"id": "20260618_mexico_south_korea", "date": "18/06/2026", "time": "03:00", "group": "A", "teamA": {"name": "México", "code": "mx"}, "teamB": {"name": "Coreia do Sul", "code": "kr"}, "venue": "Estadio Azteca (Cidade do México)"},
        
        # Matchday 2 - 19 de Junho (Grupos C, D)
        {"id": "20260619_scotland_morocco", "date": "19/06/2026", "time": "21:00", "group": "C", "teamA": {"name": "Escócia", "code": "gb-sct"}, "teamB": {"name": "Marrocos", "code": "ma"}, "venue": "Gillette Stadium (Boston)"},
        {"id": "20260619_usa_australia", "date": "19/06/2026", "time": "18:00", "group": "D", "teamA": {"name": "Estados Unidos", "code": "us"}, "teamB": {"name": "Austrália", "code": "au"}, "venue": "SoFi Stadium (Los Angeles)"},
        {"id": "20260619_brazil_haiti", "date": "19/06/2026", "time": "00:00", "group": "C", "teamA": {"name": "Brasil", "code": "br"}, "teamB": {"name": "Haiti", "code": "ht"}, "venue": "MetLife Stadium (New York/New Jersey)"},
        {"id": "20260619_paraguay_turkiye", "date": "19/06/2026", "time": "03:00", "group": "D", "teamA": {"name": "Paraguai", "code": "py"}, "teamB": {"name": "Turquia", "code": "tr"}, "venue": "Dallas Stadium (Dallas)"},
        
        # Matchday 2 - 20 de Junho (Grupos E, F)
        {"id": "20260620_germany_ivorycoast", "date": "20/06/2026", "time": "18:00", "group": "E", "teamA": {"name": "Alemanha", "code": "de"}, "teamB": {"name": "Costa do Marfim", "code": "ci"}, "venue": "Houston Stadium (Houston)"},
        {"id": "20260620_curacao_ecuador", "date": "20/06/2026", "time": "21:00", "group": "E", "teamA": {"name": "Curaçao", "code": "cw"}, "teamB": {"name": "Equador", "code": "ec"}, "venue": "Atlanta Stadium (Atlanta)"},
        {"id": "20260620_netherlands_sweden", "date": "20/06/2026", "time": "00:00", "group": "F", "teamA": {"name": "Holanda", "code": "nl"}, "teamB": {"name": "Suécia", "code": "se"}, "venue": "Dallas Stadium (Dallas)"},
        {"id": "20260620_japan_tunisia", "date": "20/06/2026", "time": "03:00", "group": "F", "teamA": {"name": "Japão", "code": "jp"}, "teamB": {"name": "Tunísia", "code": "tn"}, "venue": "San Francisco Stadium (Santa Clara)"},
        
        # Matchday 2 - 21 de Junho (Grupos G, H)
        {"id": "20260621_belgium_iran", "date": "21/06/2026", "time": "18:00", "group": "G", "teamA": {"name": "Bélgica", "code": "be"}, "teamB": {"name": "Irã", "code": "ir"}, "venue": "Vancouver Stadium (Vancouver)"},
        {"id": "20260621_egypt_newzealand", "date": "21/06/2026", "time": "21:00", "group": "G", "teamA": {"name": "Egito", "code": "eg"}, "teamB": {"name": "Nova Zelândia", "code": "nz"}, "venue": "Kansas City Stadium (Kansas City)"},
        {"id": "20260621_spain_saudiarabia", "date": "21/06/2026", "time": "00:00", "group": "H", "teamA": {"name": "Espanha", "code": "es"}, "teamB": {"name": "Arábia Saudita", "code": "sa"}, "venue": "Seattle Stadium (Seattle)"},
        {"id": "20260621_capeverde_uruguay", "date": "21/06/2026", "time": "03:00", "group": "H", "teamA": {"name": "Cabo Verde", "code": "cv"}, "teamB": {"name": "Uruguai", "code": "uy"}, "venue": "Boston Stadium (Boston)"},
        
        # Matchday 2 - 22 de Junho (Grupos I, J)
        {"id": "20260622_france_norway", "date": "22/06/2026", "time": "18:00", "group": "I", "teamA": {"name": "França", "code": "fr"}, "teamB": {"name": "Noruega", "code": "no"}, "venue": "MetLife Stadium (New York/New Jersey)"},
        {"id": "20260622_senegal_iraq", "date": "22/06/2026", "time": "21:00", "group": "I", "teamA": {"name": "Senegal", "code": "sn"}, "teamB": {"name": "Iraque", "code": "iq"}, "venue": "Gillette Stadium (Boston)"},
        {"id": "20260622_argentina_austria", "date": "22/06/2026", "time": "00:00", "group": "J", "teamA": {"name": "Argentina", "code": "ar"}, "teamB": {"name": "Áustria", "code": "at"}, "venue": "Kansas City Stadium (Kansas City)"},
        {"id": "20260622_algeria_jordan", "date": "22/06/2026", "time": "03:00", "group": "J", "teamA": {"name": "Argélia", "code": "dz"}, "teamB": {"name": "Jordânia", "code": "jo"}, "venue": "San Francisco Stadium (Santa Clara)"},
        
        # Matchday 2 - 23 de Junho (Grupos K, L)
        {"id": "20260623_portugal_uzbekistan", "date": "23/06/2026", "time": "18:00", "group": "K", "teamA": {"name": "Portugal", "code": "pt"}, "teamB": {"name": "Uzbequistão", "code": "uz"}, "venue": "NRG Stadium (Houston, TX)"},
        {"id": "20260623_drcongo_colombia", "date": "23/06/2026", "time": "21:00", "group": "K", "teamA": {"name": "RD Congo", "code": "cd"}, "teamB": {"name": "Colômbia", "code": "co"}, "venue": "Mexico City Stadium (Cidade do México)"},
        {"id": "20260623_england_ghana", "date": "23/06/2026", "time": "00:00", "group": "L", "teamA": {"name": "Inglaterra", "code": "gb-eng"}, "teamB": {"name": "Gana", "code": "gh"}, "venue": "AT&T Stadium (Arlington, TX)"},
        {"id": "20260623_croatia_panama", "date": "23/06/2026", "time": "03:00", "group": "L", "teamA": {"name": "Croácia", "code": "hr"}, "teamB": {"name": "Panamá", "code": "pa"}, "venue": "Toronto Stadium (Toronto)"},
        
        # Matchday 3 - 24 de Junho (Grupos A, B)
        {"id": "20260624_czechia_mexico", "date": "24/06/2026", "time": "18:00", "group": "A", "teamA": {"name": "Tchéquia", "code": "cz"}, "teamB": {"name": "México", "code": "mx"}, "venue": "Estadio Azteca (Cidade do México)"},
        {"id": "20260624_southafrica_southkorea", "date": "24/06/2026", "time": "21:00", "group": "A", "teamA": {"name": "África do Sul", "code": "za"}, "teamB": {"name": "Coreia do Sul", "code": "kr"}, "venue": "BMO Field (Toronto)"},
        {"id": "20260624_bosnia_qatar", "date": "24/06/2026", "time": "00:00", "group": "B", "teamA": {"name": "Bósnia e Herzegovina", "code": "ba"}, "teamB": {"name": "Catar", "code": "qa"}, "venue": "BC Place (Vancouver)"},
        {"id": "20260624_switzerland_canada", "date": "24/06/2026", "time": "03:00", "group": "B", "teamA": {"name": "Suíça", "code": "ch"}, "teamB": {"name": "Canadá", "code": "ca"}, "venue": "Vancouver Stadium (Vancouver)"},
        
        # Matchday 3 - 25 de Junho (Grupos C, D)
        {"id": "20260625_morocco_haiti", "date": "25/06/2026", "time": "18:00", "group": "C", "teamA": {"name": "Marrocos", "code": "ma"}, "teamB": {"name": "Haiti", "code": "ht"}, "venue": "Miami Stadium (Miami)"},
        {"id": "20260625_scotland_brazil", "date": "25/06/2026", "time": "21:00", "group": "C", "teamA": {"name": "Escócia", "code": "gb-sct"}, "teamB": {"name": "Brasil", "code": "br"}, "venue": "MetLife Stadium (New York/New Jersey)"},
        {"id": "20260625_turkiye_usa", "date": "25/06/2026", "time": "00:00", "group": "D", "teamA": {"name": "Turquia", "code": "tr"}, "teamB": {"name": "Estados Unidos", "code": "us"}, "venue": "SoFi Stadium (Los Angeles)"},
        {"id": "20260625_paraguay_australia", "date": "25/06/2026", "time": "03:00", "group": "D", "teamA": {"name": "Paraguai", "code": "py"}, "teamB": {"name": "Austrália", "code": "au"}, "venue": "Dallas Stadium (Dallas)"},
        
        # Matchday 3 - 26 de Junho (Grupos E, F)
        {"id": "20260626_ecuador_germany", "date": "26/06/2026", "time": "18:00", "group": "E", "teamA": {"name": "Equador", "code": "ec"}, "teamB": {"name": "Alemanha", "code": "de"}, "venue": "Houston Stadium (Houston)"},
        {"id": "20260626_curacao_ivorycoast", "date": "26/06/2026", "time": "21:00", "group": "E", "teamA": {"name": "Curaçao", "code": "cw"}, "teamB": {"name": "Costa do Marfim", "code": "ci"}, "venue": "Atlanta Stadium (Atlanta)"},
        {"id": "20260626_tunisia_netherlands", "date": "26/06/2026", "time": "00:00", "group": "F", "teamA": {"name": "Tunísia", "code": "tn"}, "teamB": {"name": "Holanda", "code": "nl"}, "venue": "Dallas Stadium (Dallas)"},
        {"id": "20260626_japan_sweden", "date": "26/06/2026", "time": "03:00", "group": "F", "teamA": {"name": "Japão", "code": "jp"}, "teamB": {"name": "Suécia", "code": "se"}, "venue": "San Francisco Stadium (Santa Clara)"},
        
        # Matchday 3 - 27 de Junho (Grupos G, H)
        {"id": "20260627_newzealand_belgium", "date": "27/06/2026", "time": "18:00", "group": "G", "teamA": {"name": "Nova Zelândia", "code": "nz"}, "teamB": {"name": "Bélgica", "code": "be"}, "venue": "Vancouver Stadium (Vancouver)"},
        {"id": "20260627_egypt_iran", "date": "27/06/2026", "time": "21:00", "group": "G", "teamA": {"name": "Egito", "code": "eg"}, "teamB": {"name": "Irã", "code": "ir"}, "venue": "Kansas City Stadium (Kansas City)"},
        {"id": "20260627_uruguay_spain", "date": "27/06/2026", "time": "00:00", "group": "H", "teamA": {"name": "Uruguai", "code": "uy"}, "teamB": {"name": "Espanha", "code": "es"}, "venue": "Seattle Stadium (Seattle)"},
        {"id": "20260627_capeverde_saudiarabia", "date": "27/06/2026", "time": "03:00", "group": "H", "teamA": {"name": "Cabo Verde", "code": "cv"}, "teamB": {"name": "Arábia Saudita", "code": "sa"}, "venue": "Boston Stadium (Boston)"},
        
        # Matchday 3 - 28 de Junho (Grupos I, J)
        {"id": "20260628_iraq_france", "date": "28/06/2026", "time": "18:00", "group": "I", "teamA": {"name": "Iraque", "code": "iq"}, "teamB": {"name": "França", "code": "fr"}, "venue": "MetLife Stadium (New York/New Jersey)"},
        {"id": "20260628_senegal_norway", "date": "28/06/2026", "time": "21:00", "group": "I", "teamA": {"name": "Senegal", "code": "sn"}, "teamB": {"name": "Noruega", "code": "no"}, "venue": "Gillette Stadium (Boston)"},
        {"id": "20260628_jordan_argentina", "date": "28/06/2026", "time": "00:00", "group": "J", "teamA": {"name": "Jordânia", "code": "jo"}, "teamB": {"name": "Argentina", "code": "ar"}, "venue": "Kansas City Stadium (Kansas City)"},
        {"id": "20260628_algeria_austria", "date": "28/06/2026", "time": "03:00", "group": "J", "teamA": {"name": "Argélia", "code": "dz"}, "teamB": {"name": "Áustria", "code": "at"}, "venue": "San Francisco Stadium (Santa Clara)"},
        
        # Matchday 3 - 29 de Junho (Grupos K, L)
        {"id": "20260629_colombia_portugal", "date": "29/06/2026", "time": "18:00", "group": "K", "teamA": {"name": "Colômbia", "code": "co"}, "teamB": {"name": "Portugal", "code": "pt"}, "venue": "NRG Stadium (Houston, TX)"},
        {"id": "20260629_drcongo_uzbekistan", "date": "29/06/2026", "time": "21:00", "group": "K", "teamA": {"name": "RD Congo", "code": "cd"}, "teamB": {"name": "Uzbequistão", "code": "uz"}, "venue": "Mexico City Stadium (Cidade do México)"},
        {"id": "20260629_panama_england", "date": "29/06/2026", "time": "00:00", "group": "L", "teamA": {"name": "Panamá", "code": "pa"}, "teamB": {"name": "Inglaterra", "code": "gb-eng"}, "venue": "AT&T Stadium (Arlington, TX)"},
        {"id": "20260629_croatia_ghana", "date": "29/06/2026", "time": "03:00", "group": "L", "teamA": {"name": "Croácia", "code": "hr"}, "teamB": {"name": "Gana", "code": "gh"}, "venue": "Toronto Stadium (Toronto)"}
    ]

    # Mapeamento de códigos de países para reconstrução
    country_codes = {
        "México": "mx", "África do Sul": "za", "Coreia do Sul": "kr", "Tchéquia": "cz",
        "Canadá": "ca", "Bósnia e Herzegovina": "ba", "Estados Unidos": "us", "Paraguai": "py",
        "Catar": "qa", "Suíça": "ch", "Brasil": "br", "Marrocos": "ma", "Escócia": "gb-sct",
        "Haiti": "ht", "Austrália": "au", "Turquia": "tr", "Alemanha": "de", "Curaçao": "cw",
        "Holanda": "nl", "Japão": "jp", "Costa do Marfim": "ci", "Equador": "ec", "Suécia": "se",
        "Tunísia": "tn", "Espanha": "es", "Cabo Verde": "cv", "Bélgica": "be", "Egito": "eg",
        "Arábia Saudita": "sa", "Uruguai": "uy", "Irã": "ir", "Nova Zelândia": "nz",
        "França": "fr", "Senegal": "sn", "Noruega": "no", "Iraque": "iq", "Argentina": "ar",
        "Argélia": "dz", "Áustria": "at", "Jordânia": "jo", "Inglaterra": "gb-eng", "Croácia": "hr",
        "Gana": "gh", "Panamá": "pa", "Uzbequistão": "uz", "Colômbia": "co", "RD Congo": "cd"
    }

    # Estádios padrão para os já jogados
    venues = {
        "20260611_mexico_south_africa": "Estadio Azteca (Cidade do México)",
        "20260611_south_korea_czechia": "BMO Field (Toronto)",
        "20260612_canada_bosnia": "BC Place (Vancouver)",
        "20260612_usa_paraguay": "SoFi Stadium (Los Angeles)",
        "20260613_qatar_switzerland": "Gillette Stadium (Boston)",
        "20260613_brazil_morocco": "MetLife Stadium (New York/New Jersey)",
        "20260613_scotland_haiti": "Miami Stadium (Miami)",
        "20260613_australia_turkiye": "Dallas Stadium (Dallas)",
        "20260614_germany_curacao": "Houston Stadium (Houston)",
        "20260614_netherlands_japan": "Dallas Stadium (Dallas)",
        "20260614_ivory_coast_ecuador": "Atlanta Stadium (Atlanta)",
        "20260614_sweden_tunisia": "San Francisco Stadium (Santa Clara)",
        "20260615_spain_cape_verde": "Seattle Stadium (Seattle)",
        "20260615_belgium_egypt": "Vancouver Stadium (Vancouver)",
        "20260615_saudi_arabia_uruguay": "Boston Stadium (Boston)",
        "20260615_iran_new_zealand": "Kansas City Stadium (Kansas City)",
        "20260616_france_senegal": "MetLife Stadium (New York/New Jersey)",
        "20260616_norway_iraq": "Gillette Stadium (Boston)",
        "20260616_argentina_algeria": "Kansas City Stadium (Kansas City)",
        "20260616_austria_jordan": "San Francisco Stadium (Santa Clara)",
        "20260618_south_africa_czechia": "Atlanta Stadium (Atlanta)",
        "20260618_switzerland_bosnia": "SoFi Stadium (Los Angeles)",
        "20260618_canada_qatar": "BC Place (Vancouver)",
        "20260618_mexico_south_korea": "Estadio Azteca (Cidade do México)"
    }
    
    # Identificar grupo a partir do ID ou de dados anteriores
    groups = {
        "20260611_mexico_south_africa": "A", "20260611_south_korea_czechia": "A",
        "20260612_canada_bosnia": "B", "20260612_usa_paraguay": "D",
        "20260613_qatar_switzerland": "B", "20260613_brazil_morocco": "C",
        "20260613_scotland_haiti": "C", "20260613_australia_turkiye": "D",
        "20260614_germany_curacao": "E", "20260614_netherlands_japan": "F",
        "20260614_ivory_coast_ecuador": "E", "20260614_sweden_tunisia": "F",
        "20260615_spain_cape_verde": "H", "20260615_belgium_egypt": "G",
        "20260615_saudi_arabia_uruguay": "H", "20260615_iran_new_zealand": "G",
        "20260616_france_senegal": "I", "20260616_norway_iraq": "I",
        "20260616_argentina_algeria": "J", "20260616_austria_jordan": "J",
        "20260618_south_africa_czechia": "A", "20260618_switzerland_bosnia": "B",
        "20260618_canada_qatar": "B", "20260618_mexico_south_korea": "A"
    }

    # Alimentar dinamicamente a partir do cronograma de próximos jogos
    for game in upcoming_schedule:
        venues[game["id"]] = game["venue"]
        groups[game["id"]] = game["group"]

    # Reconstruir lista de jogos concluídos
    for mid, info in status["processed_matches"].items():
        teamA, teamB = info["teams"]
        codeA = country_codes.get(teamA, "un")
        codeB = country_codes.get(teamB, "un")
        group = groups.get(mid, "K" if "portugal" in mid or "colombia" in mid else "L")
        venue = venues.get(mid, "Estádio da Copa")
        
        md_file = os.path.join(base_dir, "partidas", f"{mid}.md")
        summary_text = ""
        if os.path.exists(md_file):
            with open(md_file, "r", encoding="utf-8") as f:
                summary_text = f.read()
                
        matches_list.append({
            "id": mid,
            "date": info["date"],
            "group": group,
            "teamA": {"name": teamA, "code": codeA},
            "teamB": {"name": teamB, "code": codeB},
            "score": info["score"],
            "venue": venue,
            "summary_md": summary_text
        })

    # Filtrar próximos jogos que já foram concluídos
    processed_ids = set(status["processed_matches"].keys())
    remaining_upcoming = [game for game in upcoming_schedule if game["id"] not in processed_ids]

    # Gerar o arquivo data.js
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("const COPA_DATA = {\n")
        f.write(f'  last_check: "{current_date}T14:48:56Z",\n')
        f.write("  matches: [\n")
        
        for idx, m in enumerate(matches_list):
            f.write("    {\n")
            f.write(f'      id: "{m["id"]}",\n')
            f.write(f'      date: "{m["date"]}",\n')
            f.write(f'      group: "{m["group"]}",\n')
            f.write(f'      teamA: {{ name: "{m["teamA"]["name"]}", code: "{m["teamA"]["code"]}" }},\n')
            f.write(f'      teamB: {{ name: "{m["teamB"]["name"]}", code: "{m["teamB"]["code"]}" }},\n')
            f.write(f'      score: "{m["score"]}",\n')
            f.write(f'      venue: "{m["venue"]}",\n')
            # Escrever o resumo em markdown usando template literals do JS (backticks)
            # Precisamos apenas escapar backticks e cifrões dentro do markdown
            escaped_md = m["summary_md"].replace("`", "\\`").replace("$", "\\$")
            f.write(f'      summary_md: `{escaped_md}`\n')
            
            if idx == len(matches_list) - 1:
                f.write("    }\n")
            else:
                f.write("    },\n")
                
        f.write("  ],\n")
        f.write("  upcoming_matches: [\n")
        
        for idx, g in enumerate(remaining_upcoming):
            f.write("    {\n")
            f.write(f'      id: "{g["id"]}",\n')
            f.write(f'      date: "{g["date"]}",\n')
            f.write(f'      time: "{g["time"]}",\n')
            f.write(f'      group: "{g["group"]}",\n')
            f.write(f'      teamA: {{ name: "{g["teamA"]["name"]}", code: "{g["teamA"]["code"]}" }},\n')
            f.write(f'            teamB: {{ name: "{g["teamB"]["name"]}", code: "{g["teamB"]["code"]}" }},\n')
            f.write(f'      venue: "{g["venue"]}"\n')
            
            if idx == len(remaining_upcoming) - 1:
                f.write("    }\n")
            else:
                f.write("    },\n")
                
        f.write("  ],\n")

        # Escrever país e suas histórias
        country_histories = {
            "mx": "O México tem uma rica história que remonta às civilizações Asteca e Maia, colonizado pela Espanha em 1521. No futebol, é uma força tradicional da CONCACAF, sediando sua terceira Copa do Mundo (1970, 1986 e 2026), e conhecido pela paixão de sua torcida.",
            "za": "Localizada no extremo sul do continente africano, tem sua história moderna marcada pela luta contra o Apartheid e a liderança de Nelson Mandela. No futebol, sediou a icônica Copa de 2010 e seus 'Bafana Bafana' são muito queridos.",
            "kr": "Uma das nações mais tecnológicas do mundo, com uma rica história dinástica milenar. É uma das seleções mais vitoriosas da Ásia, alcançando a histórica semifinal na Copa do Mundo de 2002.",
            "cz": "Localizada no coração da Europa Central, sua história inclui o Reino da Boêmia e a antiga Tchecoslováquia. No futebol, tem um histórico glorioso como vice-campeã mundial em 1934 e 1962.",
            "ca": "O segundo maior país em território, colonizado por franceses e ingleses, conhecido pela multiculturalidade. O futebol tem crescido exponencialmente, com esta sendo sua segunda Copa consecutiva.",
            "ba": "Localizada nos Bálcãs, declarou independência em 1992. Sua história é marcada pela resiliência. Estreou em Copas do Mundo em 2014, revelando grandes jogadores técnicos no futebol europeu.",
            "qa": "Um pequeno e próspero emirado no Golfo Pérsico, que se tornou um polo esportivo global ao sediar a histórica Copa do Mundo de 2022.",
            "ch": "Conhecida por sua neutralidade histórica, paisagens alpinas e precisão tecnológica. No futebol, é uma presença constante nas oitavas de final de Copas do Mundo, com um jogo tático muito forte.",
            "br": "O maior país da América do Sul, colonizado por Portugal. É o berço do 'Futebol Arte' e o único pentacampeão mundial (1958, 1962, 1970, 1994, 2002), exportando craques para todo o planeta.",
            "ma": "Localizado no Norte da África, tem uma fusão de influências berberes, árabes e europeias. Fez história ao se tornar a primeira seleção africana a chegar a uma semifinal de Copa do Mundo em 2022.",
            "ht": "Primeira república negra independente do mundo (1804). Sua história é marcada pela resiliência e riqueza cultural. Participou da Copa do Mundo em 1974 e busca inspirar sua população através do esporte.",
            "gb-sct": "Parte do Reino Unido, a Escócia é famosa por seus castelos, clãs e gaita de foles. Participou da primeira partida internacional de futebol da história contra a Inglaterra em 1872.",
            "us": "Potência econômica e cultural global. O futebol (soccer) tem crescido em popularidade massiva, tendo alcançado as quartas de final em 2002 e sendo um dos anfitriões em 2026.",
            "py": "País bilíngue (espanhol e guarani) no coração da América do Sul. No futebol, é reconhecido por sua defesa intransponível e espírito de garra, tendo alcançado as quartas de final em 2010.",
            "au": "Uma nação continental com fauna única e praias famosas. Seus 'Socceroos' são conhecidos pelo vigor físico, com destaque para a campanha de oitavas de final na Copa de 2006.",
            "tr": "Uma ponte entre a Europa e a Ásia, com uma história rica que abrange os impérios Bizantino e Otomano. Conquistou o histórico 3º lugar na Copa do Mundo de 2002.",
            "de": "Localizada no centro da Europa, é uma das potências industriais do mundo. No futebol, é tetracampeã mundial (1954, 1974, 1990, 2014), famosa por sua organização e força mental.",
            "cw": "Uma ilha caribenha que faz parte do Reino dos Países Baixos. Faz sua estreia histórica em Copas do Mundo em 2026, com uma equipe rápida inspirada na escola de futebol holandesa.",
            "ci": "Localizada na África Ocidental, é um grande produtor de cacau. Seus 'Elefantes' ganharam destaque mundial com a geração de Didier Drogba nos anos 2000.",
            "ec": "Nomeado devido à linha do equador, possui a incrível biodiversidade de Galápagos. No futebol, tem se consolidado como força sul-americana, com campanhas sólidas em Copas recentes.",
            "nl": "Famosa pelos moinhos de vento, canais e engenharia de diques. Revolucionou o futebol nos anos 70 com o 'Futebol Total' de Johan Cruyff, tendo sido finalista em 1974, 1978 e 2010.",
            "jp": "Arquipélago asiático conhecido pela mistura de tradição milenar e tecnologia de ponta. No futebol, os 'Samurais Azuis' são conhecidos pela disciplina tática e velocidade.",
            "se": "Nação escandinava de alto padrão de vida e história viking. No futebol, foi vice-campeã mundial em 1958 em casa e conquistou o terceiro lugar em 1994.",
            "tn": "Localizada no Norte da África, abriga as ruínas da antiga Cartago. Suas 'Águias de Cartago' participam frequentemente do torneio, marcados por uma defesa compacta.",
            "be": "Sede da União Europeia, famosa pelos chocolates e cervejas. Sua geração de ouro conquistou o terceiro lugar na Copa do Mundo de 2018 com um ataque letal.",
            "eg": "Egito é o lar da civilização dos Faraós e das pirâmides milenares. No futebol, os 'Faraós' são a maior potência da Copa Africana de Nações, com o atacante Mo Salah como ícone moderno.",
            "ir": "Berço do antigo Império Persa, com uma riqueza cultural e poética milenar. É uma das potências do futebol asiático, conhecida pela resiliência defensiva em Copas do Mundo.",
            "nz": "Famosa pelas paisagens naturais cinematográficas e cultura Maori. Seus 'All Whites' fizeram uma campanha histórica e invicta na fase de grupos da Copa de 2010.",
            "es": "Rica história marcada pelo Império Espanhol, arte e flamenco. No futebol, dominou o mundo de 2008 a 2012 com o estilo 'Tiki-Taka', consagrando-se campeã da Copa de 2010.",
            "cv": "Um arquipélago vulcânico na costa oeste da África, colonizado por Portugal. Seus 'Tubarões Azuis' fazem uma estreia histórica na Copa do Mundo de 2026 com futebol alegre.",
            "sa": "Localizada na península arábica, abriga os locais mais sagrados do Islã. Protagonizou uma das maiores zebras da história ao vencer a campeã Argentina na Copa de 2022.",
            "uy": "País de forte tradição agropecuária e leis progressistas pioneiras. No futebol, é o gigante pioneiro do esporte, tendo vencido as Copas de 1930 e 1950 ('Maracanazo').",
            "fr": "Polo cultural, literário e político na Europa Ocidental. No futebol, os 'Bleus' são bicampeões mundiais (1998, 2018) e exportam grandes talentos para todo o mundo.",
            "sn": "Localizado no ponto mais ocidental da África, conhecido pela hospitalidade ('Teranga'). Seus 'Leões da Teranga' alcançaram as quartas de final em sua estreia em 2002.",
            "no": "Famosa pelos fiordes majestosos e riqueza impulsionada pela energia sustentável. No futebol, retorna ao grande palco mundial liderada pelo artilheiro implacável Erling Haaland.",
            "iq": "Conhecido historicamente como a Mesopotâmia, o berço da escrita e das primeiras cidades. Sua seleção de futebol é conhecida por unir o país em momentos de festa nacional.",
            "ar": "Nação sul-americana famosa pelo tango, gastronomia e literatura. No futebol, é tricampeã mundial (1978, 1986, 2022), embalada pelas lendas de Maradona e Lionel Messi.",
            "dz": "O maior país da África em território, com rica história de independência. Suas 'Raposas do Deserto' são conhecidas pela técnica refinada e espírito guerreiro de luta.",
            "at": "Famosa pela música clássica (Mozart) e palácios imperiais dos Habsburgo. Teve uma grande era de futebol nos anos 30 ('Wunderteam') e busca reviver sua glória.",
            "jo": "Lar da cidade histórica de Petra e do Mar Morto. A seleção jordaniana faz sua estreia histórica no torneio em 2026, celebrando a maior conquista esportiva do país.",
            "pt": "Nação ibérica de exploradores marítimos e fado. No futebol, revelou lendas como Eusébio, Figo e Cristiano Ronaldo, conquistando a Eurocopa em 2016.",
            "cd": "Localizada no coração da África, possui a segunda maior floresta tropical do mundo. O país tem uma rica cultura musical e retorna à Copa buscando surpreender com futebol físico.",
            "uz": "Uma parada chave na antiga Rota da Seda, famosa pela arquitetura de azulejos azuis de Samarcanda. Estreia na Copa de 2026 com futebol técnico de estilo central-asiático.",
            "co": "Conhecida pelo café de alta qualidade e incrível biodiversidade. No futebol, encanta o mundo com sua torcida alegre e equipes talentosas, com destaque para a Copa de 2014.",
            "gb-eng": "Berço do futebol moderno, do Parlamento e dos Beatles. Conquistou a Copa do Mundo de 1966 em casa e possui a liga nacional de clubes mais assistida do planeta.",
            "hr": "Famosa por sua bela costa no Adriático e cidades muradas. É uma superpotência recente do futebol, tendo sido vice-campeã em 2018 e terceira colocada em 1998 e 2022.",
            "gh": "Primeiro país subsaariano a declarar independência (1957). Os 'Black Stars' encantam o futebol mundial pela alegria e alcançaram as quartas de final de forma dramática em 2010.",
            "pa": "Famoso pelo canal transoceânico que liga o Atlântico ao Pacífico. Seus 'Canaleros' disputam sua segunda Copa do Mundo, movidos pela paixão e dedicação dos seus atletas."
        }

        teams_list = [
            {"name": "México", "code": "mx", "group": "A"},
            {"name": "África do Sul", "code": "za", "group": "A"},
            {"name": "Coreia do Sul", "code": "kr", "group": "A"},
            {"name": "Tchéquia", "code": "cz", "group": "A"},
            {"name": "Canadá", "code": "ca", "group": "B"},
            {"name": "Bósnia e Herzegovina", "code": "ba", "group": "B"},
            {"name": "Catar", "code": "qa", "group": "B"},
            {"name": "Suíça", "code": "ch", "group": "B"},
            {"name": "Brasil", "code": "br", "group": "C"},
            {"name": "Marrocos", "code": "ma", "group": "C"},
            {"name": "Haiti", "code": "ht", "group": "C"},
            {"name": "Escócia", "code": "gb-sct", "group": "C"},
            {"name": "Estados Unidos", "code": "us", "group": "D"},
            {"name": "Paraguai", "code": "py", "group": "D"},
            {"name": "Austrália", "code": "au", "group": "D"},
            {"name": "Turquia", "code": "tr", "group": "D"},
            {"name": "Alemanha", "code": "de", "group": "E"},
            {"name": "Curaçao", "code": "cw", "group": "E"},
            {"name": "Costa do Marfim", "code": "ci", "group": "E"},
            {"name": "Equador", "code": "ec", "group": "E"},
            {"name": "Holanda", "code": "nl", "group": "F"},
            {"name": "Japão", "code": "jp", "group": "F"},
            {"name": "Suécia", "code": "se", "group": "F"},
            {"name": "Tunísia", "code": "tn", "group": "F"},
            {"name": "Bélgica", "code": "be", "group": "G"},
            {"name": "Egito", "code": "eg", "group": "G"},
            {"name": "Irã", "code": "ir", "group": "G"},
            {"name": "Nova Zelândia", "code": "nz", "group": "G"},
            {"name": "Espanha", "code": "es", "group": "H"},
            {"name": "Cabo Verde", "code": "cv", "group": "H"},
            {"name": "Arábia Saudita", "code": "sa", "group": "H"},
            {"name": "Uruguai", "code": "uy", "group": "H"},
            {"name": "França", "code": "fr", "group": "I"},
            {"name": "Senegal", "code": "sn", "group": "I"},
            {"name": "Noruega", "code": "no", "group": "I"},
            {"name": "Iraque", "code": "iq", "group": "I"},
            {"name": "Argentina", "code": "ar", "group": "J"},
            {"name": "Argélia", "code": "dz", "group": "J"},
            {"name": "Áustria", "code": "at", "group": "J"},
            {"name": "Jordânia", "code": "jo", "group": "J"},
            {"name": "Portugal", "code": "pt", "group": "K"},
            {"name": "RD Congo", "code": "cd", "group": "K"},
            {"name": "Uzbequistão", "code": "uz", "group": "K"},
            {"name": "Colômbia", "code": "co", "group": "K"},
            {"name": "Inglaterra", "code": "gb-eng", "group": "L"},
            {"name": "Croácia", "code": "hr", "group": "L"},
            {"name": "Gana", "code": "gh", "group": "L"},
            {"name": "Panamá", "code": "pa", "group": "L"}
        ]

        f.write("  country_histories: {\n")
        for c_idx, (code, history) in enumerate(country_histories.items()):
            escaped_hist = history.replace('"', '\\"').replace('\n', '\\n')
            if c_idx == len(country_histories) - 1:
                f.write(f'    "{code}": "{escaped_hist}"\n')
            else:
                f.write(f'    "{code}": "{escaped_hist}",\n')
        f.write("  },\n")
        
        f.write("  teams_list: [\n")
        for t_idx, t in enumerate(teams_list):
            if t_idx == len(teams_list) - 1:
                f.write(f'    {{ name: "{t["name"]}", code: "{t["code"]}", group: "{t["group"]}" }}\n')
            else:
                f.write(f'    {{ name: "{t["name"]}", code: "{t["code"]}", group: "{t["group"]}" }},\n')
        f.write("  ]\n")
        f.write("};\n")
    print("data.js reconstruído e atualizado com sucesso.")
    git_push(base_dir)

def git_push(base_dir):
    import subprocess
    git_path = r"C:\Users\User\AppData\Local\OpenClaw\deps\portable-git\mingw64\bin\git.exe"
    if not os.path.exists(git_path):
        print("Aviso: Git executável portátil não encontrado em:", git_path)
        return
        
    try:
        dot_git = os.path.join(base_dir, ".git")
        if not os.path.exists(dot_git):
            print("Inicializando repositório Git local...")
            subprocess.run([git_path, "init"], cwd=base_dir, check=True)
            subprocess.run([git_path, "config", "user.name", "Copa Bot"], cwd=base_dir, check=True)
            subprocess.run([git_path, "config", "user.email", "copabot@example.com"], cwd=base_dir, check=True)
            
        print("Adicionando arquivos ao Git...")
        subprocess.run([git_path, "add", "."], cwd=base_dir, check=True)
        
        # Verificar se há mudanças
        status_proc = subprocess.run([git_path, "status", "--porcelain"], cwd=base_dir, capture_output=True, text=True, check=True)
        if not status_proc.stdout.strip():
            print("Sem alterações para commitar.")
            return
            
        print("Criando commit...")
        subprocess.run([git_path, "commit", "-m", "git commit update"], cwd=base_dir, check=True)
        subprocess.run([git_path, "branch", "-M", "main"], cwd=base_dir, check=True)
        
        # Verificar se existe remote 'origin'
        remotes_proc = subprocess.run([git_path, "remote"], cwd=base_dir, capture_output=True, text=True, check=True)
        if "origin" not in remotes_proc.stdout:
            print("Aviso: Remote 'origin' não configurado. Adicione o remote para permitir o push automático.")
            return
            
        print("Fazendo push para o GitHub...")
        subprocess.run([git_path, "push", "-u", "origin", "main"], cwd=base_dir, check=True)
        print("Push automático realizado com sucesso!")
    except Exception as e:
        print(f"Erro no push automático do Git: {e}")

if __name__ == "__main__":
    main()
