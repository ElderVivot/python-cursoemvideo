n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
opcao = 0
soma = 0
multiplicacao = 0
maior = 0
while opcao != 5:
    print('------------------------')
    opcao = int(input("""O que você deseja:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair """))
    if( opcao == 1 ):
        soma = n1 + n2
        print('A opção selecionada foi SOMA, e o resultado desta é {}.'.format(soma))
    elif( opcao == 2 ):
        multiplicacao = n1 * n2
        print('A opção selecionada foi MULTIPLICAÇÃO, e o resultado desta é {}.'.format(multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('A opção selecionada foi MAIOR, e o resultado deste é {}.'.format(maior))
    elif opcao == 4:
        n1 = float(input('Digite o número 1: '))
        n2 = float(input('Digite o número 2: '))
    elif opcao == 5:
        print('Fechando o programa!!')
        break
    else:
        opcao = int(input('Opção digitada é inválida, digite uma nova opção novamente seguindo os '
                          'critérios passando anteriormente: '))