times = ('Fluminense','Athletico PR','Athletico GO','Athletico MG','Avaí','Botafogo','Ceará','Corinthians','Coritiba','Cuiaba','Flamengo','America MG','Fortaleza','Goias','Internacional','Juventude','Palmeiras','Bragantino','Santos','São Paulo')
for pos, cont in enumerate(times):
  print(f'{pos+1}° time = {cont}')
print('Libertadores! ')
for cont in range(0,5):
  print(f'{cont+1}° time = {times[cont]}')
print(f'Zona de Rebaixamento')
for cont in range(len(times)-4 ,len(times) ):
  print(f'{cont+1}° time = {times[cont]}')
print(f'Em ordem alfabetica fica: {sorted(times)}')
for pos, cont in enumerate(times):
  if cont == 'Fluminense': 
    print(f'{cont} esta em {pos+1}°')
