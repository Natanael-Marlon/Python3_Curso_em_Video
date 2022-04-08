termo = int(input('Digita ai o primeiro termo: '))
razao = int(input('Digita ai a razão: '))
print(termo)
for c in range(1 , 10):
  termo += razao
  print(f'{termo}')
