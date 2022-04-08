import random
nome1 = input('Digite o 1 nome ')
nome2 = input('Digite o 2 nome ')
nome3 = input('Digite o 3 nome ')
nome4 = input('Digite o 4 nome ')
sorteio = random.choice([nome1,nome2,nome3,nome4])

print('o nome escolhido foi {} !!'.format(sorteio))