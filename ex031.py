distancia = float(input('Diga quantos Kms tem sua viagem...'))
if(distancia <= 200):
  preco = distancia * 0.5
  print('ficou R${:.2f} bora viajar!!!'.format(preco))
else:
  preco = distancia * 0.45
  print('ficou R${:.2f} bora viajar!!!'.format(preco))
