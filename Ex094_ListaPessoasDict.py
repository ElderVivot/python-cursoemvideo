pessoa = {}
lista_pessoas = []

soma_idade = 0

while True:
    # adiciona os dados da pessoa
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo (M/F): '))
    pessoa['idade'] = int(input('Digite a idade: '))

    soma_idade += pessoa['idade']

    # copia o dado da pessoa atual para uma lista
    lista_pessoas.append(pessoa.copy())

    # limpa o dicionário (não obg mas desejável)
    pessoa.clear()

    print('-'*20)

    # questiona se quer continuar ou não, e o while valida a resposta informada
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    while continuar not in ('S, N'):
        continuar = str(input('Valor incorreto, digite S para continuar e N para parar: ')).strip().upper()
    if continuar == "N":
        break

print('-'*50)

print(lista_pessoas)

print('-'*50)

media_idade = soma_idade / len(lista_pessoas)
print(f"A) Foram cadastradas {len(lista_pessoas)} pessoas.")
print(f"B) A média de idade do grupo é {media_idade:.2f}")

print(f"C) As mulheres cadastradas foram: ", end='')
for i in range(0, len(lista_pessoas)):
    if lista_pessoas[i]["sexo"] == 'F':
        print(f'{lista_pessoas[i]["nome"]}, ', end='')

print()
print(f"D) A lista das pessoas que estão acima da média são: ")
for pes in lista_pessoas:
    if pes["idade"] > media_idade:
        print(f'\t-', end='')
        for k, v in pes.items():
            print(f"{k} = {v}; ", end='')
        print()

