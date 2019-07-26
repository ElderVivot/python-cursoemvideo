h = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
area = h * l
qtd_litros = area / 2
print('A área das medidas passadas é {:.2f} m². E será necessário {:.2f} litros de tintas necessários pra '
      'pintar.'.format(area, qtd_litros))