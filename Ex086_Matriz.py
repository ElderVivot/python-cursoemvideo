matriz_temp = []
matriz = []
linhas = int(input('Digite a quantidade de linhas que sua matriz terá: '))
colunas = int(input('Digite a quantidade de colunas que sua matriz terá: '))

# Insere os dados
# le as linhas
for i in range(0, linhas):
    matriz.append(matriz_temp[:])
    # le as colunas
    for j in range(0, colunas):
        val = int(input(f'Digite o valor para {[i+1, j+1]}: '))
        matriz[i].append(val)

print('-'*20)

# Imprime os dados
# le as linhas
for i in range(0, linhas):
    # le as colunas
    for j in range(0, colunas):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()