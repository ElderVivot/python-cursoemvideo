dados = []
pessoas = {}
#pessoas = {'nome':'Elder', 'sexo':'M', 'idade':24}

for i in range(0, 3):
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo (M/F): ')).strip().upper()
    pessoas['idade'] = int(input('Idade: '))

    # adiciona em dados
    dados.append(pessoas.copy())

    # limpa pessoas
    pessoas.clear()

for pes in dados:
    for k, v in pes.items():
        print(f'O campo {k} tem o valor {v}.')
