#!/usr/bin/env python3
"""
Script para processar os 16 jogos de 23-26 de Junho de 2026.
Cria resumos detalhados, atualiza status.json e reconstrói data.js.
"""
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 16 jogos para processar com resultados REAIS pesquisados
matches_to_process = [
    {
        "id": "20260623_portugal_uzbekistan",
        "date": "2026-06-23",
        "teams": ["Portugal", "Uzbequistão"],
        "score": "5-0",
        "group": "K",
        "venue": "NRG Stadium (Houston, TX)",
        "summary": """# ⚽ Resumo do Jogo: Portugal 5 - 0 Uzbequistão
**Data:** 23 de Junho de 2026  
**Estádio:** NRG Stadium (Houston, TX)  
**Fase:** Fase de Grupos - Grupo K

## 📝 Visão Geral do Jogo
**Portugal** aplicou uma goleada histórica de **5 a 0** sobre o **Uzbequistão** em Houston, numa noite que ficará para a história do futebol mundial. Cristiano Ronaldo tornou-se o primeiro jogador a marcar em **seis Copas do Mundo diferentes**, superando também Eusébio como maior goleador de Portugal em mundiais.

## ⚽ Marcadores e Lances Importantes
- **Gols de Portugal**: Cristiano Ronaldo (2 gols), Nuno Mendes (livre direto), Abduvohid Nematov (autogolo), Rafael Leão (87')
- **Gols do Uzbequistão**: Nenhum

## 🔑 Momentos Decisivos
- **Cristiano Ronaldo** abriu o placar e estabeleceu um recorde histórico ao marcar em sua sexta Copa do Mundo — feito inédito no futebol mundial.
- **Nuno Mendes** ampliou com um belo gol de livre direto, colocando a bola no ângulo.
- O goleiro uzbeque **Abduvohid Nematov** cometeu um infeliz autogolo ao tentar defender um cruzamento rasteiro.
- **Ronaldo** marcou mais uma vez, superando **Eusébio** como maior artilheiro de Portugal em Copas do Mundo.
- **Rafael Leão** fechou a goleada aos 87 minutos com uma jogada individual brilhante.
- Portugal garantiu a liderança do Grupo K com campanha perfeita.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260623_drcongo_colombia",
        "date": "2026-06-23",
        "teams": ["RD Congo", "Colômbia"],
        "score": "0-1",
        "group": "K",
        "venue": "Mexico City Stadium (Cidade do México)",
        "summary": """# ⚽ Resumo do Jogo: RD Congo 0 - 1 Colômbia
**Data:** 23 de Junho de 2026  
**Estádio:** Guadalajara Stadium (Zapopan, México)  
**Fase:** Fase de Grupos - Grupo K

## 📝 Visão Geral do Jogo
A **Colômbia** venceu a **RD Congo** por **1 a 0** numa partida equilibrada em Zapopan, com um gol decisivo no segundo tempo que garantiu a classificação colombiana para a fase eliminatória.

## ⚽ Marcadores e Lances Importantes
- **Gols da Colômbia**: Daniel Muñoz (76')
- **Gols da RD Congo**: Nenhum

## 🔑 Momentos Decisivos
- A primeira metade foi marcada pelo equilíbrio, com ambas as seleções se anulando taticamente.
- Aos 76 minutos, **Daniel Muñoz** apareceu na área para finalizar com precisão e abrir o placar para a Colômbia.
- A RD Congo tentou pressionar nos minutos finais, mas a defesa colombiana manteve-se sólida.
- Com a vitória, a Colômbia assegurou a classificação no Grupo K.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260623_england_ghana",
        "date": "2026-06-23",
        "teams": ["Inglaterra", "Gana"],
        "score": "0-0",
        "group": "L",
        "venue": "AT&T Stadium (Arlington, TX)",
        "summary": """# ⚽ Resumo do Jogo: Inglaterra 0 - 0 Gana
**Data:** 23 de Junho de 2026  
**Estádio:** AT&T Stadium (Arlington, TX)  
**Fase:** Fase de Grupos - Grupo L

## 📝 Visão Geral do Jogo
**Inglaterra** e **Gana** empataram sem gols em Arlington, numa partida frustrante para os ingleses que não conseguiram furar a defesa ganense apesar da forte pressão, sobretudo na reta final do jogo.

## ⚽ Marcadores e Lances Importantes
- **Gols da Inglaterra**: Nenhum
- **Gols de Gana**: Nenhum

## 🔑 Momentos Decisivos
- A Inglaterra dominou a posse de bola, mas encontrou uma muralha defensiva de Gana muito bem organizada.
- Nos minutos finais, a pressão inglesa intensificou-se, mas a defesa ganense segurou firme.
- O empate manteve ambas as equipas com possibilidades de classificação, dependendo dos resultados da última jornada.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260623_croatia_panama",
        "date": "2026-06-23",
        "teams": ["Croácia", "Panamá"],
        "score": "1-0",
        "group": "L",
        "venue": "Toronto Stadium (Toronto)",
        "summary": """# ⚽ Resumo do Jogo: Croácia 1 - 0 Panamá
**Data:** 23 de Junho de 2026  
**Estádio:** Toronto Stadium (Toronto)  
**Fase:** Fase de Grupos - Grupo L

## 📝 Visão Geral do Jogo
A **Croácia** derrotou o **Panamá** por **1 a 0** em Toronto, graças a um gol do suplente **Ante Budimir** no segundo tempo. A partida marcou a 200ª internacionalização do capitão **Luka Modrić**, e a vitória deu à Croácia os seus primeiros três pontos no torneio.

## ⚽ Marcadores e Lances Importantes
- **Gols da Croácia**: Ante Budimir (54')
- **Gols do Panamá**: Nenhum

## 🔑 Momentos Decisivos
- O primeiro tempo foi disputado, com o Panamá a mostrar organização defensiva.
- Aos 54 minutos, o suplente **Ante Budimir** entrou decisivo e marcou o único gol da partida.
- **Luka Modrić** celebrou a marca histórica de 200 jogos pela seleção croata com a braçadeira de capitão.
- O resultado confirmou a eliminação do Panamá da competição.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260624_czechia_mexico",
        "date": "2026-06-24",
        "teams": ["Tchéquia", "México"],
        "score": "0-3",
        "group": "A",
        "venue": "Estadio Azteca (Cidade do México)",
        "summary": """# ⚽ Resumo do Jogo: Tchéquia 0 - 3 México
**Data:** 24 de Junho de 2026  
**Estádio:** Estadio Azteca (Cidade do México)  
**Fase:** Fase de Grupos - Grupo A

## 📝 Visão Geral do Jogo
O **México** goleou a **Tchéquia** por **3 a 0** no mítico Estádio Azteca, completando uma campanha perfeita na fase de grupos com três vitórias em três jogos e terminando na liderança do Grupo A.

## ⚽ Marcadores e Lances Importantes
- **Gols do México**: Mateo Chávez (55'), Julián Quiñones (61'), Álvaro Fidalgo (90+4')
- **Gols da Tchéquia**: Nenhum

## 🔑 Momentos Decisivos
- O primeiro tempo terminou sem gols, com a Tchéquia a resistir à pressão mexicana.
- **Mateo Chávez** abriu o placar aos 55 minutos, desencadeando a avalanche mexicana.
- Apenas 6 minutos depois, **Julián Quiñones** ampliou com um gol de classe.
- **Álvaro Fidalgo** selou a goleada nos acréscimos (90+4'), arrancando ovação do Azteca.
- A Tchéquia foi eliminada da competição com esta derrota.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260624_southafrica_southkorea",
        "date": "2026-06-24",
        "teams": ["África do Sul", "Coreia do Sul"],
        "score": "1-0",
        "group": "A",
        "venue": "BMO Field (Toronto)",
        "summary": """# ⚽ Resumo do Jogo: África do Sul 1 - 0 Coreia do Sul
**Data:** 24 de Junho de 2026  
**Estádio:** Monterrey Stadium (Guadalupe, México)  
**Fase:** Fase de Grupos - Grupo A

## 📝 Visão Geral do Jogo
A **África do Sul** fez história ao derrotar a **Coreia do Sul** por **1 a 0**, classificando-se para a fase eliminatória de uma Copa do Mundo pela primeira vez em sua história. Um gol solitário de **Thapelo Maseko** no segundo tempo foi o suficiente para selar esta conquista histórica.

## ⚽ Marcadores e Lances Importantes
- **Gols da África do Sul**: Thapelo Maseko (63')
- **Gols da Coreia do Sul**: Nenhum

## 🔑 Momentos Decisivos
- O primeiro tempo foi equilibrado, sem gols mas com boas chances para ambos os lados.
- Aos 63 minutos, **Thapelo Maseko** marcou o gol que mudou a história do futebol sul-africano, finalizando com classe dentro da área.
- A defesa sul-africana resistiu à pressão coreana nos minutos finais para proteger a vantagem.
- A classificação da África do Sul para o mata-mata foi celebrada como um dos momentos mais emocionantes desta Copa.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260624_bosnia_qatar",
        "date": "2026-06-24",
        "teams": ["Bósnia e Herzegovina", "Catar"],
        "score": "3-1",
        "group": "B",
        "venue": "BC Place (Vancouver)",
        "summary": """# ⚽ Resumo do Jogo: Bósnia e Herzegovina 3 - 1 Catar
**Data:** 24 de Junho de 2026  
**Estádio:** Lumen Field (Seattle, WA)  
**Fase:** Fase de Grupos - Grupo B

## 📝 Visão Geral do Jogo
A **Bósnia e Herzegovina** venceu o **Catar** por **3 a 1** em Seattle, com uma exibição convincente que garantiu a sua passagem ao mata-mata como uma das melhores terceiras colocadas, enquanto o Catar foi eliminado do torneio.

## ⚽ Marcadores e Lances Importantes
- **Gols da Bósnia**: Kerim Alajbegovic (29'), Mahmud Abunada (34', autogolo), Ermin Mahmic (80')
- **Gols do Catar**: Hassan Al-Haydos (42')

## 🔑 Momentos Decisivos
- **Kerim Alajbegovic** abriu o placar aos 29 minutos com uma finalização à meia-volta.
- Apenas 5 minutos depois, o goleiro catariano **Mahmud Abunada** cometeu um autogolo infeliz ao tentar defender um cruzamento.
- O capitão do Catar, **Hassan Al-Haydos**, reduziu aos 42 minutos com um gol de penálti, reacendendo a esperança.
- **Ermin Mahmic** fechou o placar aos 80 minutos, selando a vitória bósnia e eliminando o Catar.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260624_switzerland_canada",
        "date": "2026-06-24",
        "teams": ["Suíça", "Canadá"],
        "score": "2-1",
        "group": "B",
        "venue": "Vancouver Stadium (Vancouver)",
        "summary": """# ⚽ Resumo do Jogo: Suíça 2 - 1 Canadá
**Data:** 24 de Junho de 2026  
**Estádio:** BC Place (Vancouver)  
**Fase:** Fase de Grupos - Grupo B

## 📝 Visão Geral do Jogo
A **Suíça** derrotou o **Canadá** por **2 a 1** em Vancouver, conquistando a liderança do Grupo B. O Canadá, apesar da derrota, classificou-se como segundo colocado.

## ⚽ Marcadores e Lances Importantes
- **Gols da Suíça**: Rubén Vargas (46'), Johan Manzambi (57')
- **Gols do Canadá**: Promise David (76')

## 🔑 Momentos Decisivos
- O primeiro tempo terminou empatado sem gols, num jogo cauteloso.
- Logo no início do segundo tempo, **Rubén Vargas** abriu o placar aos 46 minutos com um chute colocado.
- **Johan Manzambi** ampliou aos 57 minutos, parecendo selar o resultado.
- O suplente **Promise David** descontou para o Canadá aos 76 minutos, gerando tensão nos minutos finais.
- A Suíça segurou o resultado e terminou na liderança do Grupo B.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260625_morocco_haiti",
        "date": "2026-06-24",
        "teams": ["Marrocos", "Haiti"],
        "score": "4-2",
        "group": "C",
        "venue": "Miami Stadium (Miami)",
        "summary": """# ⚽ Resumo do Jogo: Marrocos 4 - 2 Haiti
**Data:** 24 de Junho de 2026  
**Estádio:** Miami Stadium (Miami Gardens, FL)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
**Marrocos** venceu o **Haiti** por **4 a 2** num jogo espetacular e cheio de alternâncias em Miami. Apesar de o Haiti ter tomado a frente duas vezes, Marrocos mostrou resiliência e qualidade para virar o jogo e garantir a classificação para a fase eliminatória.

## ⚽ Marcadores e Lances Importantes
- **Gols de Marrocos**: Achraf Hakimi (39'), Ismael Saibari (45+1'), Soufiane Rahimi (78'), Gessime Yassine (89')
- **Gols do Haiti**: Yassine Bounou (10', autogolo), Wilson Isidor (43')

## 🔑 Momentos Decisivos
- O Haiti surpreendeu ao abrir o placar logo aos 10 minutos graças a um autogolo de **Yassine Bounou**.
- **Achraf Hakimi** empatou aos 39 minutos com um chute potente de fora da área.
- **Wilson Isidor** devolveu a vantagem ao Haiti aos 43 minutos.
- Ainda antes do intervalo, **Ismael Saibari** empatou novamente (45+1'), levando o jogo para o intervalo em 2-2.
- No segundo tempo, Marrocos dominou: **Soufiane Rahimi** (78') e **Gessime Yassine** (89') selaram a virada e a goleada.
- Marrocos terminou em segundo no Grupo C, atrás do Brasil.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260625_scotland_brazil",
        "date": "2026-06-24",
        "teams": ["Escócia", "Brasil"],
        "score": "0-3",
        "group": "C",
        "venue": "MetLife Stadium (New York/New Jersey)",
        "summary": """# ⚽ Resumo do Jogo: Escócia 0 - 3 Brasil
**Data:** 24 de Junho de 2026  
**Estádio:** Miami Stadium (Miami Gardens, FL)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
O **Brasil** goleou a **Escócia** por **3 a 0** com uma exibição brilhante, liderada por **Vinícius Júnior** que marcou dois gols no primeiro tempo. A Seleção Brasileira confirmou a liderança do Grupo C com esta vitória convincente.

## ⚽ Marcadores e Lances Importantes
- **Gols do Brasil**: Vinícius Júnior (7', 45+2'), Matheus Cunha (2º tempo)
- **Gols da Escócia**: Nenhum

## 🔑 Momentos Decisivos
- Logo aos 7 minutos, **Vinícius Júnior** abriu o placar com uma jogada individual desconcertante, passando por dois defensores antes de finalizar no canto.
- **Vinícius** marcou novamente nos acréscimos do primeiro tempo (45+2'), com uma finalização precisa que deixou o goleiro escocês sem chance.
- No segundo tempo, **Matheus Cunha** fechou a conta, confirmando a superioridade brasileira.
- O Brasil garantiu o primeiro lugar do Grupo C e avançou com confiança para a fase eliminatória.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260625_turkiye_usa",
        "date": "2026-06-25",
        "teams": ["Turquia", "Estados Unidos"],
        "score": "3-2",
        "group": "D",
        "venue": "SoFi Stadium (Los Angeles)",
        "summary": """# ⚽ Resumo do Jogo: Turquia 3 - 2 Estados Unidos
**Data:** 25 de Junho de 2026  
**Estádio:** SoFi Stadium (Los Angeles, CA)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
A **Turquia** venceu os **Estados Unidos** por **3 a 2** num jogo dramático em Los Angeles, com o gol da vitória a surgir nos últimos segundos dos acréscimos. Apesar da derrota, os EUA já estavam classificados como primeiros do Grupo D.

## ⚽ Marcadores e Lances Importantes
- **Gols da Turquia**: Arda Güler (10'), Barış Alper Yılmaz (31'), Kaan Ayhan (90+8')
- **Gols dos EUA**: Auston Trusty (3'), Sebastian Berhalter (49')

## 🔑 Momentos Decisivos
- **Auston Trusty** abriu o placar logo aos 3 minutos para os EUA com um cabeceamento certeiro.
- **Arda Güler** empatou aos 10 minutos com um chute espetacular de fora da área, demonstrando todo o seu talento.
- **Barış Alper Yılmaz** virou o jogo para a Turquia aos 31 minutos.
- No segundo tempo, **Sebastian Berhalter** empatou novamente para os EUA aos 49 minutos.
- O gol dramático da vitória turca veio aos 90+8' por **Kaan Ayhan**, num cabeceamento após escanteio, arrancando euforia da torcida turca presente no SoFi Stadium.
- A Turquia, apesar da vitória, já estava eliminada do torneio.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260625_paraguay_australia",
        "date": "2026-06-25",
        "teams": ["Paraguai", "Austrália"],
        "score": "0-0",
        "group": "D",
        "venue": "Dallas Stadium (Dallas)",
        "summary": """# ⚽ Resumo do Jogo: Paraguai 0 - 0 Austrália
**Data:** 25 de Junho de 2026  
**Estádio:** San Francisco Bay Area Stadium (Santa Clara, CA)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
**Paraguai** e **Austrália** empataram sem gols em Santa Clara, num resultado que classificou a **Austrália** como segunda colocada do Grupo D para a fase eliminatória da Copa do Mundo de 2026.

## ⚽ Marcadores e Lances Importantes
- **Gols do Paraguai**: Nenhum
- **Gols da Austrália**: Nenhum

## 🔑 Momentos Decisivos
- O jogo foi marcado pela cautela de ambas as seleções, ambas cientes de que o empate beneficiava a Austrália.
- Paraguai teve as melhores chances, mas não conseguiu converter em gol.
- A Austrália garantiu a classificação como vice-líder do Grupo D com este empate estratégico.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260626_ecuador_germany",
        "date": "2026-06-25",
        "teams": ["Equador", "Alemanha"],
        "score": "2-1",
        "group": "E",
        "venue": "Houston Stadium (Houston)",
        "summary": """# ⚽ Resumo do Jogo: Equador 2 - 1 Alemanha
**Data:** 25 de Junho de 2026  
**Estádio:** Houston Stadium (Houston, TX)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
O **Equador** surpreendeu ao derrotar a **Alemanha** por **2 a 1** em Houston, garantindo a classificação para a fase eliminatória. A Alemanha abriu o placar rapidamente, mas o Equador mostrou garra e qualidade para virar o resultado.

## ⚽ Marcadores e Lances Importantes
- **Gols do Equador**: Nilson Angulo (9'), Gonzalo Plata (77')
- **Gols da Alemanha**: Leroy Sané (2')

## 🔑 Momentos Decisivos
- A Alemanha começou fulminante, com **Leroy Sané** a abrir o placar logo aos 2 minutos com um chute potente.
- O Equador reagiu rapidamente: **Nilson Angulo** empatou aos 9 minutos, restabelecendo o equilíbrio.
- O jogo manteve-se empatado até os 77 minutos, quando **Gonzalo Plata** marcou o gol da virada com uma finalização precisa no canto.
- O Equador segurou o resultado e garantiu vaga no mata-mata, numa das surpresas da fase de grupos.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260626_curacao_ivorycoast",
        "date": "2026-06-25",
        "teams": ["Curaçao", "Costa do Marfim"],
        "score": "0-2",
        "group": "E",
        "venue": "Atlanta Stadium (Atlanta)",
        "summary": """# ⚽ Resumo do Jogo: Curaçao 0 - 2 Costa do Marfim
**Data:** 25 de Junho de 2026  
**Estádio:** Philadelphia Stadium (Filadélfia, PA)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
A **Costa do Marfim** derrotou **Curaçao** por **2 a 0**, com **Nicolas Pépé** a marcar os dois gols. A vitória histórica garantiu a primeira classificação da Costa do Marfim para a fase eliminatória de uma Copa do Mundo, enquanto Curaçao se despediu do torneio.

## ⚽ Marcadores e Lances Importantes
- **Gols da Costa do Marfim**: Nicolas Pépé (2 gols)
- **Gols de Curaçao**: Nenhum

## 🔑 Momentos Decisivos
- **Nicolas Pépé** abriu o placar no primeiro tempo com uma finalização clínica, mostrando toda a sua experiência.
- No segundo tempo, **Pépé** voltou a marcar, desta vez com um chute de fora da área que não deu hipótese ao goleiro.
- A Costa do Marfim controlou o jogo do início ao fim, dominando a posse de bola e as oportunidades.
- A classificação representou um marco histórico para o futebol marfinense em Copas do Mundo.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260626_tunisia_netherlands",
        "date": "2026-06-25",
        "teams": ["Tunísia", "Holanda"],
        "score": "1-3",
        "group": "F",
        "venue": "Dallas Stadium (Dallas)",
        "summary": """# ⚽ Resumo do Jogo: Tunísia 1 - 3 Holanda
**Data:** 25 de Junho de 2026  
**Estádio:** Kansas City Stadium (Kansas City, MO)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
A **Holanda** venceu a **Tunísia** por **3 a 1** e garantiu a liderança do Grupo F, avançando para o mata-mata onde enfrentará Marrocos. A Tunísia foi eliminada após a fase de grupos.

## ⚽ Marcadores e Lances Importantes
- **Gols da Holanda**: Ellyes Skhiri (3', autogolo), Brian Brobbey (7'), Jan-Paul van Hecke (62')
- **Gols da Tunísia**: Hazem Mastouri (54')

## 🔑 Momentos Decisivos
- Logo aos 3 minutos, um autogolo de **Ellyes Skhiri** abriu o placar para a Holanda.
- **Brian Brobbey** ampliou rapidamente aos 7 minutos, colocando a Holanda em posição confortável.
- No segundo tempo, **Hazem Mastouri** descontou para a Tunísia aos 54 minutos, trazendo esperança.
- **Jan-Paul van Hecke** fechou a conta aos 62 minutos com um cabeceamento certeiro após escanteio, selando a vitória holandesa.
- A Holanda avançou como líder do Grupo F, enquanto a Tunísia se despediu do Mundial.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
    {
        "id": "20260626_japan_sweden",
        "date": "2026-06-25",
        "teams": ["Japão", "Suécia"],
        "score": "1-1",
        "group": "F",
        "venue": "San Francisco Stadium (Santa Clara)",
        "summary": """# ⚽ Resumo do Jogo: Japão 1 - 1 Suécia
**Data:** 25 de Junho de 2026  
**Estádio:** Dallas Stadium (Arlington, TX)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
**Japão** e **Suécia** empataram por **1 a 1** em Arlington, num resultado que classificou ambas as seleções para a fase eliminatória. O Japão terminou como segundo do Grupo F (atrás da Holanda) e enfrentará o Brasil, enquanto a Suécia avançou como uma das melhores terceiras.

## ⚽ Marcadores e Lances Importantes
- **Gols do Japão**: Daizen Maeda (56')
- **Gols da Suécia**: Anthony Elanga (62')

## 🔑 Momentos Decisivos
- O primeiro tempo terminou sem gols, com ambas as equipas a jogar de forma cautelosa.
- **Daizen Maeda** abriu o placar para o Japão aos 56 minutos, com uma finalização rápida dentro da área.
- A Suécia reagiu rapidamente: **Anthony Elanga** empatou apenas 6 minutos depois (62'), com um chute preciso.
- O empate final classificou ambas as seleções — o Japão como vice-líder e a Suécia como terceira colocada.

---
*Atualizado automaticamente via Copa Bot.*
"""
    },
]

# Carregar status.json existente
status_path = os.path.join(BASE_DIR, "status.json")
with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

processed_count = 0
for match in matches_to_process:
    mid = match["id"]
    if mid in status["processed_matches"]:
        print(f"⏭️  Já processado: {mid}")
        continue

    # Salvar resumo .md
    md_path = os.path.join(BASE_DIR, "partidas", f"{mid}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(match["summary"].strip() + "\n")
    print(f"📝 Resumo salvo: {mid}")

    # Atualizar status.json
    status["processed_matches"][mid] = {
        "date": match["date"],
        "teams": match["teams"],
        "score": match["score"],
        "summary_file": f"partidas/{mid}.md"
    }
    processed_count += 1

# Salvar status.json atualizado
from datetime import datetime, timezone
status["last_check"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(status_path, "w", encoding="utf-8") as f:
    json.dump(status, f, indent=2, ensure_ascii=False)

print(f"\n✅ {processed_count} jogos processados!")
print(f"📊 Total de jogos no status.json: {len(status['processed_matches'])}")
print("🔄 Agora execute: python update_helper.py rebuild")
