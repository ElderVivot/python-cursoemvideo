n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
n4 = int(input('Valor 4: '))
v = (n1, n2, n3, n4)

print(f'O valor 9 aparece {v.count(9)} vezes.')
print(f'O primeiro valor 3 apareceu na posição {v.index(3)+1}.')

print('Pares: ', end='')
for i in v:
    if i % 2 == 0:
        print(f'{i} ', end='')
print('.')