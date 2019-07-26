distancia = float(input('Digite a distância em KM será percorrida nesta viagem: '))
if distancia <= 200.00:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('A distância percorrida será {:.2f} e o preço será {:.2f}'.format(distancia, preco))