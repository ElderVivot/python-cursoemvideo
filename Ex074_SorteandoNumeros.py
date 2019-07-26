import random
n1 = random.randint(1,10)
n2 = random.randint(1,10)
n3 = random.randint(1,10)
n4 = random.randint(1,10)
v = (n1, n2, n3, n4)

menor = 0
maior = 0

for pos, _v in enumerate(v):
    if pos == 0:
        menor = _v
        maior = _v
    else:
        if _v < menor:
            menor = _v
        if _v > maior:
            maior = _v

print(f'Os valores escolhidos foram {v}')
print(f'O menor valor é {menor} e o maior é {maior}')