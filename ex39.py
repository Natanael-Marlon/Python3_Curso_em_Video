ano = int(input('Diga seu ano de nascimento xoven '))
idade = 2022 - ano

if(idade == 18):
  print( f'É hora de se alistar ja esta com {idade} anos ')
elif(idade < 18):
  n_idade = (18 - idade) * 1
  print( f'Ta quase na hora de se alistar ja esta com {idade} anos faltam apenas {n_idade} anos ')
elif(idade > 18):
  n_idade = (idade - 18)*1
  print( f'Passou da hora se alistar ja esta com {idade} anos e deveria ter se alistado a {n_idade} anos ')
