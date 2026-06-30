#!/usr/bin/env python3
"""
Script para processar as primeiras 4 partidas dos 32 avos de final (Round of 32) da Copa do Mundo 2026.
Atualiza status.json e gera os resumos markdown de alta qualidade.
"""
import json
import os
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

matches_r32 = [
    {
        "id": "R32_southafrica_canada",
        "date": "2026-06-28",
        "teams": ["África do Sul", "Canadá"],
        "score": "0-1",
        "group": "R32",
        "venue": "SoFi Stadium (Los Angeles)",
        "summary": """# ⚽ Resumo do Jogo: África do Sul 0 - 1 Canadá
**Data:** 28 de Junho de 2026  
**Estádio:** SoFi Stadium (Los Angeles, CA)  
**Fase:** 32 avos de final (Round of 32)

## 📝 Visão Geral do Jogo
O **Canadá** venceu a **África do Sul** por **1 a 0** em Los Angeles, garantindo sua classificação dramática para as oitavas de final da Copa do Mundo de 2026. O gol da vitória foi marcado no apagar das luzes da partida pelo meio-campista Stephen Eustáquio.

## ⚽ Marcadores e Lances Importantes
- **Gols do Canadá**: Stephen Eustáquio (90+2')
- **Gols da África do Sul**: Nenhum

## 🔑 Momentos Decisivos
- O jogo foi marcado por muito equilíbrio e intensidade tática, com a África do Sul se defendendo com maestria e buscando os contra-ataques.
- Quando o confronto parecia se encaminhar para a prorrogação, **Stephen Eustáquio** aproveitou um rebote na entrada da área aos 90+2' para chutar rasteiro e vencer o goleiro sul-africano.
- Com a vitória dramática, o Canadá avança de fase e segue fazendo história na competição, enquanto a valente seleção sul-africana encerra sua trajetória de orgulho no torneio.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "R32_brazil_japan",
        "date": "2026-06-29",
        "teams": ["Brasil", "Japão"],
        "score": "2-1",
        "group": "R32",
        "venue": "Houston Stadium (Houston, TX)",
        "summary": """# ⚽ Resumo do Jogo: Brasil 2 - 1 Japão
**Data:** 29 de Junho de 2026  
**Estádio:** Houston Stadium (Houston, TX)  
**Fase:** 32 avos de final (Round of 32)

## 📝 Visão Geral do Jogo
O **Brasil** avançou para as oitavas de final após derrotar o **Japão** de virada por **2 a 1** em Houston. O gol da vitória brasileira foi marcado nos acréscimos do segundo tempo por Gabriel Martinelli, coroando uma partida eletrizante e cheia de tensão.

## ⚽ Marcadores e Lances Importantes
- **Gols do Brasil**: Casemiro (56'), Gabriel Martinelli (90+5')
- **Gols do Japão**: Kaishu Sano (29')

## 🔑 Momentos Decisivos
- O Japão surpreendeu a defesa brasileira aos 29 minutos, abrindo o placar com uma finalização certeira de **Kaishu Sano**.
- No segundo tempo, o Brasil aumentou a pressão e empatou aos 56 minutos com uma cabeçada imponente do capitão **Casemiro** após cobrança de escanteio.
- Nos minutos finais, quando ambas as equipes já demonstravam desgaste, **Gabriel Martinelli** recebeu assistência precisa na área e finalizou cruzado aos 90+5' para dar a vitória e a classificação ao Brasil.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "R32_germany_paraguay",
        "date": "2026-06-29",
        "teams": ["Alemanha", "Paraguai"],
        "score": "1-1 (3-4 GP)",
        "group": "R32",
        "venue": "Gillette Stadium (Boston, MA)",
        "summary": """# ⚽ Resumo do Jogo: Alemanha 1 - 1 Paraguai (3-4 nos pênaltis)
**Data:** 29 de Junho de 2026  
**Estádio:** Gillette Stadium (Boston, MA)  
**Fase:** 32 avos de final (Round of 32)

## 📝 Visão Geral do Jogo
O **Paraguai** chocou o mundo ao eliminar a **Alemanha** nos pênaltis por **4 a 3**, após um empate por **1 a 1** no tempo regulamentar e prorrogação. Foi uma das maiores surpresas da história da competição e a primeira vez que a Alemanha perde uma disputa de pênaltis na história das Copas do Mundo.

## ⚽ Marcadores e Lances Importantes
- **Gols da Alemanha**: Kai Havertz (54')
- **Gols do Paraguai**: Julio Enciso (42')
- **Decisão por Pênaltis**: Paraguai venceu por 4 a 3 (Jose Canale converteu a cobrança decisiva)

## 🔑 Momentos Decisivos
- O Paraguai abriu o placar aos 42 minutos com um belo gol do jovem talento **Julio Enciso**.
- A Alemanha buscou o empate no segundo tempo, com **Kai Havertz** finalizando com precisão aos 54 minutos.
- O placar permaneceu inalterado até o fim dos 120 minutos.
- Na histórica disputa de pênaltis, a precisão paraguaia prevaleceu, e **Jose Canale** marcou o pênalti decisivo que garantiu a vaga histórica do Paraguai nas oitavas de final.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "R32_netherlands_morocco",
        "date": "2026-06-29",
        "teams": ["Holanda", "Marrocos"],
        "score": "1-1 (2-3 GP)",
        "group": "R32",
        "venue": "Estadio Monterrey (Monterrey, México)",
        "summary": """# ⚽ Resumo do Jogo: Holanda 1 - 1 Marrocos (2-3 nos pênaltis)
**Data:** 29 de Junho de 2026  
**Estádio:** Estadio Monterrey (Monterrey, México)  
**Fase:** 32 avos de final (Round of 32)

## 📝 Visão Geral do Jogo
**Marrocos** carimbou o passaporte para as oitavas de final ao derrotar a **Holanda** na disputa por pênaltis por **3 a 2**, após um empate por **1 a 1** persistir no tempo regulamentar e prorrogação. Os Leões do Atlas enfrentam o Canadá na próxima fase.

## ⚽ Marcadores e Lances Importantes
- **Gols da Holanda**: Cody Gakpo (72')
- **Gols de Marrocos**: Issa Diop (90+1')
- **Decisão por Pênaltis**: Marrocos venceu por 3 a 2

## 🔑 Momentos Decisivos
- A Holanda abriu o placar aos 72 minutos através de seu principal atacante, **Cody Gakpo**, inflamando a torcida holandesa.
- Marrocos não desistiu e, nos acréscimos do segundo tempo (90+1'), **Issa Diop** igualou o marcador com uma cabeçada certeira após cobrança de falta na área.
- Após uma prorrogação tensa e sem gols, a estrela do goleiro marroquino brilhou nos pênaltis, ajudando Marrocos a vencer por 3 a 2.

---
*Atualizado automaticamente via Copa Bot.*
"""
    }
]

# Atualizar status.json
status_path = os.path.join(BASE_DIR, "status.json")
with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

count = 0
for m in matches_r32:
    mid = m["id"]
    if mid in status["processed_matches"]:
        print(f"⏭️ Já processado: {mid}")
        continue
    
    # Salvar resumo .md
    md_path = os.path.join(BASE_DIR, "partidas", f"{mid}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(m["summary"].strip() + "\n")
        
    status["processed_matches"][mid] = {
        "date": m["date"],
        "teams": m["teams"],
        "score": m["score"],
        "summary_file": f"partidas/{mid}.md"
    }
    print(f"📝 {mid}: {m['teams'][0]} {m['score']} {m['teams'][1]}")
    count += 1

status["last_check"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(status_path, "w", encoding="utf-8") as f:
    json.dump(status, f, indent=2, ensure_ascii=False)

print(f"\n✅ {count} jogos dos 32 avos processados! Total: {len(status['processed_matches'])}")
