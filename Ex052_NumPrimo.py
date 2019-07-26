num = int(input('Digite um número: '))
qtd_diviseis = 0
for i in range(1,num+1):
    if num % i == 0:
        qtd_diviseis = qtd_diviseis+1
if qtd_diviseis <= 2:
    print('Este número é primo.')
else:
    print('Este número NÃO é primo.')
#print(qtd_diviseis)