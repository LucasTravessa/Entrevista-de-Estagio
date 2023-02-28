
# 1
INDICE = 13
SOMA =0
K = 0

for K in range(INDICE):
    K=K+1
    SOMA=SOMA+K

print (f'Soma: {SOMA}')

# 2

NUMERO = int(input("O numero pertense ou não a sequencia de fibonacci: "))

if (NUMERO==0) or (NUMERO==1):
    print("Pertence")

Fibo = 1
Fiboo = 2

while Fiboo < NUMERO:
    Fibo = Fibo+Fiboo
    Fiboo = Fiboo + Fibo

if (Fibo == NUMERO) or (Fiboo == NUMERO):
    print("Pertence")
else:
    print("Não pertence")

# 3

import json

with open("dados.json", "r") as f:
    entrada = json.load(f)

valor = []
for i in entrada:
    valor.append(i.get('valor'))


minimo = min(i for i in valor if i > 0)
maximo = max(valor)

print (f'Valor minimo: {minimo}')
print (f'Valor maximo: {maximo}')

total=0

for i in valor:
    total = total + i

media = total / len(valor)
dias = 0

for i in valor:
    if i > media:
        dias+=1

print(f'Dias em que o faturamento foi maior que a média: {dias}')

# 4

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

Total = SP + RJ + MG + ES + Outros

def porcent(estado):
   return round(estado*100/Total , 2)

print(f'SP: {porcent(SP)}%')
print(f'RJ: {porcent(RJ)}%')
print(f'MG: {porcent(MG)}%')
print(f'ES: {porcent(ES)}%')
print(f'Outros: {porcent(Outros)}%')

#5

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
istring = ''
tamS= len(string)

for i in reversed(range(0, tamS)):
    istring= istring + string[i]

print (f'stringe invertid: {istring}')
