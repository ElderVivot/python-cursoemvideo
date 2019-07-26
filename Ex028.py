import random
num_random = random.randint(1, 5)
#print(num_random)
num_digitado = int(input('Digite um número entre 1 e 5 para tentar adivinhar em qual número o computador pensou: '))
if num_digitado == num_random:
    print('O número que você digitou ({}) é igual ao que o computador pensou. Parabéns!!!'.format(num_digitado))
else:
    print('O número que você digitou foi o {}, mas o que o computador pensou é o {}. Você errou :('.format(num_digitado, num_random))