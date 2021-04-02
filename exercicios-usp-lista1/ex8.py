''' MIT - Escreva um código para contar o número de vezes que a sequência 'bob' aparece numa string s composta unicamente de letras minúsculas.
 Por exemplo, se s = 'azcbobobegghakl', seu programa deve imprimir Número de ocorrências de bob: 2.'''


s = input('tell me something')

cont = 0
for i in range(0,len(s)-2):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
        cont+=1


print(cont)