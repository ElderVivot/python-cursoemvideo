import random
par_impar = 'P'
total_par_impar = 'P'
qtd_ganhou = 0
while par_impar == total_par_impar:
    print('-=' * 20)
    print('VAMOS JOGAR PAR OU ÍMPAR!!')
    print('-=' * 20)
    num_jog = int(input('Informe um número: '))
    par_impar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
    while par_impar not in ('P, I'):
        par_impar = str(input('Valor Inválido, digite P para Par ou I para Ímpar: ')).strip().upper()
    num_pc = random.randint(1, 10)
    total = num_jog + num_pc
    if total % 2 == 0:
        total_par_impar = 'P'
    else:
        total_par_impar = 'I'
    if par_impar == total_par_impar:
        print(f'Você jogou {num_jog} e o computador jogou {num_pc}, e a soma dá {total}. Portanto, você ganhou. PARABÉNS!!!')
    else:
        print(f'Você jogou {num_jog} e o computador jogou {num_pc}, e a soma dá {total}. Portanto, você perdeu :( :( .')
        break
    qtd_ganhou += 1
if qtd_ganhou > 0:
    print(f'Você ganhou {qtd_ganhou} vezes consecutivas do computador. Fera demais ;) ;) ')
else:
    print('Infelizmente você não ganhou nenhuma vez do computador :( :( ')