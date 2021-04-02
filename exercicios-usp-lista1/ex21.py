import numpy as np
lista = []
def password_generator():

    length = np.random.randint(7,10)
    cont = 0
    password = ''
    while cont<=length:
        caracter = np.random.choice(range(33,147))
        lista.append(chr(caracter))
        cont+=1
        password +=lista[cont-1]

    return password



print(password_generator())


