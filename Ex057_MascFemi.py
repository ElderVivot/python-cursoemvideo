sexo = ''
while sexo != '.':
    sexo = input('Digite o sexo da pessoa, sendo M-Masculino e F-Feminino. E digite . para sair: ').upper()
    if( sexo not in('M, F, .') ):
        sexo = input('Valor digitado ({}) inválido, deve ser informado M para Masculino e F para Feminino: ').format(sexo).upper()