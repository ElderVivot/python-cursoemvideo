valCasa = float(input('Valor da casa: '))
salComprador = float(input('Salário mensal do comprador: '))
anosPagar = int(input('Anos pra pagar a casa: '))
valMensalPagar = valCasa / anosPagar / 12
#print(valMensalPagar)
if valMensalPagar <= salComprador * 0.3:
    print('O valor mensal da prestação será R$ {:.2f}. Vai sobrar R$ {:.2f} para você gastar com '
          'outras coisas.'.format(valMensalPagar, salComprador - valMensalPagar))
else:
    print('Seu salário mensal não é suficiente pra comprar esta casa.')