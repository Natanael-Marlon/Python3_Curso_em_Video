ano = int(input('Diga seu ano de nascimento xoven '))
idade = 2022 - ano
print(idade)
if(idade <= 9):
  print(f'mirin {idade} anos ')
elif(idade <= 14):
  print(f' infantil {idade} anos ')
elif(idade <= 19):
  print(f' junior {idade} anos ')
elif(idade <= 20):
  print(f' Senior {idade} anos ')
elif(idade > 20):
  print(f' Master {idade} anos ')
