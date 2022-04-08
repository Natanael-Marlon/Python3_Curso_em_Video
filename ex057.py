sexo = str(input('Digite seu sexo!!! [M/F]')).upper()
while 'M' != sexo and 'F' != sexo:
  print(f'Digite novamente {sexo} e um valor incorreto ')
  sexo = str(input('Digite seu sexo!!! [M/F]')).upper()
print(f'Sexo escolhido {sexo}')
