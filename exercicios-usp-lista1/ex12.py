""" Escreva um programa que converta um número binário (base 2) em decimal (base 10). Seu programa deve ler o
número binário do usuário como uma sequência de zeros e uns e exibir o número decimal equivalente, processando cada dígito da representação binária.
 Por exemplo, 1010011 (base 2) ≡ 83 (base 10), obtido a partir da definição:

"""

x = input('tell me a binary number')
exp = 0
sum_ = 0
for k in range(len(x),0,-1):
    if x[k-1] == '1':
        sum_ += 2**exp

    else:
        pass



    exp+=1

print(sum_)