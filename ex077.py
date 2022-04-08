palavra = 'Carne'.upper(),'Sarna'.upper(),'Sarrar'.upper(),'Sorte'.upper(),'Peido'.upper()
vogais = 'A', 'E', 'I', 'O', 'U'

for pos , c in enumerate(palavra):
  print(f'{c} vogais são: ', end='')
  for d in range(0,len(c)):
    if c[d] in vogais:
      print(f'{c[d]}',end='')
  print('')


