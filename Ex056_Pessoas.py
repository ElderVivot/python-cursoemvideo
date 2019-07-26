print('DADOS DA PESSOA 1: ')
nome = input('- Nome: ')
idade = int(input('- Idade: '))
sexo = input('- Sexo (M=Masculino;F=Feminino): ')
print('-----------------------')
media = 0
soma = idade
maior_idade = idade
nome_pessoa_mais_velha = nome
qtd_mulher_menos_20 = 0
for i in range(2, 5):
    print('DADOS DA PESSOA {}: '.format(i))
    nome = input('- Nome: ')
    idade = int(input('- Idade: '))
    sexo = input('- Sexo (M=Masculino;F=Feminino): ')
    print('-----------------------')
    soma = soma + idade
    if sexo == 'F' and idade < 20:
        qtd_mulher_menos_20 = qtd_mulher_menos_20 = 1
    if idade > maior_idade:
        nome_pessoa_mais_velha = nome
media = soma / 4
print('')
print('A média de idade entre as 4 pessoas é {:.2f}.'.format(media))
print('A pessoa mais velha é {}.'.format(nome_pessoa_mais_velha))
print('A quantidade de mulheres com menos de 20 é {}.'.format(qtd_mulher_menos_20))