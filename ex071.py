print('CAIXA ELETRÔNICO SIMULATOR!!!\nCédulas disponiveis:\nR$ 50\nR$ 20\nR$ 10\nR$ 1')
while True:
  saque = int(input('Quanto de Saque?? '))
  if saque <= 0:
    break
  nota_50 = saque//50
  saque   = (saque - (50*nota_50))
  nota_20 = saque//20
  saque   = (saque - (20*nota_20))
  nota_10 = saque//10
  saque   = (saque - (10*nota_10))
  nota_01 = saque//1
  saque   = (saque - (nota_01))
  print(f'Saque de {saque} tem:\n{nota_50} notas de R$ 50\n{nota_20} notas de R$ 20\n{nota_10} notas de R$ 10\n{nota_01} notas de R$ 1')
