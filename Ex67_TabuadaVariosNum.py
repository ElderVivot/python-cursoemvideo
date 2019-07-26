n = 0
while n >= 0:
    print('-' * 30)
    n = int(input('De qual número você quer ver a tabuada? '))
    if n < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print('- {} x {} = {}'.format(n, i, n * i))