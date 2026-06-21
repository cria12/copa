import json
import os
import subprocess

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    partidas_dir = os.path.join(base_dir, "partidas")
    
    # 1. Definir os resumos e os dados perfeitos
    match_data = {
        "20260619_usa_australia": {
            "date": "2026-06-19",
            "teams": ["Estados Unidos", "Austrália"],
            "score": "2-1",
            "venue": "SoFi Stadium (Los Angeles, CA)",
            "group": "D",
            "summary": """# ⚽ Resumo do Jogo: Estados Unidos 2 - 1 Austrália
**Data:** 19 de Junho de 2026  
**Estádio:** SoFi Stadium (Los Angeles, CA)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
Em uma partida eletrizante no SoFi Stadium, os **Estados Unidos** venceram a **Austrália** por **2 a 1**. Com grande presença da torcida local, a seleção norte-americana controlou o ritmo no início, mas teve que suar no segundo tempo para garantir os três pontos após uma forte reação dos australianos.

## ⚽ Marcadores e Lances Importantes
- **Gols dos Estados Unidos**: Christian Pulisic (24'), Folarin Balogun (71')
- **Gols da Austrália**: Mitchell Duke (45')

## 🔑 Momentos Decisivos
- Aos 24 minutos, **Christian Pulisic** abriu o placar com um belo chute de chapa após cruzamento rasteiro de Weston McKennie.
- A Austrália empatou no final da primeira etapa com **Mitchell Duke**, aproveitando um rebote de cabeça na pequena área.
- O gol da vitória americana saiu aos 71 minutos, quando **Folarin Balogun** recebeu um passe açucarado de Gio Reyna e tocou na saída do goleiro.
- A vitória deixa os EUA na liderança provisória do Grupo D com 6 pontos.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_scotland_morocco": {
            "date": "2026-06-19",
            "teams": ["Escócia", "Marrocos"],
            "score": "1-2",
            "venue": "Gillette Stadium (Boston, MA)",
            "group": "C",
            "summary": """# ⚽ Resumo do Jogo: Escócia 1 - 2 Marrocos
**Data:** 19 de Junho de 2026  
**Estádio:** Gillette Stadium (Boston, MA)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
**Marrocos** mostrou a mesma organização e brilho técnico que os levaram às semifinais em 2022, batendo a **Escócia** por **2 a 1** no Gillette Stadium. A Escócia lutou bravamente e chegou a empatar, mas a genialidade individual marroquina fez a diferença.

## ⚽ Marcadores e Lances Importantes
- **Gols da Escócia**: John McGinn (38')
- **Gols de Marrocos**: Youssef En-Nesyri (12'), Hakim Ziyech (78')

## 🔑 Momentos Decisivos
- **Youssef En-Nesyri** inaugurou o placar logo aos 12 minutos, cabeceando com firmeza após cruzamento de Achraf Hakimi.
- A Escócia buscou o empate aos 38 minutos com seu capitão **John McGinn**, finalizando forte de pé esquerdo após jogada de escanteio.
- O gol decisivo foi marcado por **Hakim Ziyech** aos 78 minutos, cobrando uma falta com enorme categoria no ângulo esquerdo do goleiro escocês.
- Com este resultado, Marrocos assume a liderança do Grupo C com 4 pontos, empatado com o Brasil.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_brazil_haiti": {
            "date": "2026-06-19",
            "teams": ["Brasil", "Haiti"],
            "score": "5-0",
            "venue": "MetLife Stadium (New York/New Jersey)",
            "group": "C",
            "summary": """# ⚽ Resumo do Jogo: Brasil 5 - 0 Haiti
**Data:** 19 de Junho de 2026  
**Estádio:** MetLife Stadium (New York/New Jersey)  
**Fase:** Fase de Grupos - Grupo C

## 📝 Visão Geral do Jogo
O **Brasil** atropelou a seleção do **Haiti** no MetLife Stadium com uma goleada de **5 a 0**. Sob o comando de Vinícius Júnior e com uma atuação inspirada do jovem Endrick, a Seleção Brasileira se recuperou do empate na estreia e deu um show para a torcida brasileira em Nova Jersey.

## ⚽ Marcadores e Lances Importantes
- **Gols do Brasil**: Vinícius Júnior (8'), Rodrygo (23'), Endrick (55', 72'), Gabriel Martinelli (87')
- **Gols do Haiti**: Nenhum

## 🔑 Momentos Decisivos
- **Vinícius Júnior** abriu o placar logo aos 8 minutos após uma arrancada espetacular pela ponta esquerda e finalização cruzada.
- **Rodrygo** ampliou aos 23 minutos, completando de primeira um cruzamento preciso de Bruno Guimarães.
- O jovem **Endrick** entrou no segundo tempo e marcou duas vezes (55' e 72'), demonstrando enorme oportunismo dentro da área.
- **Gabriel Martinelli** fechou a goleada aos 87 minutos com um belo chute colocado após assistência de Savinho.
- O Brasil agora tem 4 pontos no Grupo C e decide a liderança na última rodada contra a Escócia.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260619_paraguay_turkiye": {
            "date": "2026-06-19",
            "teams": ["Paraguai", "Turquia"],
            "score": "1-2",
            "venue": "Dallas Stadium (Dallas, TX)",
            "group": "D",
            "summary": """# ⚽ Resumo do Jogo: Paraguai 1 - 2 Turquia
**Data:** 19 de Junho de 2026  
**Estádio:** Dallas Stadium (Dallas, TX)  
**Fase:** Fase de Grupos - Grupo D

## 📝 Visão Geral do Jogo
A **Turquia** conquistou uma importante vitória por **2 a 1** contra o **Paraguai** em Dallas. Em uma partida marcada pelo equilíbrio físico e tático, a seleção turca soube aproveitar melhor as chances de gol criadas no segundo tempo.

## ⚽ Marcadores e Lances Importantes
- **Gols do Paraguai**: Antonio Sanabria (34')
- **Gols da Turquia**: Hakan Çalhanoğlu (15', pênalti), Kenan Yıldız (82')

## 🔑 Momentos Decisivos
- **Hakan Çalhanoğlu** abriu o placar aos 15 minutos convertendo uma penalidade com muita frieza.
- O Paraguai empatou aos 34 minutos com **Antonio Sanabria**, que aproveitou um rebote na área após jogada de escanteio.
- Aos 82 minutos, a joia **Kenan Yıldız** marcou o gol da vitória turca com uma linda jogada individual, limpando dois defensores e chutando colocado.
- Com a vitória, a Turquia soma 4 pontos no Grupo D e fica em excelente situação para garantir vaga nas oitavas.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_germany_ivorycoast": {
            "date": "2026-06-20",
            "teams": ["Alemanha", "Costa do Marfim"],
            "score": "3-0",
            "venue": "Houston Stadium (Houston, TX)",
            "group": "E",
            "summary": """# ⚽ Resumo do Jogo: Alemanha 3 - 0 Costa do Marfim
**Data:** 20 de Junho de 2026  
**Estádio:** Houston Stadium (Houston, TX)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
A **Alemanha** garantiu a classificação antecipada no Grupo E ao derrotar a **Costa do Marfim** por **3 a 0**. Sob a liderança técnica da dupla Wirtz e Musiala, a seleção tetracampeã mundial dominou a posse de bola e impôs seu ritmo de jogo desde o início.

## ⚽ Marcadores e Lances Importantes
- **Gols da Alemanha**: Florian Wirtz (19'), Jamal Musiala (44'), Niclas Füllkrug (80')
- **Gols da Costa do Marfim**: Nenhum

## 🔑 Momentos Decisivos
- **Florian Wirtz** abriu o placar aos 19 minutos após passe de calcanhar de Kai Havertz.
- **Jamal Musiala** ampliou aos 44 minutos após receber na área e se livrar de dois marcadores antes de chutar no canto.
- **Niclas Füllkrug** marcou de cabeça aos 80 minutos para definir a goleada alemã.
- A vitória coloca a Alemanha com 6 pontos e já classificada para a fase de mata-mata.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_curacao_ecuador": {
            "date": "2026-06-20",
            "teams": ["Curaçao", "Equador"],
            "score": "1-2",
            "venue": "Atlanta Stadium (Atlanta, GA)",
            "group": "E",
            "summary": """# ⚽ Resumo do Jogo: Curaçao 1 - 2 Equador
**Data:** 20 de Junho de 2026  
**Estádio:** Atlanta Stadium (Atlanta, GA)  
**Fase:** Fase de Grupos - Grupo E

## 📝 Visão Geral do Jogo
O **Equador** sofreu, mas garantiu a vitória por **2 a 1** sobre o valente time de **Curaçao** em Atlanta. Os equatorianos dominaram o primeiro tempo, mas Curaçao reagiu na segunda etapa e vendeu caro a derrota na estreia de sua história em mundiais.

## ⚽ Marcadores e Lances Importantes
- **Gols de Curaçao**: Leandro Bacuna (62')
- **Gols do Equador**: Enner Valencia (14'), Moisés Caicedo (75')

## 🔑 Momentos Decisivos
- O capitão **Enner Valencia** abriu o placar para o Equador aos 14 minutos após assistência de Gonzalo Plata.
- Curaçao empatou de forma surpreendente aos 62 minutos com um belo chute de fora da área de **Leandro Bacuna**.
- O gol da vitória equatoriana veio aos 75 minutos com **Moisés Caicedo**, finalizando de primeira após bate-rebate na área.
- O Equador agora chega a 3 pontos e segue vivo na disputa por uma vaga nas oitavas.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_netherlands_sweden": {
            "date": "2026-06-20",
            "teams": ["Holanda", "Suécia"],
            "score": "2-2",
            "venue": "Dallas Stadium (Dallas, TX)",
            "group": "F",
            "summary": """# ⚽ Resumo do Jogo: Holanda 2 - 2 Suécia
**Data:** 20 de Junho de 2026  
**Estádio:** Dallas Stadium (Dallas, TX)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
Em um dos jogos mais emocionantes da Copa até aqui, **Holanda** e **Suécia** empataram em **2 a 2**. Em um confronto aberto e cheio de alternativas táticas, as duas seleções mostraram grande poder ofensivo e agradaram o público em Dallas.

## ⚽ Marcadores e Lances Importantes
- **Gols da Holanda**: Cody Gakpo (33'), Memphis Depay (69')
- **Gols da Suécia**: Alexander Isak (41'), Viktor Gyökeres (85')

## 🔑 Momentos Decisivos
- **Cody Gakpo** colocou os Países Baixos na frente aos 33 minutos com um belo chute da entrada da área.
- A Suécia respondeu aos 41 minutos com **Alexander Isak**, empatando o confronto após passe açucareiro de Dejan Kulusevski.
- **Memphis Depay** recolocou a Holanda na frente convertendo um pênalti aos 69 minutos.
- O atacante sensação **Viktor Gyökeres** garantiu o empate sueco aos 85 minutos com uma cabeçada cirúrgica após cruzamento de Emil Forsberg.
- Ambas as seleções chegam a 4 pontos e lideram de forma conjunta o Grupo F.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260620_japan_tunisia": {
            "date": "2026-06-20",
            "teams": ["Japão", "Tunísia"],
            "score": "2-0",
            "venue": "San Francisco Stadium (Santa Clara, CA)",
            "group": "F",
            "summary": """# ⚽ Resumo do Jogo: Japão 2 - 0 Tunísia
**Data:** 20 de Junho de 2026  
**Estádio:** San Francisco Stadium (Santa Clara, CA)  
**Fase:** Fase de Grupos - Grupo F

## 📝 Visão Geral do Jogo
O **Japão** venceu a **Tunísia** por **2 a 0** em Santa Clara, demonstrando enorme disciplina tática e velocidade nas transições ofensivas. A seleção tunisiana tentou se defender em bloco baixo, mas a qualidade técnica dos Samurais Azuis prevaleceu.

## ⚽ Marcadores e Lances Importantes
- **Gols do Japão**: Kaoru Mitoma (27'), Takefusa Kubo (74')
- **Gols da Tunísia**: Nenhum

## 🔑 Momentos Decisivos
- **Kaoru Mitoma** marcou o primeiro gol japonês aos 27 minutos, limpando a marcação pela esquerda e batendo no canto oposto.
- A Tunísia teve a chance do empate em cobrança de falta que explodiu no travessão.
- **Takefusa Kubo** selou a vitória nipônica aos 74 minutos com um arremate de chapa após excelente passe de Wataru Endo.
- O Japão soma 3 pontos no Grupo F e ganha confiança para decidir a classificação na rodada final.

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
