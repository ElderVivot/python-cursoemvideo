import datetime

trabalhador = dict()

nome = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
idade = datetime.date.today().year - ano_nascimento
ctps = str(input('CTPS (informe 0 caso não tenha: )'))
if ctps != '0':
    ano_contratacao = int(input('Ano da 1º Contratação: '))
    salario = float(input('Salário: '))
    aposentadoria = ano_contratacao + 35
    trabalhador = {'nome': nome, 'idade': idade, 'ctps': ctps, 'contratacao': ano_contratacao, 'salario': salario,
                   'aposentadoria': aposentadoria}
else:
    trabalhador = {'nome': nome, 'idade': idade, 'ctps': ctps }

print('-'*30)

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')