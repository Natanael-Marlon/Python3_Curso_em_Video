reta_1 = int(input('Digite o tamanho da primeira reta '))
reta_2 = int(input('Digite o tamanho da segunda reta '))
reta_3 = int(input('Digite o tamanho da terceira reta '))

if((reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_3 + reta_2) > reta_1):
  print(' \033[0;32m é um triangulo \033[m')
else:
  print('\033[0;31m não é triangulo \033[m')
