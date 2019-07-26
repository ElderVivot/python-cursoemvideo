n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print('O valor digitado em metros foi {:.3f}, o que equivale {:.3f} cm e {:.3f} mm.'.format(n, cm, mm))