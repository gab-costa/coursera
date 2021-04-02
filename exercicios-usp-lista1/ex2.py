'''   Escreva um programa que, dada uma duração de tempo em segundos, calcule o número equivalente  horas, minutos e segundos.'''

x= int(input('tell me the seconds'))
hour=0
minutes=0
seconds=0

hour  = x//3600
seconds = x%3600

if seconds >=60:
    minutes = seconds//60
    seconds = seconds%60
else:
    pass

print(f'hour{hour} minutes{minutes} seconds{seconds}')
