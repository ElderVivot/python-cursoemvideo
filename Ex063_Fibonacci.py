n = int(input('Digite a quantidade de termos da sequência Fibonacci que você deseja mostrar: '))
fib_ant = 0
fib_atu = 1
i = 1
calc_fib = 0
print('{} --> '.format(fib_ant), end='')
while i <= n:
    calc_fib = fib_ant + fib_atu
    fib_ant = fib_atu
    fib_atu = calc_fib
    print('{} --> '.format(fib_atu), end='')
    i += 1