qtd_homens = qtd_mulheres = qtd_maior = 0

while True:
    nome = str(input('Digite um nome: '))
    sexo = str(input('Qual o sexo [M/F])? ').upper())
    idade = int(input(f'Qual a idade ? '))
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres += 1
    if idade >= 18:
        qtd_maior += 1
    outra = str(input('Deseja continuar [S/N]? ').upper())
    if outra == 'N':
        break

print(f'1 Pessoas com +18 anos: {qtd_maior}')
print(f'2 Homens cadastrados: {qtd_homens}')
print(f'3 Mulheres com menos de 20 anos: {qtd_mulheres}')