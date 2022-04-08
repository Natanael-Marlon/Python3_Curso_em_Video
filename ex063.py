n = int(input('Quantos elementos fibonacci vc quer infeliz?? '))
n1 = 0 
n2 = 1
soma = 0
print(n1,n2, end=' ')
while n >= 3:
  soma = n1 + n2 
  print(soma,end=' ')
  n1 = n2
  n2 = soma
  n -= 1





