from random import randint
from operator import itemgetter
from time import sleep

print('=' * 40)
print(f'{"Game de sorteamento":^40}')
print('=' * 40)

quant = int(input('Quantidade de players: '))

jogadores = {} # or dict()

for j in range(0, quant):
	jogadores['Jogador' + str(j + 1)] = randint(1, 6)

print('-' * 40)
print('Valores sorteado: ')

for key, value in jogadores.items():
	print(f'	-  {key} tirou {value} no dado.')

print('-' * 40)

print('	-  Ranking:')

# Vai organiza os valores do dicionario
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for p, j in enumerate(ordem):
	print(f'	-  {p + 1}* Lugar: {j[0]} com {j[1]}')

print('-' * 40)

