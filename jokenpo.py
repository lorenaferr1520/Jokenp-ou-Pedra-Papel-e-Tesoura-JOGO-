# Pedra Papel e Tesoura
from time import sleep
from random import randint
# def das ASCII
def pedra():
            print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
def papel():
            print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
def tesoura():
            print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
# variaveis de repetições
repetições = int()
vitoriasuser = 0
vitoriascomputador = 0
totalempates = 0
count = 1
#def resultados
def empate():
    print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')
def computadorganha():
    print(f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')

def usuarioganha():
    print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')   
# def linha
def linhaamarela():
    print(f'{cores["amarelo"]}-=-{cores["limpa"]}' * 20)
# biblioteca de cores
cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[1;31m', # Negrito + Vermelho
    'verde': '\033[1;32m',    # Negrito + Verde
    'amarelo': '\033[1;33m',   # Negrito + Amarelo
    'azul': '\033[1;34m',      # Negrito + Azul
    'roxo': '\033[1;35m',      # Negrito + Roxo
    'ciano': '\033[1;36m',     # Negrito + Ciano
    'cinza': '\033[37m',
    'sublinhado': '\033[4m'
}

itens = ('Pedra', 'Papel', 'Tesoura')
print(f'{cores["amarelo"]}-=-=-=-=-=-=-=-=-=- PEDRA, PAPEL E TESOURA -=-=-=-=-=-=-=-=-{cores["limpa"]}')
# escolha do usuário com tratamento de erros:

while True:
    try:
        repetições = int(input("melhor de quantas: "))
    except ValueError:
        print("apenas números!")
    else:
        break

while count <= repetições:
    while True:
        try:
            usuario = int(input('''Suas opções:
            [0] PEDRA
            [1] PAPEL
            [2] TESOURA
            Qual é a sua jogada? '''))
            
            # O IF deve estar dentro do TRY para filtrar o número logo após a digitação
            if 0 <= usuario <= 2:
                break  # Único lugar onde o código tem permissão de sair do loop
            else:
                print(f'{cores["vermelho"]}JOGADA INVÁLIDA!{cores["limpa"]}')
                print('Por favor, escolha entre 0, 1 ou 2.')

        except ValueError:
            print(f'{cores["vermelho"]}JOGADA INVÁLIDA!{cores["limpa"]}')
            print('Por favor, digite um número inteiro.')

    computador = randint(0,2) # escolha do computador
    escolha_computador = itens[computador]
    escolha_usuário = itens[usuario]
        
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    linhaamarela()
    print(f'O computador jogou {escolha_computador}')
    if computador == 0:
        pedra()
    elif computador == 1:
        papel()
    else:
        tesoura()
            
    print(f'O usuário jogou {escolha_usuário}')
    if usuario == 0:
        pedra()
    elif usuario == 1:
        papel()
    else:
        tesoura()
    linhaamarela()

    # comparação de escolhas usuário e computador e definição da vitória
    if computador == 0:
        if usuario == 0:
            empate()
            totalempates += 1
        elif usuario == 1:
            usuarioganha()
            vitoriasuser += 1
        elif usuario == 2:
            computadorganha()
            vitoriascomputador += 1

    elif computador == 1:
        if usuario == 0:
            computadorganha()
            vitoriascomputador += 1
        elif usuario == 1:
            empate()
            totalempates += 1
        elif usuario == 2:
            usuarioganha()
            vitoriasuser += 1

    else:
        if usuario == 0:
            usuarioganha()
            vitoriasuser += 1
        elif usuario == 1:
            computadorganha()
            vitoriascomputador += 1
        elif usuario == 2:
            empate()
            totalempates += 1
    count += 1
# mostra os resultados gerais
linhaamarela()
print(f"{cores['sublinhado']}resultado final:{cores['limpa']}")
print(f'Usuário ganhou {vitoriasuser}')
print(f'Computador ganhou {vitoriascomputador}')
if totalempates > 0:
    print(f'Ouve um total de {totalempates} empates!')

# mostra quem ganhou de todas as partidas
linhaamarela()
if vitoriasuser > vitoriascomputador:
    print(f'{cores["verde"]} Vitória  do usuario no melhor de {repetições}! {cores["limpa"]}')
elif vitoriasuser == vitoriascomputador:
    print(f'{cores["amarelo"]} Empate entre usuário e computador no melhor de {repetições}! {cores["limpa"]}')
else:
    print(f'{cores["vermelho"]} Vitória  do computador no melhor de {repetições}! {cores["limpa"]}')

linhaamarela()
print(f'''{cores["amarelo"]}Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

    {cores["limpa"]}  ''')
