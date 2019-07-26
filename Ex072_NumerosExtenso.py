numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

num_usu = int(input('Digite um número entre 0 e 5: '))
while num_usu not in range(0, 6):
    num_usu = int(input('Número inválido. Digite um número entre 0 e 5: '))

#for i, num in enumerate(numeros):
print(f'Você digitou o número {numeros[num_usu]}.')