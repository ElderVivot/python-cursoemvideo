def listaNum(* num):
    if len(num) > 0:
        print('-'*30)
        print('Analisando valores ...')
        print(f'{num} Foram informados {len(num)} ao todo.')
        print(f'O maior deles é {max(num)}')
    else:
        print('-' * 30)
        print('Analisando valores ...')
        print(f'Não foi informado nenhum falor.')
        print(f'Não existe valor maior')

listaNum(1,2,3,4)
listaNum(1)