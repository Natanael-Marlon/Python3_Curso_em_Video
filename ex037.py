num = int(input('Diga um numero '))
esc= int(input('Digite o qual  moodo de conversão \n 1 -Binario \n 2 - Octal \n 3 - Hexadecimal \n'))
if(esc == 1):
  print(f'Em Binario deu {bin(num)[2:]}')
elif(esc == 2):
  print(f'Em Octal deu {oct(num)[2:]}')
elif(esc == 3):
  print(f'Em Hexadecimal deu {hex(num)[2:]}')
else:
  print('Você não escolheu um numero de conversão correspondente!! ')

