import math

vel = float(input('diga qts Km/h...'))

if(vel >= 81):
  print('multado..')
  exesso = vel - 80
  multa = exesso * 7
  print('R${:.2f} pro detran'.format(multa))
else:
  print('Da proxima não escapa')

