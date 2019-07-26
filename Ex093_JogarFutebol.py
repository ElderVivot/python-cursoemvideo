jogador = {}
lista_jogos = []

jogador['nome'] = str(input('Digite o nome do jogador: '))
qtd_partidas = int(input(f'Quantos jogos o {jogador["nome"]} participou? '))

#qtd_gols = 0
for i in range(1, qtd_partidas+1):
    lista_jogos.append(int(input(f'Quantos jogos na partida {i}? ')))
    #qtd_gols += lista_jogos[i-1]

jogador['gols'] = lista_jogos
jogador['total'] = sum(lista_jogos)

print('-'*50)

print(jogador)

print('-'*50)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")

print('-'*50)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos:')
#for i in range(1, qtd_partidas+1):
for k, v in enumerate(jogador["gols"]):
    print(f'\t- Na partida {k+1} ele marcou {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')