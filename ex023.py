num = int(input('Digite um numero '))

mil_num = num // 1000 % 10
cen_num = num // 100 % 10
dez_num = num // 10 % 10
uni_num = num // 1 % 10
print('milhar {}\ncentena {}\ndezena {}\nunidade {}'.format(mil_num,cen_num,dez_num,uni_num))


