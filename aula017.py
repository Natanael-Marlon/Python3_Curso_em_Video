val = []
val.append(5)
val.append(9)
val.append(4)
for cont in range(0 , 5):
  val.append(int(input('Digite um valor: ')))


for c ,v in enumerate(val):
  print(f'{c} {v} ')