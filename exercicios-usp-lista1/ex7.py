'''(MIT) Escreva um programa que conte o número de vogais numa string s composta unicamente de letras minúsculas. Por exemplo, se s = 'azcbobobegghakl', seu programa deve imprimir Número de vogais: 5.'''

s = input('tell me something')
cont=0
for i in s.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        cont+=1

print(f'o numero de vogais eh {cont}')