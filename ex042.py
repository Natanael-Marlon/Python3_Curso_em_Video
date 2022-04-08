reta_1 = int(input('Digite o tamanho da primeira reta '))
reta_2 = int(input('Digite o tamanho da segunda reta '))
reta_3 = int(input('Digite o tamanho da terceira reta '))

if((reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_3 + reta_2) > reta_1):
  print('é um trinagulo')
  if(reta_1 == reta_2 and reta_1 == reta_3 and reta_2 == reta_3):
    print('triangulo equilatero')
  elif((reta_1 == reta_2 != reta_3) or (reta_1 == reta_3 != reta_2) or (reta_2 == reta_3 != reta_1)):
    print('triangulo isoceles')
  else:
    print('triangulo escaleno')
else:
  print(' não é triangulo ')

