import random
num_random = random.randint(1, 5)
#print(num_random)
cont = 0
num_digitado = int(input('Digite um número entre 1 e 5 para tentar adivinhar em qual número o computador pensou: '))
while num_digitado != num_random:
    num_digitado = int(input('Você errou, o computador pensou em outro número. Digite novamente pra tentar acertar: '))
    cont += 1
print('Parabéns, você acertou!!! Foi necessário {} tentativas para isto.'.format(cont))