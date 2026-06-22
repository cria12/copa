import json
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    partidas_dir = os.path.join(base_dir, "partidas")
    
    # Definir os resumos e os dados oficiais do Google para as 4 partidas de 21/06
    match_data = {
        "20260621_belgium_iran": {
            "date": "2026-06-21",
            "teams": ["Bélgica", "Irã"],
            "score": "0-0",
            "venue": "Vancouver Stadium (Vancouver)",
            "group": "G",
            "summary": """# ⚽ Resumo do Jogo: Bélgica 0 - 0 Irã
**Data:** 21 de Junho de 2026  
**Estádio:** Vancouver Stadium (Vancouver)  
**Fase:** Fase de Grupos - Grupo G

## 📝 Visão Geral do Jogo
Bélgica e Irã empataram em **0 a 0** em Vancouver. A seleção belga dominou a posse de bola, mas teve enormes dificuldades para furar a defesa iraniana e acabou jogando com 10 homens no final do segundo tempo após a expulsão de Nathan Ngoy. O goleiro iraniano Alireza Beiranvand foi o grande destaque do jogo com defesas cruciais.

## ⚽ Marcadores e Lances Importantes
- **Gols da Bélgica**: Nenhum
- **Gols do Irã**: Nenhum
- **Expulsões**: Nathan Ngoy (67', Bélgica)

## 🔑 Momentos Decisivos
- A Bélgica pressionou no início, mas esbarrou no goleiro **Alireza Beiranvand**, que fez excelentes defesas.
- Aos 67 minutos, o zagueiro belga **Nathan Ngoy** recebeu cartão vermelho direto após cometer falta em Mehdi Taremi, interrompendo uma oportunidade clara de gol.
- Com um jogador a mais, o Irã equilibrou o jogo e teve chances nos contra-ataques, mas não conseguiu marcar.
- O empate de 0 a 0 embolou a classificação no Grupo G da Copa.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260621_spain_saudiarabia": {
            "date": "2026-06-21",
            "teams": ["Espanha", "Arábia Saudita"],
            "score": "4-0",
            "venue": "Seattle Stadium (Seattle)",
            "group": "H",
            "summary": """# ⚽ Resumo do Jogo: Espanha 4 - 0 Arábia Saudita
**Data:** 21 de Junho de 2026  
**Estádio:** Seattle Stadium (Seattle)  
**Fase:** Fase de Grupos - Grupo H

## 📝 Visão Geral do Jogo
A **Espanha** atropelou a **Arábia Saudita** por **4 a 0** em Seattle. Com atuação avassaladora de Lamine Yamal e dois gols relâmpagos de Mikel Oyarzabal na primeira etapa, a seleção espanhola confirmou seu favoritismo e somou 4 pontos no Grupo H.

## ⚽ Marcadores e Lances Importantes
- **Gols da Espanha**: Lamine Yamal (10'), Mikel Oyarzabal (21', 24'), Hassan Al Tambakti (52', gol contra)
- **Gols da Arábia Saudita**: Nenhum

## 🔑 Momentos Decisivos
- Aos 10 minutos, a joia **Lamine Yamal** abriu o placar após jogada individual e finalização colocada.
- **Mikel Oyarzabal** marcou duas vezes seguidas em um intervalo de três minutos (21' e 24'), ampliando para 3 a 0.
- No início do segundo tempo (52'), a Espanha marcou o quarto com um gol contra do defensor saudita **Hassan Al Tambakti**.
- A vitória coloca a Espanha em excelente situação com 4 pontos no Grupo H, enquanto a Arábia Saudita permanece com 1 ponto.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260621_capeverde_uruguay": {
            "date": "2026-06-21",
            "teams": ["Cabo Verde", "Uruguai"],
            "score": "2-2",
            "venue": "Boston Stadium (Boston)",
            "group": "H",
            "summary": """# ⚽ Resumo do Jogo: Cabo Verde 2 - 2 Uruguai
**Data:** 21 de Junho de 2026  
**Estádio:** Boston Stadium (Boston)  
**Fase:** Fase de Grupos - Grupo H

## 📝 Visão Geral do Jogo
Em jogo eletrizante no Boston Stadium, a estreante **Cabo Verde** conquistou um empate heróico por **2 a 2** contra o bicampeão mundial **Uruguai**. Cabo Verde saiu na frente com um golaço de falta de Kevin Pina, o Uruguai virou ainda na primeira etapa, mas Hélio Varela garantiu o empate histórico para a seleção africana no segundo tempo.

## ⚽ Marcadores e Lances Importantes
- **Gols de Cabo Verde**: Kevin Pina (21'), Hélio Varela (61')
- **Gols do Uruguai**: Maximiliano Araújo (44'), Agustín Canobbio (45+5')

## 🔑 Momentos Decisivos
- Aos 21 minutos, **Kevin Pina** abriu o placar para Cabo Verde cobrando falta de 31 metros com enorme categoria, marcando o primeiro gol do país em Copas do Mundo.
- O Uruguai empatou aos 44 minutos com **Maxi Araújo** de cabeça.
- Nos acréscimos da primeira etapa (45+5'), **Agustín Canobbio** marcou de cabeça para colocar a Celeste na frente por 2 a 1.
- Aos 61 minutos, apenas dois minutos após entrar em campo, **Hélio Varela** aproveitou erro defensivo do Uruguai e marcou o gol do empate final de 2 a 2.
- Cabo Verde soma seu segundo ponto na Copa e comemora muito o resultado histórico.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260621_egypt_newzealand": {
            "date": "2026-06-21",
            "teams": ["Egito", "Nova Zelândia"],
            "score": "3-1",
            "venue": "Kansas City Stadium (Kansas City)",
            "group": "G",
            "summary": """# ⚽ Resumo do Jogo: Egito 3 - 1 Nova Zelândia
**Data:** 21 de Junho de 2026  
**Estádio:** Kansas City Stadium (Kansas City)  
**Fase:** Fase de Grupos - Grupo G

## 📝 Visão Geral do Jogo
O **Egito** fez história ao conquistar sua primeira vitória em Copas do Mundo ao vencer a **Nova Zelândia** de virada por **3 a 1** em Kansas City. A Nova Zelândia saiu na frente no primeiro tempo, mas os Faraós reagiram na segunda etapa liderados por Mohamed Salah para sacramentar a vitória.

## ⚽ Marcadores e Lances Importantes
- **Gols do Egito**: Mostafa Zico (58'), Mohamed Salah (67'), Trezeguet (82')
- **Gols da Nova Zelândia**: Finn Surman (15')

## 🔑 Momentos Decisivos
- Aos 15 minutos, **Finn Surman** colocou a Nova Zelândia em vantagem cabeceando forte após cobrança de escanteio.
- O Egito empatou aos 58 minutos com cabeceio de **Mostafa Zico** após cruzamento de Mohamed Hany.
- A virada egípcia veio aos 67 minutos, quando **Mohamed Salah** recebeu na área e bateu cruzado de perna esquerda.
- Aos 82 minutos, **Trezeguet** cabeceou cruzamento de Salah para fechar o placar em 3 a 1.
- A vitória histórica deixa o Egito na liderança do Grupo G com 4 pontos e perto das oitavas.

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

        # Atualizar/sobrescrever status.json
        status["processed_matches"][mid] = {
            "date": info["date"],
            "teams": info["teams"],
            "score": info["score"],
            "summary_file": f"partidas/{mid}.md"
        }
    
    # 4. Salvar status.json
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)
    print("status.json atualizado com as novas partidas concluídas.")

if __name__ == "__main__":
    main()
