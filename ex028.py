import random

tent = int(input('Tente descobrir que numero  de 0 a 5 pensei... '))
sorteio = random.randint(0,5)
if(tent == sorteio):
  print('Vc escolheu {} e eu {} acertou !'.format(tent,sorteio))

else:
  print('Vc escolheu {} e eu {} errou !'.format(tent,sorteio))  
  
  if(tent -1 == sorteio or tent +1 == sorteio):
    print('Raspou a caneleta')
