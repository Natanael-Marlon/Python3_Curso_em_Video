sal = float(input('Digite seu salario R$ '))

if(sal >= 1250):
  aumento = (sal*0.10) + sal
  print('Aumentou para R${}'.format(aumento))
else:
  aumento = (sal*0.15) + sal
  print('Aumentou para R${}'.format(aumento))


