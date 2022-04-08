termo = int(input('Digita ai o primeiro termo: '))
razao = int(input('Digita ai a razão: '))
cont  = 10
esc = ''
print(termo)
if(esc == ''):
  while cont > 1 :
    cont -= 1
    termo += razao
    print(f'{termo}')
  esc = str(input('Gostaria de outro termo?? [S/N] ')).upper()
  while( 'S' == esc):
    termo = int(input('Digita ai o primeiro termo: '))
    razao = int(input('Digita ai a razão: '))
    cont  = 10
    while cont > 1 :
      cont -= 1
      termo += razao
      print(f'{termo}')
    esc = str(input('Gostaria de outro termo?? [S/N] ')).upper()
  print('Saindo do programa')
