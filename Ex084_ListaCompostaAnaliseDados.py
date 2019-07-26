pessoas = list()
galera = list()

continuar = 'S'

qtd_pessoas = 0
maior_peso = 0
menor_peso = 0
while continuar == 'S':
    # pega os dados do teclado
    nome = str(input(f'Digite o nome: '))
    peso = int(input(f'Digite o peso (KG): '))

    # adiciona na lista de pessoas
    pessoas.append(nome)
    pessoas.append(peso)

    # adiciona na lista de galeras
    galera.append(pessoas[:])

    # limpa a lista de pessoas para não duplicar valores
    pessoas.clear()

    # contabiliza qtd de pessoas adicionadas
    qtd_pessoas += 1

    # verifica qual é o maior peso
    if qtd_pessoas == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    # questiona se quer continuar e não, e o while valida a resposta informada
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    while continuar not in ('S, N'):
        continuar = str(input('Valor incorreto, digite S para continuar e N para parar: ')).strip().upper()

print('-'*30)

print(f'A quantidade de pessoas cadastradas foram {qtd_pessoas}.')

lista_pesados = ''
lista_leves = ''

for pes in galera:
    if pes[1] == maior_peso:
        lista_pesados = str(lista_pesados) + ', ' + pes[0]
    if pes[1] == menor_peso:
        lista_leves = str(lista_leves) + ', ' + pes[0]

print(f'O maior peso foi {maior_peso} KG. Sendo as pessoas mais pesadas: {lista_pesados}')
print(f'O menor peso foi {menor_peso} KG. Sendo as pessoas mais leves: {lista_leves}')
