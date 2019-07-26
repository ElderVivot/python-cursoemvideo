import random
import time

def sorteia():
    lista = []

    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(random.randint(1, 10))
        print(f'{lista[i]} ', end='', flush=True)
        time.sleep(0.3)
    print('PRONTO!!')

    return lista

def somaPar(list):
    time.sleep(1)
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores par da lista {list} é {soma}.')

somaPar(sorteia())


