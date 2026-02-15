# Jokenp-ou-Pedra-Papel-e-Tesoura-JOGO-
Oi! Este é o meu primeiro projeto de jogo interativo. Fiz ele durante o curso de Python para colocar em prática o que aprendi sobre condições e bibliotecas. 🪨📄✂️

🚀 funcionamento do jogo:
    - configuração: o usuario define a quantidade de rodadas (melhor de X)
    - segunda entrada: escolha entre pedra (0), papel (1) ou tesoura (2)
        -> tratamento de erro: O sistema valida entradas para impedir letras ou números fora do intervalo.
    - IA do computador: descisão gerada via randint (módulo random)
    - processamento de regras: utiliza estruturas condicionais (if/elif/else)
    - placar final: contabilização automática de vitórias do usuário, do  computador e empates

💡 detalhes:
    - Lógica de Jogo: if, elif e else para decidir quem ganha.
    - Sorteio: biblioteca random para o computador escolher a jogada.
    - Animação:time.sleep para dar um tempo entre o "JO... KEN... PO!".
    - Cores no Terminal: dicionário de cores para deixar o resultado mais    fácil de ler (Verde para vitória e Vermelho para derrota).

🎨 Arte ASCII para cada jogada, assim o terminal fica mais visual e divertido de jogar. Também tratei o erro de quando o usuário digita um número que não existe, para o programa não travar.

PEDRA                PAPEL               TESOURA
    _______             _______             _______
---'   ____)        ---'    ____)____   ---'   ____)____
      (_____)                  ______)            ______)
      (_____)                 _______)         __________)
      (____)                 _______)         (____)
---.__(___)         ---.__________)     ---.__(___)

💾 atualizações:
    02/2026:
        adição de funções para as ASCII
        tratamento de erros no input do usuário
        pato
        def de resultados
        adição de melhor de quantas com repetição while e contadores