lanche = ('Suco', 'Refri', 'Pão', 'Feijão')

# for modelo 1
for k in range(0, len(lanche)):
    print(lanche[k])

print('-'*10)
# for modelo 2
for comida in lanche:
    print(comida)

print('-' * 10)
# for modelo 3
for pos, lanche_ in enumerate(lanche):
    print(f'Vou comer {lanche_} na posição {pos}.')

print('-'*10)
# ordena a lista
print(sorted(lanche))