casa       = float(input('Diga o valor da casa '))
sal        = float(input('Diga o valor do salario '))
anos_pagar = float(input('diga em quantos anos pagar '))
anos       = anos_pagar * 12
parcela    = casa / anos
li_mensal  = sal*0.30

if(li_mensal > parcela):
  print('O emprestimo foi aceito em {:.0f}x com o valor de parcela em {:.2f} '.format(anos,parcela))
else:
  print('O emprestimo foi negado em {:.0f}x com o valor de parcela em {:.2f}  pq seus 30% é {:.2f}'.format(anos,parcela,li_mensal))

