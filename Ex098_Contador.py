import time

def contador(ini, fim, passo):
    if passo == 0 and fim > ini:
        passo = 1
    if passo == 0 and fim < ini:
        passo = -1
        
    if passo > 0:
        print(f'Contagem de {ini} até {fim} saltando {passo} números: ', end='')
        for i in range(ini, fim + 1, passo):
            print(f'{i} ... ', end='', flush=True)
            time.sleep(0.5)
    else:
        print(f'Contagem regressiva de {ini} até {fim} saltando {passo*-1} números: ', end='')
        for i in range(ini, fim - 1, passo):
            print(f'{i} ... ', end='', flush=True)
            time.sleep(0.5)
    print()


contador(1, 10, 1)
print()
contador(10,0,-2)

print()
print('Informe você mesmo os valores:')
contador(int(input('- Digite o número que a contagem deve começar: ')), int(input('- Digite em qual terminar: ')),
         int(input('- E de quantos você quer pular em cada número: ')))

