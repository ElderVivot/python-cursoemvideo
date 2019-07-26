temp = []
alunos = []

continuar = 'S'
id_aluno = 0

while continuar == 'S':

    # cada aluno tem um ID
    id_aluno += 1
    temp.append(id_aluno)

    # pega os dados e adiciona no vetor temporário
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))

    # copia os dados do vetor temp para o de alunos
    alunos.append(temp[:])

    # limpa o vetor temp
    temp.clear()

    # questiona se quer continuar ou não, e o while valida a resposta informada
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    while continuar not in ('S, N'):
        continuar = str(input('Valor incorreto, digite S para continuar e N para parar: ')).strip().upper()

print('-='*30)

# mostra os dados de todos os alunos
print(' Nº | NOME               | MÉDIA ')
for i in range(0, len(alunos)):
    media = ( alunos[i][2] + alunos[i][3] ) / 2
    print(f'{alunos[i][0]:^3} | {alunos[i][1]:<18} | {media:^5.2f}')

# mostra as notas de cada aluno individualmente, de acordo o que o usário desejar
while True:
    print('+' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (0 Interrompe) '))
    if(aluno == 0):
        break
    # mostra as notas
    print(f'- As notas de {alunos[aluno-1][1]} foram {alunos[aluno-1][2]:.2f} e {alunos[aluno-1][3]:.2f}')

