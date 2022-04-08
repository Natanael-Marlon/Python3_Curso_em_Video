val   = []
maior = menor = posmai = posmen =0
for cont in range(0 , 5):
  val.append(int(input('Digite um valor: ')))
for c , v in enumerate(val):
  if v >= maior or c == 0:
    maior = v
    posmai = c
  if v <= menor or c == 0:
    menor = v
    posmen = c
    
print(f'o maior e {maior} na pos {posmai + 1} \no menor e {menor} na pos {posmen + 1} ')
  