num = int(input('Digite um número: '))
i = num
res_fatorial = num
"""while i > 1:
    i -= 1
    res_fatorial = res_fatorial * i
print('O fatorial de {} é {}.'.format(num, res_fatorial))"""

for j in range(num - 1, 0, -1):
    res_fatorial = res_fatorial * j
print('O fatorial de {} é {}.'.format(num, res_fatorial))