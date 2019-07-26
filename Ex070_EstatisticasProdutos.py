print('*'*50)
print('   LOJA VIVOT SOFTWARE    ')
novo_produto = 'S'
total = 0
maior_que_1000 = 0
mais_barato = ''
valor_mais_barato = 0
contador = 0
while novo_produto == 'S':
    print('-' * 30)
    nome = str(input('Nome Produto: '))
    valor = float(input('Valor Produto: '))
    contador += 1
    total += valor
    if valor > 1000:
        maior_que_1000 += 1
    if contador == 1:
        valor_mais_barato = valor
        mais_barato = nome
    else:
        if valor < valor_mais_barato:
            valor_mais_barato = valor
            mais_barato = nome
    novo_produto = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while novo_produto not in ('S, N, '):
        novo_produto = str(input('Opção inválida, digite [S/N]: ')).strip().upper()
    if novo_produto == 'N':
        break
    print('-' * 30 )
    print(f'O valor total da compra foi R$ {total:.2f}.')
    print(f'Existem {maior_que_1000} produtos com valores acima de R$ 1000,00.')
    print(f'O produto mais barato é o {mais_barato} e seu valor foi {valor_mais_barato:.2f}.')