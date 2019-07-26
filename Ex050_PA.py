a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = int(input('Digite a quantidade de termos que esta PA terá: '))
an = a1
print('a1 = {}'.format( an))
for i in range(2, n+1):
    an_old = an
    an = an + razao
    print('a{} = a{} + r = {} + {} = {}'.format(i, i-1, an_old, razao, an))
#print(an)