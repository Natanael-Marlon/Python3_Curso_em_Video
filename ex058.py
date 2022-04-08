import random

tent = int(input('Tente descobrir que numero  de 0 a 10 pensei... '))
sorteio = random.randint(0,10)
cont = 1
if(tent == sorteio):
  print(f'Acertou eu escolhi {tent} e vc {sorteio}')
while tent != sorteio:
  tent = int(input('Tente descobrir que numero  de 0 a 10 pensei... '))
  sorteio = random.randint(0,10)
  print('Errou vai de novo ')
  cont += 1
print(f'Acertou em {cont} tentativas')

