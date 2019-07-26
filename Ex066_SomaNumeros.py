n = soma = 0
while n != 999:
    n = int(input('Digite um número ou 999 para sair: '))
    if n == 999:
        break
    soma += n
print(f'A soma é {soma}')