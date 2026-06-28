#!/usr/bin/env python3
"""
Batch: 12 últimos jogos da fase de grupos + atualizar schedule com eliminatórias (Round of 32).
"""
import json, os, sys
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

matches = [
    {"id":"20260622_france_norway","date":"2026-06-26","teams":["França","Noruega"],"score":"4-1","group":"I",
     "summary":"""# ⚽ Resumo do Jogo: França 4 - 1 Noruega
**Data:** 26 de Junho de 2026  
**Estádio:** MetLife Stadium (New York/New Jersey)  
**Fase:** Fase de Grupos - Grupo I

## 📝 Visão Geral do Jogo
A **França** goleou a **Noruega** por **4 a 1** com uma exibição brilhante de **Ousmane Dembélé**, que marcou um hat-trick nos primeiros 32 minutos. A vitória garantiu à França o primeiro lugar do Grupo I.

## ⚽ Marcadores e Lances Importantes
- **Gols da França**: Ousmane Dembélé (hat-trick: 3 gols), Désiré Doué (90+')
- **Gols da Noruega**: Thelo Aasgaard

## 🔑 Momentos Decisivos
- **Dembélé** marcou três gols fulminantes nos primeiros 32 minutos, deixando a defesa norueguesa sem reação.
- **Thelo Aasgaard** descontou para a Noruega, mas o resultado já estava definido.
- **Désiré Doué** fechou a goleada nos acréscimos. A França terminou líder do Grupo I.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260622_senegal_iraq","date":"2026-06-26","teams":["Senegal","Iraque"],"score":"5-0","group":"I",
     "summary":"""# ⚽ Resumo do Jogo: Senegal 5 - 0 Iraque
**Data:** 26 de Junho de 2026  
**Estádio:** Toronto Stadium (Toronto)  
**Fase:** Fase de Grupos - Grupo I

## 📝 Visão Geral do Jogo
O **Senegal** aplicou uma goleada histórica de **5 a 0** sobre o **Iraque**, com destaque para **Pape Gueye** (2 gols). O Iraque teve Rebin Sulaka expulso por cartão vermelho após revisão do VAR.

## ⚽ Marcadores e Lances Importantes
- **Gols do Senegal**: Habib Diarra (4'), Ismaïla Sarr (56'), Pape Gueye (59', 71'), Iliman Ndiaye (82')
- **Cartão Vermelho**: Rebin Sulaka (Iraque) — expulsão após VAR

## 🔑 Momentos Decisivos
- **Habib Diarra** abriu o placar logo aos 4 minutos. Após a expulsão de Sulaka, o Senegal dominou.
- **Pape Gueye** marcou duas vezes em 12 minutos. O Senegal terminou 3º no Grupo I e buscava vaga como melhor terceiro.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260627_uruguay_spain","date":"2026-06-26","teams":["Uruguai","Espanha"],"score":"0-1","group":"H",
     "summary":"""# ⚽ Resumo do Jogo: Uruguai 0 - 1 Espanha
**Data:** 26 de Junho de 2026  
**Estádio:** Guadalajara Stadium (Zapopan, México)  
**Fase:** Fase de Grupos - Grupo H

## 📝 Visão Geral do Jogo
A **Espanha** venceu o **Uruguai** por **1 a 0** com gol de **Alex Baena**, garantindo o 1º lugar do Grupo H com 7 pontos. O Uruguai foi eliminado.

## ⚽ Marcadores e Lances Importantes
- **Gols da Espanha**: Alex Baena (42')
- **Cartão Vermelho**: Agustín Canobbio (Uruguai) — nos acréscimos

## 🔑 Momentos Decisivos
- **Alex Baena** aproveitou um erro do goleiro Muslera para marcar aos 42 minutos.
- A Espanha dominou e Canobbio foi expulso nos acréscimos, selando uma noite amarga para o Uruguai.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260627_capeverde_saudiarabia","date":"2026-06-26","teams":["Cabo Verde","Arábia Saudita"],"score":"0-0","group":"H",
     "summary":"""# ⚽ Resumo do Jogo: Cabo Verde 0 - 0 Arábia Saudita
**Data:** 26 de Junho de 2026  
**Estádio:** Boston Stadium (Boston, MA)  
**Fase:** Fase de Grupos - Grupo H

## 📝 Visão Geral do Jogo
**Cabo Verde** e **Arábia Saudita** empataram sem gols num resultado **histórico**: Cabo Verde, na sua primeira Copa do Mundo, classificou-se para os 32 avos de final como 2º do Grupo H, tornando-se a menor nação (por população) a chegar à fase eliminatória de um Mundial masculino.

## ⚽ Marcadores e Lances Importantes
- Nenhum gol

## 🔑 Momentos Decisivos
- O empate foi suficiente para Cabo Verde se classificar, provocando cenas de celebração emocionante.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260627_newzealand_belgium","date":"2026-06-27","teams":["Nova Zelândia","Bélgica"],"score":"1-5","group":"G",
     "summary":"""# ⚽ Resumo do Jogo: Nova Zelândia 1 - 5 Bélgica
**Data:** 27 de Junho de 2026  
**Estádio:** BC Place (Vancouver)  
**Fase:** Fase de Grupos - Grupo G

## 📝 Visão Geral do Jogo
A **Bélgica** goleou a **Nova Zelândia** por **5 a 1**, com **Leandro Trossard** a marcar dois gols e **Kevin De Bruyne** e **Romelu Lukaku** a juntarem-se à festa.

## ⚽ Marcadores e Lances Importantes
- **Gols da Bélgica**: Leandro Trossard (28', 50'), Kevin De Bruyne (66'), Romelu Lukaku (86'), Alexis Saelemaekers (90+4')
- **Gols da Nova Zelândia**: Elijah Just (84')

## 🔑 Momentos Decisivos
- **Trossard** brilhou com um bis no primeiro tempo e início do segundo. A Bélgica terminou líder do Grupo G.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260627_egypt_iran","date":"2026-06-27","teams":["Egito","Irã"],"score":"1-1","group":"G",
     "summary":"""# ⚽ Resumo do Jogo: Egito 1 - 1 Irã
**Data:** 27 de Junho de 2026  
**Estádio:** Kansas City Stadium (Kansas City, MO)  
**Fase:** Fase de Grupos - Grupo G

## 📝 Visão Geral do Jogo
**Egito** e **Irã** empataram por **1 a 1**. O Egito classificou-se como 2º do Grupo G, enquanto o Irã ficou em 3º lugar.

## ⚽ Marcadores e Lances Importantes
- **Gols do Egito**: Mahmoud Saber (5')
- **Gols do Irã**: Ramin Rezaeian (14')

## 🔑 Momentos Decisivos
- **Saber** abriu o placar rapidamente aos 5 minutos. **Rezaeian** empatou aos 14'. O empate classificou o Egito.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260629_panama_england","date":"2026-06-27","teams":["Panamá","Inglaterra"],"score":"0-2","group":"L",
     "summary":"""# ⚽ Resumo do Jogo: Panamá 0 - 2 Inglaterra
**Data:** 27 de Junho de 2026  
**Estádio:** MetLife Stadium (New York/New Jersey)  
**Fase:** Fase de Grupos - Grupo L

## 📝 Visão Geral do Jogo
A **Inglaterra** derrotou o **Panamá** por **2 a 0** com gols de **Jude Bellingham** e **Harry Kane**, garantindo o 1º lugar do Grupo L.

## ⚽ Marcadores e Lances Importantes
- **Gols da Inglaterra**: Jude Bellingham (62'), Harry Kane (67')
- **Gols do Panamá**: Nenhum

## 🔑 Momentos Decisivos
- **Bellingham** desbloqueou o jogo aos 62' com um remate de fora da área. **Kane** ampliou 5 minutos depois.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260629_croatia_ghana","date":"2026-06-27","teams":["Croácia","Gana"],"score":"2-1","group":"L",
     "summary":"""# ⚽ Resumo do Jogo: Croácia 2 - 1 Gana
**Data:** 27 de Junho de 2026  
**Estádio:** Lincoln Financial Field (Filadélfia, PA)  
**Fase:** Fase de Grupos - Grupo L

## 📝 Visão Geral do Jogo
A **Croácia** venceu o **Gana** por **2 a 1** num jogo dramático, garantindo vaga na fase eliminatória.

## ⚽ Marcadores e Lances Importantes
- **Gols da Croácia**: Petar Sučić (31'), Nikola Vlašić (83')
- **Gols de Gana**: Derrick Luckassen (73')

## 🔑 Momentos Decisivos
- **Sučić** abriu o placar. Gana empatou por **Luckassen** (73'). **Vlašić** marcou o gol da vitória aos 83'.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260628_jordan_argentina","date":"2026-06-27","teams":["Jordânia","Argentina"],"score":"1-3","group":"J",
     "summary":"""# ⚽ Resumo do Jogo: Jordânia 1 - 3 Argentina
**Data:** 27 de Junho de 2026  
**Estádio:** AT&T Stadium (Arlington, TX)  
**Fase:** Fase de Grupos - Grupo J

## 📝 Visão Geral do Jogo
A **Argentina** venceu a **Jordânia** por **3 a 1**, com **Lionel Messi** a entrar como suplente e marcar, tornando-se o primeiro jogador a marcar em **sete jogos consecutivos** de Copa do Mundo.

## ⚽ Marcadores e Lances Importantes
- **Gols da Argentina**: Giovani Lo Celso (19'), Lautaro Martínez (31' pen.), Lionel Messi (80')
- **Gols da Jordânia**: Mousa Al-Tamari (55')

## 🔑 Momentos Decisivos
- **Lo Celso** abriu o placar. **Lautaro** ampliou de penálti. **Al-Tamari** reduziu. **Messi** saiu do banco e marcou aos 80' — recorde histórico!

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260628_algeria_austria","date":"2026-06-27","teams":["Argélia","Áustria"],"score":"3-3","group":"J",
     "summary":"""# ⚽ Resumo do Jogo: Argélia 3 - 3 Áustria
**Data:** 27 de Junho de 2026  
**Estádio:** GEHA Field at Arrowhead Stadium (Kansas City, MO)  
**Fase:** Fase de Grupos - Grupo J

## 📝 Visão Geral do Jogo
**Argélia** e **Áustria** empataram por **3 a 3** num jogo absolutamente épico, com gols nos acréscimos de ambos os lados. O empate classificou ambas as equipas para o mata-mata!

## ⚽ Marcadores e Lances Importantes
- **Gols da Argélia**: Belghali (41'), Riyad Mahrez (60', 90+3')
- **Gols da Áustria**: Marko Arnautović (28'), Marcel Sabitzer (55'), Saša Kalajdžić (90+5')

## 🔑 Momentos Decisivos
- **Arnautović** abriu. **Belghali** empatou. **Sabitzer** deu vantagem à Áustria. **Mahrez** empatou. Nos acréscimos: **Mahrez** (90+3') e **Kalajdžić** (90+5') — um final de loucos!

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260629_colombia_portugal","date":"2026-06-27","teams":["Colômbia","Portugal"],"score":"0-0","group":"K",
     "summary":"""# ⚽ Resumo do Jogo: Colômbia 0 - 0 Portugal
**Data:** 27 de Junho de 2026  
**Estádio:** NRG Stadium (Houston, TX)  
**Fase:** Fase de Grupos - Grupo K

## 📝 Visão Geral do Jogo
**Colômbia** e **Portugal** empataram sem gols num jogo tático e equilibrado. A Colômbia terminou líder do Grupo K, e Portugal classificou-se como 2º colocado.

## ⚽ Marcadores e Lances Importantes
- Nenhum gol

## 🔑 Momentos Decisivos
- Jogo muito disputado e cauteloso. Ambas as equipas já classificadas jogaram com prudência.

---
*Atualizado automaticamente via Copa Bot.*
"""},
    {"id":"20260629_drcongo_uzbekistan","date":"2026-06-27","teams":["RD Congo","Uzbequistão"],"score":"3-1","group":"K",
     "summary":"""# ⚽ Resumo do Jogo: RD Congo 3 - 1 Uzbequistão
**Data:** 27 de Junho de 2026  
**Estádio:** Mexico City Stadium (Cidade do México)  
**Fase:** Fase de Grupos - Grupo K

## 📝 Visão Geral do Jogo
A **RD Congo** conquistou a sua **primeira vitória de sempre** numa Copa do Mundo ao derrotar o **Uzbequistão** por **3 a 1**, classificando-se para a fase eliminatória de forma histórica. Enfrentará a Inglaterra nos 32 avos de final.

## ⚽ Marcadores e Lances Importantes
- **Gols da RD Congo**: Yoane Wissa (68' pen., 90+1'), Fiston Mayele (78')
- **Gols do Uzbequistão**: Eldor Shomurodov (10')

## 🔑 Momentos Decisivos
- **Shomurodov** deu vantagem ao Uzbequistão aos 10'. A RD Congo reagiu no 2º tempo: **Wissa** empatou de penálti, **Mayele** virou, e **Wissa** fechou nos acréscimos. Vitória histórica!

---
*Atualizado automaticamente via Copa Bot.*
"""},
]

# Processar
status_path = os.path.join(BASE_DIR, "status.json")
with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

count = 0
for m in matches:
    mid = m["id"]
    if mid in status["processed_matches"]:
        print(f"⏭️  Já processado: {mid}")
        continue
    md_path = os.path.join(BASE_DIR, "partidas", f"{mid}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(m["summary"].strip() + "\n")
    status["processed_matches"][mid] = {
        "date": m["date"], "teams": m["teams"],
        "score": m["score"], "summary_file": f"partidas/{mid}.md"
    }
    print(f"📝 {mid}: {m['teams'][0]} {m['score']} {m['teams'][1]}")
    count += 1

status["last_check"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(status_path, "w", encoding="utf-8") as f:
    json.dump(status, f, indent=2, ensure_ascii=False)

print(f"\n✅ {count} jogos processados! Total: {len(status['processed_matches'])}")
