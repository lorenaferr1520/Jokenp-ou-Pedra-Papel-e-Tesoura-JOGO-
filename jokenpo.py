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
computador = randint(0,2) # escolha do computador
escolha_computador = itens[computador]
print(f'{cores["amarelo"]}-=-=-=-=-=-=-=-=-=- PEDRA, PAPEL E TESOURA -=-=-=-=-=-=-=-=-{cores["limpa"]}')
# escolha do usuário com tratamento de erros:
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
linhaamarela()
print(f'''{cores["amarelo"]}Fim do programa 
  __
<(o )___
 ( ._> /
  `---'   quak

    {cores["limpa"]}  ''')
