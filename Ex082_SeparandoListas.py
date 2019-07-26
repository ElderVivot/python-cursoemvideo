val = list()
val_par = list()
val_impar = list()
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        val_par.append(n)
    else:
        val_impar.append(n)
    val.append(n)
print(f'A lista original é {val}. A lista dos pares é {val_par}. A lista dos impares é {val_impar}')