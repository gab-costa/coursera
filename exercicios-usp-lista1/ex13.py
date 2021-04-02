''' Escreva um programa que converta um número decimal (base 10) em binário (base 2). Leia o número decimal do usuário e use o seguinte algoritmo de divisão, exemplificado para o número 83 (base 10):

	83/2 = 41 resto 1
	41/2 = 20 resto 1
	20/2 = 10 resto 0
	10/2 = 5 resto 0
	5/2 = 2 resto 1
	2/2 = 1 resto 0
	1/2 = 0 resto 1
Os restos das divisões (começando do último valor) contém a representação binária do número, nesse caso 1010011 (base 2).'''

x = int(input('tell me a number'))
cont = x
rest =0
my_list = []
while cont >0:
    rest = cont % 2

    cont = cont//2
    my_list.append(rest)


    #print(rest)
my_list_format = []
for y in range(len(my_list),0,-1):
    #my_list_format.append(my_list[y-1])
    #print((my_list_format), end=' ')
    print(my_list[y-1], end='')



