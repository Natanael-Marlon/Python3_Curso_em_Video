soma = 0
num = 0
c = 0
while num != 999:
  num = int(input('Digita ai [999] faz parar'))
  soma += num
  c += 1
print(f'Voce digitou {c-1} vezes e a soma entre eles foi {soma-999}')
