def notas(*val, situacao=False):
    media = sum(val)  / len(val)
    if situacao == False:
        return {"qtd_notas": len(val), "maior_nota": max(val), "menor_nota": min(val), "media": media}
    else:
        if media > 7:
            sit = "BOA"
        elif 5 < media <= 7:
            sit = "MAIS OU MENOS"
        else:
            sit = "RUIM"
        return {"qtd_notas": len(val), "maior_nota": max(val), "menor_nota": min(val), "media": media, "situacao": sit}


print(notas(6, 7, 8, 3.4, situacao=True))