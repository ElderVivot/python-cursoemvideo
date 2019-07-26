n = float(input('Digite um valor: '))

notas_50 = notas_50 = n // 50
resto_50 = n % 50

notas_20 = resto_50 // 20
resto_20 = resto_50 % 20

notas_10 = resto_20 // 10
resto_10 = resto_20 % 10

notas_1 = resto_10 // 1

print(f'Total de {notas_50:.0f} de R$ 50,00')
print(f'Total de {notas_20:.0f} de R$ 20,00')
print(f'Total de {notas_10:.0f} de R$ 10,00')
print(f'Total de {notas_1:.0f} de R$ 1,00')