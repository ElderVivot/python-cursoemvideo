frase = str(input('Digite uma frase: '))
frase_sem_espaco = frase.replace(' ', '')
nova_frase = str('')
for i in range(len(frase_sem_espaco), 0, -1):
    nova_frase = nova_frase + '' + frase_sem_espaco[i-1]
if nova_frase == frase_sem_espaco:
    print('É um palíndromo, visto que a frase digitada inicialmente sem espaço é {} e de trás pra frente ela '
          'fica {}.'.format(frase_sem_espaco, nova_frase))
else:
    print('Não é um palíndromo, visto que a frase digitada inicialmente sem espaço é {} e de trás pra frente ela '
          'fica {}.'.format(frase_sem_espaco, nova_frase))