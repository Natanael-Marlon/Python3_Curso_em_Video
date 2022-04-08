resp = 'S'
soma = 0
tot  = 0
maior = 0
menor = 0
media = 0
while resp == 'S' and 's':
  num = int(input('Digita um numero ai '))
  soma += num
  tot += 1
  if(tot == 1):
    maior = menor = num
  else:
    if(num > maior):
      maior = num
    elif(num < menor):
      menor = num
  resp = str(input('Vai continuar?? [S/N]')).upper().strip()[0]
media = soma / tot
print(f'Voce fez {tot} vezes e a media foi {media}\nO maior valor foi {maior} e o menor foi {menor} ')



