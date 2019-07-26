kms = float(input('Digite a quantidade de KM rodado: '))
dias = float(input('Digite a quantidade de dias que o carro ficou alugado: '))
valor_kms = kms * 0.15
valor_dias = dias * 60
valor_total = valor_kms + valor_dias
print('A quantidade de KMs rodados foi de {:.3f} durante {:.1f} dias. Portanto, o valor total a ser pago '
      'será {:.3f} '.format(kms, dias, valor_total))