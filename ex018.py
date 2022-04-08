import math
angulo = int(input('Digite o angulo '))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print('O angulo {}° tem \nsen{:.2f}° \ncos{:.2f}° \ntan{:.2f}°'.format(angulo,sen,cos,tan))
