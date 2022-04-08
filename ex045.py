import random
jokenpo = int(input('Vamos Jogar!!!\nEscolha uma opção! \n0 - Pedra\n1 - Papel\n2 - Tesoura\n'))
sorteio =  random.randint(0,2)
if(jokenpo == sorteio):
  if(jokenpo == 0 and sorteio == 0):
    jokenpo = 'Pedra'
    sorteio = 'Pedra'
  elif(jokenpo == 1 and sorteio == 1):
    jokenpo = 'Papel'
    sorteio = 'Papel'
  elif(jokenpo == 2 and sorteio == 2):
    jokenpo = 'Tesoura'
    sorteio = 'Tesoura'
  print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\nDeu empate')

elif(jokenpo != sorteio):
  if(jokenpo == 0 and sorteio == 1):
    jokenpo = 'Pedra'
    sorteio = 'Papel'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Deu Acer')
  elif(jokenpo == 1 and sorteio == 0):
    jokenpo = 'Papel'
    sorteio = 'Pedra'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Você ganhou')
  elif(jokenpo == 0 and sorteio == 2):
    jokenpo = 'Pedra'
    sorteio = 'Tesoura'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Você ganhou')
  elif(jokenpo == 2 and sorteio == 0):
    jokenpo = 'Tesoura'
    sorteio = 'Pedra'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Deu Acer')
  elif(jokenpo == 1 and sorteio == 2):
    jokenpo = 'Papel'
    sorteio = 'Tesoura'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Deu Acer')
  elif(jokenpo == 2 and sorteio == 1):
    jokenpo = 'Tesoura'
    sorteio = 'Papel'
    print(f'Acer nitro 5 escolheu {sorteio}\nVocê escolheu {jokenpo}\n Você ganhou')
else:
  print('Opção invalida')