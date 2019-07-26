val = []

for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n >= val[-1]:
        val.append(n)
        print('Valor inserido na última posição.')
    else:
        j = 0
        while j < len(val):
            if n <= val[j]:
                val.insert(j, n)
                break
            j += 1
        print(f'Valor inserido na posição {j}')

print(f'Os valores inseridos foram: {val}')
