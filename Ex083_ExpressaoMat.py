val = list()
exp = str(input('Digite uma expressão: '))
for i in range(0, len(exp)):
    val.append(exp[i:i+1])

qtd_esq = 0 # quantidade de caracteres (
qtd_dir = 0 # quantidade de caracteres )
for v in val:
    if v == '(':
        qtd_esq += 1
    if v == ')':
        qtd_dir += 1

# primeira regra pra ver se é valido
if qtd_esq == qtd_dir:
    valido_1 = 1
else:
    valido_1 = 0

qtd_esq_2 = 0 # quantidade de caracteres (
qtd_dir_2 = 0 # quantidade de caracteres )
for j in range(0, len(val)):
    if val[j] == '(':
        qtd_esq_2 += 1
    if val[j] == ')':
        qtd_dir_2 += 1

    if qtd_dir_2 <= qtd_esq_2:
        valido_2 = 1
    else:
        valido_2 = 0
        break

if valido_1 == 1 and valido_2 == 1:
    print('Expressão válida.')
elif valido_1 == 1 and valido_2 == 0:
    print("Expressão inválida pois existe um parêntese ')' fechado antes da hora.")
elif valido_1 == 0 and valido_2 == 1:
    print("Expressão inválida pois a quantidade de parênteses abertos não é igual aos fechados")
else:
    print("Expressão inválida pois a quantidade de parênteses abertos não é igual aos fechados e existe um parêntese fechado antes da hora. ")