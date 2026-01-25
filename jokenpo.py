# Pedra Papel e Tesoura
from time import sleep
from random import randint

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
computador = randint(0,2)
escolha_computador = itens[computador]
print(f'{cores["amarelo"]}-=-=-=-=-=-=-=-=-=- PEDRA, PAPEL E TESOURA -=-=-=-=-=-=-=-=-{cores["limpa"]}')
usuario = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA           
'''))

if usuario > 2 or usuario < 0:
    print(f'{cores["vermelho"]}JOGADA INVÁLIDA!{cores["limpa"]}')
    print('Por favor, escolha entre 0, 1 ou 2.')
    print('-=-' * 20)
else:
    escolha_usuário = itens[usuario]
     
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=-' * 20)
    print(f'O computador jogou {escolha_computador}')
    if computador == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif computador == 1:
        print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        
    print(f'O usuário jogou {escolha_usuário}')
    if usuario == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif usuario == 1:
        print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    print('-=-' * 20)

    if computador == 0:
        if usuario == 0:
            print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')
        elif usuario == 1:
            print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')
        elif usuario == 2:
            print(f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')

    elif computador == 1:
        if usuario == 0:
            (f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')
        elif usuario == 1:
            print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')
        elif usuario == 2:
            print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')

    else:
        if usuario == 0:
            print(f'{cores["verde"]}O USUÁRIO GANHOU!{cores["limpa"]}')
        elif usuario == 1:
            (f'{cores["vermelho"]}O COMPUTADOR GANHOU!{cores["limpa"]}')
        elif usuario == 2:
            print(f'{cores["amarelo"]}DEU EMPATE!{cores["limpa"]}')

