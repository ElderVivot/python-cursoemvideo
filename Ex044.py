valor = float(input('Valor do produto: '))
condicao_pagto = int(input('Qual será a condição de pagamento? 1 - Dinheiro/Cheque; 2 - Cartão de Débito; '
                       '3 - 2x Cartão de Crédito; 4 - 3x ou mais Cartão de Crédito '))
if condicao_pagto == 1:
    pagar = valor * 0.9
elif condicao_pagto == 2:
    pagar = valor * 0.95
elif condicao_pagto == 3:
    pagar = valor
else:
    pagar = valor * 1.2
print('O valor do produto original é {:.2f} e com sua forma de pagamento o valor à ser pago será '
      '{:.2f}:'.format(valor, pagar))
