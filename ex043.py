peso    = float(input('Digite seu peso '))
altura  = float(input('Diigite sua altura '))
imc     = peso/(altura*altura)
if(imc < 18.5):
  print(f'{imc:.2f} kg/m2 Abaixo do Peso')
elif(imc < 25):
    print(f'{imc:.2f} kg/m2 Peso Ideal ')
elif(imc < 30):
    print(f'{imc:.2f} kg/m2 Sobrepeso ')
elif(imc <= 40):
    print(f'{imc:.2f} kg/m2 Obesidade ')
else:
    print(f'{imc:.2f} kg/m2 Obesidade Mórbida')

