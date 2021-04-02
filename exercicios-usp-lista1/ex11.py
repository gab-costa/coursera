''' Digamos que eu lhe forneça uma lista de números: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Escreva uma única linha em Python que gere uma nova lista apenas com os elementos pares de a. '''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([par for par in a if par%2==0 ])