times = ('Atlético-MG','Palmeiras','São Paulo','Santos','Bahia','Botafogo','Cruzeiro','Athletico-PR','Flamengo',
         'Chapecoense','Corinthians','Ceará','Fluminense','Goiás','Internacional','Fortaleza','CSA','Grêmio','Avaí','Vasco')

print('Os cinco primeiros times do brasileirão são: ', end='')
for cinco_prim in range(0,5):
    print(f'{times[cinco_prim]}', end='' )
    print(', ' if cinco_prim != 4 else '.', end='')

print('\n', end='')
print('-'*60)

print('Os quatros últimos times do brasileirão são: ', end='')
for quatro_ult in range(19,15,-1):
    print(f'{times[quatro_ult]}', end='' )
    print(', ' if quatro_ult != 16 else '.', end='')

print('\n', end='')
print('-'*60)

print(sorted(times))

print('-'*60)

print(f"A Chapecoense está na {times.index('Chapecoense')+1}º.")
