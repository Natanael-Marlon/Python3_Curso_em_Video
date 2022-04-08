lista = []

for c in range(0, 5):
  val = int(input('Digite um valor: '))
  # print(lista,c,'!!!!!!')
  if c == 0 or val > lista[-1]:
    lista.append(val)
    # print(lista,val,'@@@@@@')
  else:
    pos = 0
    while pos < len(lista):
      if val <= lista[pos]:
        lista.insert(pos , val)
        # print(lista,val,pos,'########')
        break
      pos += 1
print(f'Em ordem fica {lista}')



