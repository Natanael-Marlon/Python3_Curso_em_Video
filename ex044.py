produto  = float(input('Digite o valor do produto R$ '))
cond_pag = int(input('Escolha qual condição de pagamento \n1 - À vista(dinheiro/cheque) \n2 - À vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais vezes no cartão \n'))
if(cond_pag == 1):
  desconto = produto - (produto * 0.10)
  print(f'Ficou R${desconto:.2f}')
elif(cond_pag == 2):
  desconto = produto - (produto * 0.05)
  print(f'Ficou R${desconto:.2f}')
elif(cond_pag == 3):
  desconto = produto 
  parc = desconto/2
  print(f'Ficou 2x de R${parc:.2f} no total de R${desconto:.2f}')
elif(cond_pag == 4):
  desconto = produto + (produto * 0.20)
  parc = desconto/3
  print(f'Ficou 3x de R${parc:.2f} no total de R${desconto:.2f}')
else:
  print('Opção Invalida! ')