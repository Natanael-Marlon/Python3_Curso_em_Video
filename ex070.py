total  = maisdemil = 0
barato = 100000000
while True:
    nome  = input('Nome do produto: ')
    preco = int(input('Preço do produto: '))
    total += preco
    if preco > 1000:
        maisdemil += 1
    if preco < barato:
        barato = preco
        prod_barato = nome
    continua = input('Deseja continuar? [S/N] ').upper()
    if continua == 'N':
        break
print(f'Total gasto {total} ')
print(f'Mais de R$1000 {maisdemil} produtos')
print(f'O mais barato foi o produto {prod_barato} ')

