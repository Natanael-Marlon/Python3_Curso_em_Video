frase      = input('Digite a frase: ')
up_frase   = frase.upper()
cont_frase = up_frase.count('A')
pri_frase  = up_frase.find('A')
fin_frase  = up_frase.rfind('A')

print(' A letra a aparece {} vezes'.format(cont_frase))
print(' A letra aparece primeiro na posição {}'.format(pri_frase))
print(' A letra aparece a na ultima posição {}'.format(fin_frase))


