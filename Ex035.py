a = float(input('Digite o valor da reta A: '))
b = float(input('Digite o valor da reta B: '))
c = float(input('Digite o valor da reta C: '))
ab_menos = abs(a - b)
ab_mais = a + b
ac_menos = abs(a - c)
ac_mais = a + c
bc_menos = abs(b - c)
bc_mais = b + c
if ((ab_menos < c) and (c < ab_mais)) and ((ac_menos < b) and (c < ac_mais)) and ((bc_menos < a) and (a < bc_mais)):
    print('Estas retas podem formar um triângulo')
else:
    print('Estas retas NÃO podem formar um triângulo')