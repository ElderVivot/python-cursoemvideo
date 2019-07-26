v = ('Maça', 5.50, 'Banana', 30.00, 'Abacaxi', 3.85, 'Laranja', 4.65, 'Morango', 10.39, 'Uva', 2.22)

print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*45)
for p, _v in enumerate(v):
    if p % 2 == 0:
        #tamanho = 20-len(_v)
        #qtd = '.'*tamanho
        print(f"{_v:.<30} R$: ", end='')
    else:
        #campo = (f'{_v:.2f}')
        #tamanho = 5-len(campo)
        #qtd = ' '*tamanho
        print(f'{_v:>7.2f}.')