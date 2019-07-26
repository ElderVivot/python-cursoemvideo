v = ('Maça', 'Banana', 'Abacaxi', 'Laranja', 'Morango', 'Uva')

for i in range(0, len(v)):
    print(f'Na palavra {v[i].upper()} existem as vogais:', end='')
    for j in v[i]:
        if j in ('a,e,i,o,u'):
            print(f' {j}', end='')
    print('.')