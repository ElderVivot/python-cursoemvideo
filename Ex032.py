ano = int(input('Digite um ano qualquer: '))
bissexto = ano % 4
if bissexto == 0:
    print('O ano digitado é bissexto')
else:
    print('O ano digitado não é bissexto')