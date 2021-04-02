'''Escreva um programa que leia um ano do usuário e exiba uma mensagem dizendo se ele é ou não um ano bissexto.'''

def bissextile(x):
    t= False



    if x%400 ==0:
        print(f'the year {x} is bissextile')
        t=True
    elif x%100== 0:
        print(f'the year {x} is not bissextile')
    elif x%4==0:
        print(f'the year {x} is bissextile')
        t=True
    else:
        print(f'the year {x} is not bissextile')

    return t



