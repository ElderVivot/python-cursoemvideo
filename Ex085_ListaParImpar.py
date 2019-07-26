lista = [[],[]]
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'A lista com os valores de ímpares e pares separados é: {lista}')
lista[0].sort()
lista[1].sort()
#lista.sort()
print(f'A lista com os valores de ímpares e pares em ordem é: {lista}')