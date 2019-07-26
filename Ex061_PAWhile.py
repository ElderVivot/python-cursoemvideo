a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = int(input('Digite a quantidade de termos que esta PA terá: '))
an = a1
print('a1 = {}'.format( an))
i = 2
i_old = 2
while i <= n and n != 0:
    an_old = an
    an = an + razao
    print('a{} = a{} + r = {} + {} = {}'.format(i_old, i_old-1, an_old, razao, an))
    i += 1
    i_old += 1
    if( i == n + 1 ):
        print()
        n = int(input('Deseja digitar mais termos, caso sim, informe a quantidade, caso não, digite 0: '))
        i = 1
        print()
