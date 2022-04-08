maior_idadeh = 0
nome_velhoh  = ''
mulher_qtd = 0
soma_idade   = 0

for pessoa in range(1, 5):
  print(f'{pessoa}° pessoa')
  nome  = str(input('Digite o nome: ')).strip()
  idade = int(input('Digite a idade'))
  sexo  = str(input('Digite o sexo [M/F]')).strip()
  soma_idade += idade
  if(pessoa == 1 and sexo == 'M' and 'm'):
    maior_idadeh = idade
    nome_velhoh  = nome
  if(sexo == 'M' and 'm'and idade > maior_idadeh):
    maior_idadeh = idade
    nome_velhoh  = nome  
  if(sexo == 'F' and 'f' and idade < 20):
    mulher_qtd += 1 
media = soma_idade / 4
print(f'A media de idade do grupo e {media}')
print(f'O homem mais velho tem {maior_idadeh} anos e se chama{nome_velhoh}')
print(f'Tem {mulher_qtd} mulheres com menos de 20 anos')
  
