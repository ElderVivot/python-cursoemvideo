jogador = {}
lista_jogos = []
lista_jogador = []

while True:
    print('-'*30)

    jogador['nome'] = str(input('Digite o nome do jogador: '))
    qtd_partidas = int(input(f'Quantos jogos o {jogador["nome"]} participou? '))

    #qtd_gols = 0
    for i in range(1, qtd_partidas+1):
        lista_jogos.append(int(input(f'Quantos jogos na partida {i}? ')))
        #qtd_gols += lista_jogos[i-1]

    jogador['gols'] = lista_jogos[:]
    jogador['total'] = sum(lista_jogos)

    lista_jogador.append(jogador.copy())

    # limpa os dados do jogador e jogos depois de ter adicionado na lista_jogador
    jogador.clear()
    lista_jogos.clear()

    # questiona se quer continuar ou não, e o while valida a resposta informada
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    while continuar not in ('S, N'):
        continuar = str(input('Valor incorreto, digite S para continuar e N para parar: ')).strip().upper()
    if continuar == "N":
        break

print('-='*30)
#print(lista_jogador)

# mostra os dados de todos os alunos
print('cod | nome                | gols                 | total')
for i in range(0, len(lista_jogador)):
    print(f'{i+1:<3} | {lista_jogador[i]["nome"]:<19} | {str(lista_jogador[i]["gols"]):<20} | {lista_jogador[i]["total"]:^5}')

while True:
    print('-' * 50)
    jogador_id = int(input('Mostrar dados de qual jogador? (0 Interrompe) '))
    print('-' * 50)
    if (jogador_id == 0):
        break
    print(f'O jogador {lista_jogador[jogador_id-1]["nome"]} jogou {len(lista_jogador[jogador_id-1]["gols"])} jogos:')
    for k, v in enumerate(lista_jogador[jogador_id-1]["gols"]):
        print(f'\t- Na partida {k+1} ele marcou {v} gols.')
    print(f'Foi um total de {lista_jogador[jogador_id-1]["total"]} gols.')