import random
num = total = vit= 0
par = num%2==0
impar = num%2==1
usu = ''
pc  = res = ''
sorteio = random.randint(1,2)
c = 0
while True:
    usu = str(input('Par ou Impar... ')).upper()
    c += 1
    if(usu == 'PAR'):
        pc = 'IMPAR'
        sorteio = random.randint(1,2)
        num = int(input('Digite um numero de 1 a 10: '))
        print('Um dó lá sí e...\n Já!!!') 
        total = num + sorteio
        print(num,'+',sorteio,'=',total)
        if(total%2==0):
           print(f'Parbens ganhou eu escolhi {sorteio} e voce {num} e total {total} é par !!!\nVai Ota')
        else:
          print('Perdeu adeus!!')
          break
    elif(usu == 'IMPAR'):
        pc = 'PAR'
        sorteio = random.randint(1,2)
        num = int(input('Digite um numero de 1 a 10: '))
        print('Um dó lá sí e...\n Já!!!') 
        total = num + sorteio
        print(num,'+',sorteio,'=',total)
        if(total%2==1):
            print(f'Parbens ganhou eu escolhi {sorteio} e voce {num} e total {total} é impar !!!\nVai Ota')
        else:
            print('Perdeu adeus!!')
            break
print(f'Você ganhou {c - 1} vezes seguidas')