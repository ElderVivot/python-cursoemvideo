val = []

for i in range(0, 5):
    val.append(input(f'Digite o valor {i}: '))

maior = 0
menor = 0
for c, obj in enumerate(val):
    if c == 0:
        maior = obj
        menor = obj
    else:
        if obj > maior:
            maior = obj
        if obj < menor:
            menor = obj

posicoes_maior = ''
posicoes_menor = ''
for j in range(0, len(val)):
    if val[j] == maior:
        posicoes_maior = posicoes_maior + str(j) + ' ...'
    if val[j] == menor:
        posicoes_menor = posicoes_menor + str(j) + ' ...'

print(f'O menor valor é {menor} nas posições {posicoes_menor}')
print(f'O maior valor é {maior} nas posições {posicoes_maior}')

