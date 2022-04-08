num = int(input('Digite um numero e descubra seu fatorial '))
fat = 1
while num >= 1 :
  if(num == 1):
    print(f'{num} =',end='') 
  else:
    print(f'{num} x ',end='')
    fat = num * fat
  num -= 1 
print(f' {fat} ',end='')


