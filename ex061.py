termo = int(input('Digita ai o primeiro termo: '))
razao = int(input('Digita ai a razão: '))
cont  = 10
print(termo)
while cont > 1 :
  cont -= 1
  termo += razao
  print(f'{termo}')
