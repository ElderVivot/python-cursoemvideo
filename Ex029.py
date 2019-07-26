vel = float(input('Digite o valor da velocidade em KM: '))
if vel > 80.0:
    valor_multa = (vel - 80.0) * 7
    print('Você foi multado, e o valor dela será {:.2f}'.format(valor_multa))
else:
    print('Parabéns você não foi multado.')