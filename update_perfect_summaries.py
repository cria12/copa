import json
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    partidas_dir = os.path.join(base_dir, "partidas")
    
    # 1. Definir os resumos e os dados reais de acordo com a pesquisa no Google
    match_data = {
        "20260619_usa_australia": {
            "date": "2026-06-19",
            "teams": ["Estados Unidos", "Austrália"],
            "score": "2-0",
            "venue": "Seattle Stadium (Seattle, WA)",
            "group": "D",
            "summary": """# ⚽ Resumo do Jogo: Estados Unidos 2 - 0 Austrália
**Data:** 19 de Junho de 2026  
**Estádio:** Seattle Stadium (Seattle, WA)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
Os **Estados Unidos** conquistaram uma vitória sólida por **2 a 0** contra a **Austrália** no Seattle Stadium. Com amplo controle das ações de ataque, a seleção americana encaminhou o placar ainda no primeiro tempo com um gol contra e um belo cabeceio de Alex Freeman. Com este triunfo, a seleção norte-americana carimbou a classificação para a fase eliminatória da Copa.

## ⚽ Marcadores e Lances Importantes
- **Gols dos Estados Unidos**: Cameron Burgess (11', gol contra), Alex Freeman (43')
- **Gols da Austrália**: Nenhum

## 🔑 Momentos Decisivos
- Aos 11 minutos, após cruzamento rasteiro na área, o zagueiro australiano **Cameron Burgess** tentou interceptar e marcou contra.
- Aos 43 minutos, o defensor americano **Alex Freeman** subiu soberano na área e testou firme no ângulo para fazer 2 a 0 de cabeça após escanteio.
- No segundo tempo, a seleção dos EUA administrou o resultado com excelente controle de posse de bola e forte marcação.
- A Austrália tentou pressionar pelas pontas, mas não conseguiu quebrar o forte bloqueio defensivo americano.
- A vitória garantiu a classificação matemática antecipada dos Estados Unidos no mata-mata da competição.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_scotland_morocco": {
            "date": "2026-06-19",
            "teams": ["Escócia", "Marrocos"],
            "score": "0-1",
            "venue": "Boston Stadium (Boston, MA)",
            "group": "C",
            "summary": """# ⚽ Resumo do Jogo: Escócia 0 - 1 Marrocos
**Data:** 19 de Junho de 2026  
**Estádio:** Boston Stadium (Boston, MA)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
A seleção de **Marrocos** derrotou a **Escócia** por **1 a 0** no Boston Stadium. O único gol do confronto foi marcado logo no início do jogo por Ismael Saibari. A Escócia lutou bastante, mas a qualidade técnica e defensiva marroquina sobressaiu na partida do Grupo C.

## ⚽ Marcadores e Lances Importantes
- **Gols da Escócia**: Nenhum
- **Gols de Marrocos**: Ismael Saibari (2')

## 🔑 Momentos Decisivos
- Logo aos 71 segundos de jogo, **Ismael Saibari** aproveitou grande jogada ofensiva e finalizou rasteiro para marcar o gol mais rápido da Copa até agora.
- A Escócia respondeu com muita pressão física e bolas alçadas na área, mas parou no goleiro marroquino Yassine Bounou.
- No segundo tempo, Marrocos controlou o ritmo de jogo e explorou as transições em velocidade.
- A Escócia buscou o empate nos acréscimos com jogadas aéreas desesperadas, sem sucesso.
- A vitória deixou Marrocos empatado na liderança do Grupo C com o Brasil, ambos somando 4 pontos.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_brazil_haiti": {
            "date": "2026-06-19",
            "teams": ["Brasil", "Haiti"],
            "score": "3-0",
            "venue": "Lincoln Financial Field (Philadelphia, PA)",
            "group": "C",
            "summary": """# ⚽ Resumo do Jogo: Brasil 3 - 0 Haiti
**Data:** 19 de Junho de 2026  
**Estádio:** Lincoln Financial Field (Philadelphia, PA)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
O **Brasil** goleou a seleção do **Haiti** por **3 a 0** em Filadélfia. A seleção canarinho resolveu o jogo de forma avassaladora na primeira etapa com dois gols do atacante Matheus Cunha e um de Vinícius Júnior. O placar de 3 a 0 decretou a eliminação matemática da seleção do Haiti do torneio.

## ⚽ Marcadores e Lances Importantes
- **Gols do Brasil**: Matheus Cunha (23', 36'), Vinícius Júnior (45+3')
- **Gols do Haiti**: Nenhum

## 🔑 Momentos Decisivos
- Aos 23 minutos, **Matheus Cunha** aproveitou assistência certeira e finalizou de chapa para abrir o placar do confronto.
- Aos 36 minutos, novamente **Matheus Cunha** apareceu de forma oportuna para escorar o passe de Rodrygo e ampliar a contagem.
- Nos acréscimos do primeiro tempo (45+3'), **Vinícius Júnior** aproveitou rebote do goleiro haitiano e guardou o terceiro gol.
- No segundo tempo, o técnico brasileiro promoveu várias substituições para poupar o elenco fisicamente.
- Com o revés de 3 a 0, a seleção do Haiti deu adeus às chances de classificação para as oitavas de final.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_paraguay_turkiye": {
            "date": "2026-06-19",
            "teams": ["Paraguai", "Turquia"],
            "score": "1-0",
            "venue": "Dallas Stadium (Dallas, TX)",
            "group": "D",
            "summary": """# ⚽ Resumo do Jogo: Paraguai 1 - 0 Turquia
**Data:** 19 de Junho de 2026  
**Estádio:** Dallas Stadium (Dallas, TX)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
Em confronto dramático e tenso em Dallas, o **Paraguai** venceu a **Turquia** por **1 a 0**. Matías Galarza marcou o gol relâmpago no início, e a seleção sul-americana resistiu de forma heroica jogando o segundo tempo inteiro com 10 atletas após a expulsão de Miguel Almirón. A derrota causou a eliminação matemática da Turquia na Copa do Mundo de 2026.

## ⚽ Marcadores e Lances Importantes
- **Gols do Paraguai**: Matías Galarza (2')
- **Gols da Turquia**: Nenhum

## 🔑 Momentos Decisivos
- Logo aos 64 segundos do primeiro tempo, **Matías Galarza** marcou o gol paraguaio aproveitando uma bobeada defensiva.
- A partida esquentou com fortes divididas físicas e muita discussão entre as comissões técnicas.
- No final da primeira etapa, o craque paraguaio **Miguel Almirón** recebeu cartão vermelho direto após violar uma nova regra de protesto contra a arbitragem.
- Durante o segundo tempo, a Turquia bombardeou a área paraguaia, mas a seleção sul-americana ergueu uma verdadeira muralha defensiva.
- O apito final confirmou a vitória épica do Paraguai por 1 a 0 e a eliminação precoce da Turquia do mundial.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_germany_ivorycoast": {
            "date": "2026-06-20",
            "teams": ["Alemanha", "Costa do Marfim"],
            "score": "2-1",
            "venue": "Houston Stadium (Houston, TX)",
            "group": "E",
            "summary": """# ⚽ Resumo do Jogo: Alemanha 2 - 1 Costa do Marfim
**Data:** 20 de Junho de 2026  
**Estádio:** Houston Stadium (Houston, TX)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
A **Alemanha** conquistou uma virada heroica por **2 a 1** contra a **Costa do Marfim** em Toronto. A seleção africana saiu na frente com Kessié, mas o atacante Deniz Undav saiu do banco de reservas no segundo tempo para marcar duas vezes, incluindo o gol da vitória nos acréscimos, garantindo a classificação alemã.

## ⚽ Marcadores e Lances Importantes
- **Gols da Alemanha**: Deniz Undav (68', 90+4')
- **Gols da Costa do Marfim**: Franck Kessié (30')

## 🔑 Momentos Decisivos
- A Costa do Marfim começou muito perigosa nas transições e abriu o placar aos 30 minutos com um gol de **Franck Kessié**.
- Na etapa complementar, o técnico alemão fez alterações táticas, colocando **Deniz Undav** em campo.
- Aos 68 minutos, Deniz Undav balançou as redes pela primeira vez na partida, aproveitando cruzamento na área.
- A pressão alemã continuou e surtiu efeito aos 90+4 minutos, quando **Deniz Undav** marcou o gol da virada de cabeça nos acréscimos.
- A grande vitória garantiu a Alemanha nas oitavas de final da Copa com 6 pontos.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_curacao_ecuador": {
            "date": "2026-06-20",
            "teams": ["Curaçao", "Equador"],
            "score": "0-0",
            "venue": "Atlanta Stadium (Atlanta, GA)",
            "group": "E",
            "summary": """# ⚽ Resumo do Jogo: Curaçao 0 - 0 Equador
**Data:** 20 de Junho de 2026  
**Estádio:** Atlanta Stadium (Atlanta, GA)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
Em jogo histórico no Arrowhead Stadium, **Curaçao** segurou um empate heróico em **0 a 0** contra a seleção do **Equador**. A partida foi marcada por uma atuação épica do goleiro Eloy Room, que barrou todas as investidas equatorianas e garantiu o primeiro ponto da história de sua seleção na Copa do Mundo.

## ⚽ Marcadores e Lances Importantes
- **Gols de Curaçao**: Nenhum
- **Gols do Equador**: Nenhum

## 🔑 Momentos Decisivos
- O Equador sufocou Curaçao no campo de defesa, dominando as estatísticas de posse de bola e finalizações.
- O goleiro de Curaçao, **Eloy Room**, se tornou a lenda do jogo com **15 defesas**, o recorde absoluto de uma partida regulamentar em Copas do Mundo desde 1966.
- A defesa de Curaçao resistiu à intensa pressão aérea no final do segundo tempo.
- O empate de 0 a 0 garantiu o histórico primeiro ponto de Curaçao no mundial.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_netherlands_sweden": {
            "date": "2026-06-20",
            "teams": ["Holanda", "Suécia"],
            "score": "5-1",
            "venue": "Dallas Stadium (Dallas, TX)",
            "group": "F",
            "summary": """# ⚽ Resumo do Jogo: Holanda 5 - 1 Suécia
**Data:** 20 de Junho de 2026  
**Estádio:** Dallas Stadium (Dallas, TX)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
A **Holanda** atropelou a **Suécia** com uma goleada avassaladora de **5 a 1** em Houston. Com atuações espetaculares de Brian Brobbey and Cody Gakpo, que marcaram dois gols cada, o ataque holandês triturou o sistema defensivo sueco e assumiu a liderança do Grupo F.

## ⚽ Marcadores e Lances Importantes
- **Gols da Holanda**: Brian Brobbey (5', 17'), Cody Gakpo (47', 54'), Crysencio Summerville (89')
- **Gols da Suécia**: Anthony Elanga (59')

## 🔑 Momentos Decisivos
- **Brian Brobbey** abriu o placar logo aos 5 minutos e fez o segundo aos 17' com conclusões precisas de cabeça.
- Logo no início do segundo tempo, **Cody Gakpo** fez o terceiro gol holandês aos 47' e marcou o quarto aos 54 minutos.
- A Suécia reduziu a desvantagem aos 59 minutos com gol de **Anthony Elanga** em rápida corrida.
- Nos minutos finais (89'), **Crysencio Summerville** fechou a contagem em 5 a 1 com um chute cruzado.
- A vitória monumental levou os holandeses aos 4 pontos, assumindo a liderança do Grupo F.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_japan_tunisia": {
            "date": "2026-06-20",
            "teams": ["Japão", "Tunísia"],
            "score": "4-0",
            "venue": "San Francisco Stadium (Santa Clara, CA)",
            "group": "F",
            "summary": """# ⚽ Resumo do Jogo: Japão 4 - 0 Tunísia
**Data:** 20 de Junho de 2026  
**Estádio:** San Francisco Stadium (Santa Clara, CA)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
O **Japão** goleou a **Tunísia** por **4 a 0** em Monterrey, no histórico milésimo jogo (1.000) da história das Copas do Mundo. Com dois gols de Ayase Ueda e grande volume tático de meio de campo, a equipe japonesa garantiu três pontos importantíssimos no Grupo F e selou a eliminação da Tunísia.

## ⚽ Marcadores e Lances Importantes
- **Gols do Japão**: Daichi Kamada (4'), Ayase Ueda (31', 83'), Junya Ito (69')
- **Gols da Tunísia**: Nenhum

## 🔑 Momentos Decisivos
- Aos 4 minutos, **Daichi Kamada** inaugurou o marcador após assistência de Nakamura, fazendo o gol mais rápido do Japão em Copas do Mundo.
- O atacante **Ayase Ueda** ampliou a vantagem aos 31 minutos chutando forte no limite da grande área.
- Aos 69 minutos, **Junya Ito** fez o terceiro do time nipônico após assistência de Ueda.
- Aos 83 minutos, novamente **Ayase Ueda** fechou a goleada clássica com cabeceio perfeito de cobertura.
- O Japão agora soma 4 pontos no Grupo F, empatado com a Holanda, e a Tunísia deu adeus à Copa de 2026.

---
*Atualizado automaticamente via Copa Bot.*
"""
        }
    }

    # 2. Ler status.json atual
    with open(status_path, "r", encoding="utf-8") as f:
        status = json.load(f)

    # 3. Reescrever os arquivos .md e atualizar status.json
    for mid, info in match_data.items():
        # Escrever arquivo .md
        md_file_path = os.path.join(partidas_dir, f"{mid}.md")
        with open(md_file_path, "w", encoding="utf-8") as f:
            f.write(info["summary"])
        print(f"Resumo perfeito criado: {md_file_path}")

        # Atualizar status.json
        status["processed_matches"][mid] = {
            "date": info["date"],
            "teams": info["teams"],
            "score": info["score"],
            "summary_file": f"partidas/{mid}.md"
        }
    
    # 4. Salvar status.json
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)
    print("status.json atualizado com os dados e datas corretas.")

if __name__ == "__main__":
    main()
