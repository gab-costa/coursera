'''Crie um programa que peça ao usuário um número e imprima todos os seus divisores. Se você não lembra o que é um
divisor, é um número que divide outro sem deixar resto. Por exemplo, 13 é um divisor de 26 porque 26/13 não tem nenhum resto.'''

x = int(input('tell me a number'))
cont=0
for k in range(1, x+1):
    if x%k==0:
        cont+=1
        print(k)
    else:
        pass
