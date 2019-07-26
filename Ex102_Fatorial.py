def fatorial(num=1,show=True):
    result_fatorial = 1
    for i in range(num, 0, -1):
        result_fatorial *= i
    if show==True:
        for i in range(num, 0, -1):
            print(f'{i} x ' if i > 1 else f'{i} = ', end='')

    return result_fatorial

print(fatorial(5,True))