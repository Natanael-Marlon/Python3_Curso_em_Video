soma = num = c = 0
while num != 999:
  num = int(input('Digita ai [999] faz parar '))
  soma += num
  c += 1
  if(num == 999):
    print(f'Voce digitou {c-1} vezes e a soma {soma-999}  ')
    break
