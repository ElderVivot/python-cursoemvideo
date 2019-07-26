import math
cateto_opo = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do cateto adjascente: '))
#hipotenusa = math.sqrt( math.pow(cateto_opo, 2) + math.pow(cateto_adj, 2) )
hipotenusa = math.hypot(cateto_opo, cateto_adj)
print('Sendo o valor do cateto oposto sendo {:.2f} e do cateto adjascente {:.2f} então o valor da hipotenusa '
      'é {:.2f}!'.format(cateto_opo, cateto_adj, hipotenusa))