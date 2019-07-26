import random
from time import sleep
num_random = random.randint(1, 3)
#num_random = 1
# 1 será papel ; 2 será tesoura ; 3 será pedra
if num_random == 1:
    texto_pc = 'papel'
elif num_random == 2:
    texto_pc = 'tesoura'
else:
    texto_pc = 'pedra'

num_digitado = int(input('Digite 1 para papel, 2 para tesoura ou 3 pra pedra: '))
if num_digitado == 1:
    texto_jogador = 'papel'
elif num_digitado == 2:
    texto_jogador = 'tesoura'
else:
    texto_jogador = 'pedra'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
# computador ganha:
# jogador escolhe 3-pedra e computador escolhe 1-papel
# jogador escolhe 2-tesoura e computador escolhe 3-pedra
# jogador escolhe 1-papel e computador escolhe 2-tesoura
if ( num_digitado == 3 and num_random == 1 ) or ( num_digitado == 2 and num_random == 3 ) or \
        ( num_digitado == 1 and num_random == 2 ):
    print('Você escolheu {} e o computador escolheu {}. Portanto, o computador ganhou.'.format(texto_jogador, texto_pc))

# jogador ganha
# computador escolhe 3-pedra e jogador escolhe 1-papel
# computador escolhe 2-tesoura e jogador escolhe 3-pedra
# computador escolhe 1-papel e jogador escolhe 2-tesoura
elif ( num_random == 3 and num_digitado == 1 ) or ( num_random == 2 and num_digitado == 3 ) or \
        ( num_random == 1 and num_digitado == 2 ):
    print('Você escolheu {} e o computador escolheu {}. Portanto, você ganhou.'.format(texto_jogador, texto_pc))

# jogo empata
else:
    print('Você escolheu {} e o computador escolheu {}. Portanto, jogou empatou.'.format(texto_jogador, texto_pc))