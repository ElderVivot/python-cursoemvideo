peso = float(input('Digite o peso 1: '))
peso_menor = peso
peso_maior = peso
for i in range(1, 5):
    peso = float(input('Digite o peso {}: '.format(i + 1)))
    if(peso < peso_menor):
        peso_menor = peso
    if(peso > peso_maior):
        peso_maior = peso
print('O peso menor é {:.2f} e o peso maior é {:.2f}'.format(peso_menor, peso_maior))