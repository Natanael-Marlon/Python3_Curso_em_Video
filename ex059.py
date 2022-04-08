n1      = int(input('Digite um valor '))
n2      = int(input('Digite outro valor '))
escolha = int(input('Escolha um dos itens do menu\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5]Sair do programa\n'))
while escolha < 5:
  if(escolha == 1):
    soma = n1 + n2
    print(f'a soma deu {soma}')
  elif(escolha == 2):
    mult = n1 * n2
    print(f'a multiplicação deu {mult}')
  elif(escolha == 3):
    if(n1>n2):
      maior = n1
    else:
      maior = n2
    print(f'{maior} é o maior entre {n1} e {n2}')
  elif(escolha == 4):
    n1 = int(input('Digite um valor '))
    n2 = int(input('Digite outro valor '))
    print(f'O novo valor é {n1} e {n2}')
  else:
    print('Item desconhecido')
  escolha = int(input('Escolha um dos itens do menu\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Numeros\n[5]Sair do programa\n'))
if(escolha == 5):
  print('Saindo do programa...')


