t=0
cont = 2
pi = 0
while t < 15:

    fator = cont * (cont +1) * (cont+2)
    pi = pi + (-1)**(t)/fator

    cont +=2
    t+=1

real = 4*pi +3
print(real)