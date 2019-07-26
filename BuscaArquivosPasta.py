import os
from unicodedata import normalize

def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def buscaArquivosEmPasta(caminho, extensao):
    arquivos = os.listdir(caminho)
    lista_arquivos = []

    for arquivo in arquivos:
        if arquivo.endswith(extensao):
            lista_arquivos.append(arquivo)

    return lista_arquivos

print(buscaArquivosEmPasta("C:\\Users\\Elder Vivot Dias\\Downloads\\ARQUIVOS TESTE FRANCESINHA\\BANCO BRADESCO GOLDMAQ", ".xls"))

print(remover_acentos('ábóõçÁ'))