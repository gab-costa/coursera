'''Monte um código que imprima os números de
1 a 100 mas, para múltiplos de 3, imprime trei ao invés do número; se é múltiplo de 5, imprime cinci; mas,
se é múltiplo de 3 e 5 ao mesmo tempo, imprime cincisprezece (3, 5 e 15 em romeno).'''

x= list(range(0,101))

for i in x:
    if i%3==0 and i%5==0:
        x[i]='cincisprezece'
    elif i%3 == 0:
        x[i]='trei'
    elif i%5==0:
        x[i]='cinci'
    else:
        pass

print(x)
