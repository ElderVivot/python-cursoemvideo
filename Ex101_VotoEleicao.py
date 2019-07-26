import datetime

def voto(ano_nasc=2000):
    ano_atual = datetime.datetime.today().year
    idade = ano_atual-ano_nasc

    if idade < 16:
        return "VOTO NEGADO"
    elif ( idade >= 16 and idade < 18 ) or idade > 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"

print(voto(1995))