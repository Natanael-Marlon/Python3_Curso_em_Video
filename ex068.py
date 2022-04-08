import random
vit = num =0
usu = str(input('Par ou Impar... ')).upper()
if usu == 'PAR': 
  while usu != '':
    num = int(input('Digite um numero de 1 a 10: '))
    sor = random.randint(0,10)
    som = num + sor
    vit += 1 
    tot = som%2==0
    print(num, sor)
    if usu == 'PAR' and tot == True :
      print(f'Ganhou!\nDeu par vc {num} pc {sor} total {som} com {vit} vitorias consecutivas')
      usu = str(input('Par ou Impar... ')).upper()
    elif usu == 'IMPAR' and tot == True :
      tot = som%2==1
      usu = 'IMPAR'
      print(f'Perdeu!!!\nDeu par vc {num} pc {sor} total {som} com {vit-1} vitorias consecutivas')
      break
    else:
      tot = som%2==1
      usu = 'IMPAR'
      print(f'Perdeu\nDeu impar vc {num} pc {sor} total {som} com {vit-1} vitorias consecutivas')
      break
elif usu == 'IMPAR': 
  while usu != '':
    num = int(input('Digite um numero de 1 a 10: '))
    sor = random.randint(0,10)
    # sor = 1
    som = num + sor
    vit += 1 
    tot = som%2==1
    print(num, sor)
    if usu == 'IMPAR' and tot == True:
      print(f'Ganhou\nDeu impar vc {num} pc {sor} total {som} com {vit} vitorias consecutivas')
      usu = str(input('Par ou Impar... ')).upper()
    elif usu == 'PAR' and tot == True:
      tot = som%2==0
      usu = 'PAR'
      print(f'Perdeu\nDeu impar vc {num} pc {sor} total {som} com {vit-1} vitorias consecutivas')
      break
    else:
      tot = som%2==0
      usu = 'PAR'
      print(f'Perdeu\nDeu par vc {num} pc {sor} total {som} com {vit-1} vitorias consecutivas')
      break

else:
  print('invalido')
 