import random
nome1   = input('Digite o 1 nome ')
nome2   = input('Digite o 2 nome ')
nome3   = input('Digite o 3 nome ')
nome4   = input('Digite o 4 nome ')
lista   =[nome1,nome2,nome3,nome4]
random.shuffle(lista)
print('e a ordem ficou {}'.format(lista))