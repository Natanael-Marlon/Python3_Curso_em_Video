tabu = 0
while True:
  n1 = int(input('Digita ai: '))
  if(n1 < 0):
    print('Saindo...')
    break
  for c in range(1 , 11):
    tabu = c * n1
    print(f'{n1} x {c} = {tabu}') 

