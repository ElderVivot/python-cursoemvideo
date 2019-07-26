import datetime
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
diferenca_18 = abs(18 - idade)
print()
if idade < 18:
    print('Você ainda terá que se alistar pro serviço militar, e falta {} anos pra isto.'.format(diferenca_18))
elif idade > 18:
    print('Você já deve ter se alistado para para o serviço militar, visto se que passou {} anos pra este '
          'prazo.'.format(diferenca_18))
else:
    print('Você está no ano do seu alistamento.')