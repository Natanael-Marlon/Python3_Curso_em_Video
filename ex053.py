palavras = str(input('Digite aí: ')).strip().upper()
separa   = palavras.split()
junta    = ''.join(separa)
inverso  = ''
for c in range(len(junta) -1,-1,-1):
  inverso += junta[c]
if(inverso == junta):
  print(f'{inverso} é um palindromo')
else:
  print(f'{inverso} não é um palindromo')

