n = int(input('Digite um número: '))
print('Valor digitado foi {}, segue abaixo o valor da sua tabuada: '.format(n))
for i in range(1, 11):
    print('- {} x {} = {}'.format(n, i, n * i))