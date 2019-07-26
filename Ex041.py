import datetime
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >= 15 and idade <= 19:
    print('JÚNIOR')
elif idade >= 20 and idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')