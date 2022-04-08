import math
cop  = float(input('Cateto Oposto '))
cad  = float(input('Cateto Adjascente '))
pcop = math.pow(cop ,2)
pcad = math.pow(cad ,2)
hip  = math.sqrt(pcop + pcad)
print('o Cateto oposto {}\ne o Adjascente {}\nda a hipotenusa {:.2f}'.format(cop,cad,hip))
