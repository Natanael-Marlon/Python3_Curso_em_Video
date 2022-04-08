produtos_preços = 'Carro',50000,'Casa',15000,'Roupa',1000,'Comida',500
for pos , c in enumerate(produtos_preços):
  if pos%2==0:
    print(f'{c} = ',end='')
  else:
    print(f'{c}')
