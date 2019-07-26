val = list()

continuar = 'S'
cont = 0
while continuar == 'S':
    num = int(input('Digite um valor: '))
    val.append(num)
    cont += 1
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while continuar not in ('S', 'N'):
        continuar = str(input('Valor incorreto, digite [S/N] para continuar: ')).upper().strip()

val.sort(reverse=True)
print(f"Lista reversa: {val}")
print(f"Quantidade de números: {cont}")
if 5 in val:
    print("O número 5 existe na lista digitada.")
else:
    print("O número 5 NÃO está na lista digitada.")