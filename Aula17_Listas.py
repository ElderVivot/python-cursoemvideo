num = [2, 3, 4, 2]
num[1] = 3
num.append(5)
num.sort()
num.insert(1, 7) # insere na posição 1 o valor 7
num.pop(3) # deleta o primeiro valor 3 encontrado
num.remove(2) # deleta o primeiro valor 2 encontrado
print(num)

a = [2,3,4,5]
b = a # quando faço uma lista receber a outra desta forma as duas tornam-se ligadas, tudo que alterar na primeira vai alterar na segunda
b[1] = 2
c = a[:] # desta forma é independente
c[2] = 3
print(b, a, c)