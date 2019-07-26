digitar = input('Deseja começar a digitar os valores agora? [S] - Sim, [N] - Não: ').upper()
i = 1
maior = 0
menor = 0
media = 0
soma = 0
while digitar == 'S':
    n = float(input('Digite o valor: '))
    if( i == 1 ):
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    i += 1
    digitar = input('Deseja continuar digitando? [S] - Sim, [N] - Não: ').upper()
media = soma / i
print('Você digitou {} números. O maior entre eles é o {:.2f} e o menor é {:.2f}. A soma é {:.2f} e a média '
      'é {:.2f}'.format(i, maior, menor, soma, media))