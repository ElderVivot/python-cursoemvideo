frase = input('Digite uma frase: ')
print('Esta frase tem {} letras "a" '.format(frase.count('a')))
print('A letra "a" aparece a primeira vez na posição {}'.format(frase.find('a')))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.rfind('a')))