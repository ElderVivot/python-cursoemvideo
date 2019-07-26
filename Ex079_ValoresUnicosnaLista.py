val = []

continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um valor: '))
    while num in val:
        num = int(input('O número informado já foi digitado antes, informe um novo: '))
    val.append(num)
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()

val.sort()
print(val)