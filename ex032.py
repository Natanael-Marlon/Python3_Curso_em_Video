ano = int(input('Diga o ano e direi se é bissexto... '))
if(ano%4==0):
  print('o ano {} é bissexto'.format(ano))
else:
  print('o ano {} não é bissexto'.format(ano))