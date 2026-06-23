import json
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    status_path = os.path.join(base_dir, "status.json")
    partidas_dir = os.path.join(base_dir, "partidas")
    
    # Definir os resumos e os dados oficiais do Google para as partidas de 22/06
    new_match_data = {
        "20260622_argentina_austria": {
            "date": "2026-06-22",
            "teams": ["Argentina", "Áustria"],
            "score": "2-0",
            "venue": "Dallas Stadium (Arlington, TX)",
            "group": "J",
            "summary": """# ⚽ Resumo do Jogo: Argentina 2 - 0 Áustria
**Data:** 22 de Junho de 2026  
**Estádio:** Dallas Stadium (Arlington, TX)  
**Fase:** Fase de Grupos - Grupo J

## 📝 Visão Geral do Jogo
A **Argentina** derrotou a **Áustria** por **2 a 0** em Arlington, confirmando sua classificação para a fase de mata-mata. A noite foi histórica: Lionel Messi marcou os dois gols da partida e se isolou como o **maior artilheiro da história das Copas do Mundo**, superando o recorde de 16 gols do alemão Miroslav Klose.

## ⚽ Marcadores e Lances Importantes
- **Gols da Argentina**: Lionel Messi (38', 90+5')
- **Gols da Áustria**: Nenhum
- **Incidente Importante**: Pênalti perdido por Lionel Messi (9')

## 🔑 Momentos Decisivos
- Logo aos 9 minutos, a Argentina teve um pênalti a seu favor, mas **Lionel Messi** cobrou para fora, adiando a festa da torcida albiceleste.
- A redenção e a história vieram aos 38 minutos, quando **Lionel Messi** abriu o placar com uma finalização cirúrgica no canto inferior após jogada trabalhada por Almada e Medina. Este gol o igualou a Klose.
- O gol do recorde absoluto saiu no final dos acréscimos (90+5'): **Lionel Messi** brigou pela bola na área, se desvencilhou da marcação e estufou a rede, selando seu 18º gol em mundiais.
- A vitória garantiu a vaga da Argentina no mata-mata, somando 6 pontos no Grupo J.

---
*Atualizado automaticamente via Copa Bot.*
"""
        },
        "20260622_algeria_jordan": {
            "date": "2026-06-22",
            "teams": ["Argélia", "Jordânia"],
            "score": "2-1",
            "venue": "San Francisco Stadium (Santa Clara, CA)",
            "group": "J",
            "summary": """# ⚽ Resumo do Jogo: Argélia 2 - 1 Jordânia
**Data:** 22 de Junho de 2026  
**Estádio:** San Francisco Stadium (Santa Clara, CA)  
**Fase:** Fase de Grupos - Grupo J

## 📝 Visão Geral do Jogo
De virada, a **Argélia** derrotou a estreante **Jordânia** por **2 a 1** na Califórnia. A Jordânia deu um susto ao abrir o placar na primeira etapa, mas os argelinos reagiram no segundo tempo e buscaram a virada com gols de Nadhir Benbouali e Amine Gouiri, mantendo vivas as esperanças de classificação e eliminando os jordanianos.

## ⚽ Marcadores e Lances Importantes
- **Gols da Argélia**: Nadhir Benbouali (69'), Amine Gouiri (82')
- **Gols da Jordânia**: Nizar Al-Rashdan (36')

## 🔑 Momentos Decisivos
- A Jordânia surpreendeu aos 36 minutos quando **Nizar Al-Rashdan** apareceu na área para completar e abrir o marcador.
- A Argélia empatou aos 69 minutos com gol de cabeça de **Nadhir Benbouali** após boa jogada aérea.
- A virada salvadora veio aos 82 minutos, com **Amine Gouiri** finalizando forte de chapa para colocar o placar em 2 a 1.
- O resultado confirmou a eliminação matemática da Jordânia na fase de grupos e manteve a Argélia na luta pelas oitavas de final.

---
*Atualizado automaticamente via Copa Bot.*
"""
        }
    }

    # 2. Ler status.json atual
    with open(status_path, "r", encoding="utf-8") as f:
        status = json.load(f)

    # 3. Reescrever os arquivos .md e atualizar status.json
    for mid, info in new_match_data.items():
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
    print("status.json atualizado com as novas partidas concluídas.")

if __name__ == "__main__":
    main()
