soma =  0
for c in range(0, 7):
  nas = int(input('Digite seu ano de nascimento: '))
  if((nas - 2022) < 18):
    soma += c
print(f'{soma} ja atingiram maioridade')