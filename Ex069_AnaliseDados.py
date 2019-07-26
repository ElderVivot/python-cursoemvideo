continuar = 'S'
qtd_maior_18 = 0
qtd_homens = 0
qtd_mulheres_menos_20 = 0
while continuar == 'S':
    print('-'*30)
    print('   CADASTRE UMA PESSOA    ')
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    while sexo not in ('M, F'):
        sexo = str(input('Sexo inválido, digite [M/F]: ')).strip().upper()
    if idade > 18:
        qtd_maior_18 += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade < 20:
        qtd_mulheres_menos_20 += 1
    print('-' * 30)
    cotinuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while continuar not in ('S, N'):
        continuar = str(input('Opção inválida, digite [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Há {qtd_maior_18} pessoas maiores que 18 anos nos dados digitados.')
print(f'Há {qtd_homens} homens nos dados digitados.')
print(f'Há {qtd_mulheres_menos_20} mulheres com menos de 20 anos nos dados digitados.')
