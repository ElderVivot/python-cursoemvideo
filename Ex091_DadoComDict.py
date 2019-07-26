import random
import time
import operator

dados = {
    "jogador1": random.randint(1, 6),
    "jogador2": random.randint(1, 6),
    "jogador3": random.randint(1, 6),
    "jogador4": random.randint(1, 6),
}

# Mostra os dados
print('Valores Sorteados:')
for k, v in dados.items():
    print(f'\tO {k} tirou {v}.')
    time.sleep(1)

print('-'*30)

# Rankeia do maior pro menor --> UMA DAS FORMAS
#i = 0
#print('Ranking dos Jogadores:')
#for item in sorted(dados, key = dados.get(), reverse=True):
#    i += 1
#    print(f'\t{i}º lugar: {item} com {dados[item]}')
#    time.sleep(1)

# Rankeia do maior pro menor
ranking = []
ranking = sorted(dados.items(), key = operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\t{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)
