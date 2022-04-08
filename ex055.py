maior = 0
menor = 0
for pessoas in range(1, 6):
  peso = float(input(f'o peso da {pessoas}° pessoa'))
  if(pessoas == 1):
    maior = peso
    menor = peso
  else:
    if(peso > maior):
      maior = peso
    elif(peso < menor):
      menor = peso
print(f'O maior peso foi {maior:.2f}kg')
print(f'O menor peso foi {menor:.2f}kg')

