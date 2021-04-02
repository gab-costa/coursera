'''Implemente o seguinte joguinho de computador: o usuário deve adivinhar um número de 1 a 100 “pensado” pelo computador
(use a função randint() do módulo numpy.random). A cada palpite do usuário, o programa vai “cercando” o número, informando
o intervalo [a,b] em que ele se encontra. Acompanhe o seguinte exemplo, em que o número secreto é 42:

Adivinhe o número:
Está entre 0 e 100: 25
Está entre 25 e 100: 60
Está entre 25 e 60: 40
Está entre 40 e 60:
E assim por diante, até o usuário acertar. Não precisa de interface gráfica! Use a função input() para pedir ao usuário
seu palpite (ou seja, crie uma TUI — text-based user interface). Qual é a melhor estratégia para ganhar o jogo no menor número de tentativas?'''
import numpy as np

correct = np.random.randint(0,101)
x =0
min = 0
max = 100
while x!= correct:
    x = int(input('tell me a number'))

    if x < correct :
        min = x
        print(f' o valor está entre {min} e {max}')


    elif x > correct :
        max = x
        print(f'o valor está entre {min} e {max}')

    else:
        print(f'parabens, o valor sorteado é {x}')
        print(correct)