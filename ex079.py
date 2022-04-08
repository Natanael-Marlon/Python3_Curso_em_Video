resp = 's'.upper()
lista = []

while True:
  if resp == 'S':    
    valor_lista = (int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if valor_lista in lista:
      print(f'{valor_lista} já existe não pode ser adicionado')
    else:
      lista.append(valor_lista)
      print(f'{valor_lista} adicionado')
  elif resp == 'N':
    lista.sort()
    print(f' em ordem crescente {lista}')
    break

