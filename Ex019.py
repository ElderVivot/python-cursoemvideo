from random import choice
n1 = str(input('Digite o nome 1: '))
n2 = str(input('Digite o nome 2: '))
n3 = str(input('Digite o nome 3: '))
n4 = str(input('Digite o nome 4: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('A pessoa escolhida foi {}'.format(escolhido))