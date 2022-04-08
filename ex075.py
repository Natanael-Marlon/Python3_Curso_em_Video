val_1 = int(input('Digite um valor '))
val_2 = int(input('Digite um valor '))
val_3 = int(input('Digite um valor '))
val_4 = int(input('Digite um valor '))
vals  = val_1 , val_2, val_3, val_4
vals9 = val_par = val3 = 0
for pos, c in enumerate(vals):
  if c == 9:
    vals9 += 1
    print(f'O nove apareceu {vals9} vezes')
  if c == 3:
    val3 += 1
    print(f'O 3 apareceu {val3} vezes')
  if c%2==0:
    val_par = c+1
    print(f'Sao {val_par-1} pares')



