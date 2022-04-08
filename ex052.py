num       =  int(input('digite um numero '))
divisores = 0
for c in range(1 , num+1):
  if(num%c==0):
    divisores += 1
    print(c)
if(divisores==2):
  print(f'{num} e primo')
else:
  print(f'{num} nao e primo')


