n1 = float(input('Digite sua  primeira nota '))
n2 = float(input('Digite sua  segunda nota '))
media = (n1+n2)/2
print(media)

if(media < 5):
  print('Reprovado! ')
elif(media <= 6.9):
  print('Recuperação! ')
elif(media >= 7):
  print('Aprovado!')


