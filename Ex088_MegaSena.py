import random
import time

temp = []
mega_sena = []
numeros_individual = []
numeros = []

qtd_jogos = int(input('Quantos jogos você quer que o computador gere da MEGA SENA? '))

print('-'*30)

for i in range(0, qtd_jogos):
    mega_sena.append(temp[:])
    for j in range(0, 6):
        num_sorteado = random.randint(1, 60)
        while num_sorteado in mega_sena[i]:
            num_sorteado = random.randint(1, 60)
        mega_sena[i].append(num_sorteado)
    mega_sena[i].sort()
    print(f'JOGO {i+1}: {mega_sena[i]}')
    time.sleep(0.3)

print('-'*30)

# Avalia os números que mais se repetiram fazendo um intervalo de 1 à 60
for num in range(1, 61):

    # define que a quantidade vai começar por zero
    qtd_por_num = 0

    # percorre os jogos da mega sena e conta quantas vezes o número está repetido
    for jogos_mega in mega_sena:
        for valores_mega in jogos_mega:
            if valores_mega == num:
                qtd_por_num += 1

    # vai criar um vetor fazendo que tenha duas chaves, a primeira coma quantidade e a segunda com número que repetiu
    numeros_individual.append(qtd_por_num)
    numeros_individual.append(num)

    # adiciona cada número (1 a 60) e a quantidade que ele repetiu numa matriz bidimensional
    numeros.append(numeros_individual[:])

    # limpa o vetor dos números
    numeros_individual.clear()

# ordena para do que mais repetiu para o menos repetido
numeros.sort(reverse=True)

# imprime os 6 números que mais repetiram
print('Os 6 números que mais se repetiram foram: ', end='')
for k in range(0, 6):
    print(f'{numeros[k][1]} ({numeros[k][0]} vezes), ' if k < 5 else f'{numeros[k][1]} ({numeros[k][0]} vezes).', end='')

#print(numeros)