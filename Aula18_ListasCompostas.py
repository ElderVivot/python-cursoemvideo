pessoas = list()
galera = list()

qtd_pessoa = int(input('Digite a quantidade de pessoas que você quer cadastrar: '))

for i in range(0, qtd_pessoa):
    pessoas.append(str(input(f'Digite o nome da {i+1}º pessoa: ')))
    pessoas.append(int(input(f'Digite a idade da {i+1}º pessoa: ')))
    galera.append(pessoas[:])
    pessoas.clear()

#print(galera)

for dados in galera:
    print(f'{dados[0]} tem {dados[1]} anos.')