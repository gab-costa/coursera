import matplotlib.pyplot as plt
import numpy as np
import json
import  math as mt
file_name1='memoria_peso.json'
file_name2='memoria_dia.json'

with open(file_name1, 'r') as lerpeso:
    peso_atual=json.load(lerpeso)

with open (file_name2, 'r') as lerdia:
    dia_atual=json.load(lerdia)


dia=int(input('me diga o DIA'))
peso_dia=float(input(f'me diga quanto você está pesando no dia {dia}'))
peso_atual.append(peso_dia)
dia_atual.append(dia)

print(dia_atual)
print(peso_atual)


with open (file_name1, 'w') as mempeso:
    json.dump(peso_atual, mempeso)


with open(file_name2, 'w') as memdia:
    #json.dump(pesos, memdia)
    json.dump(dia_atual, memdia)
    #pesos.append(peso_dia)
    #days.append(dia_pesagem)




plt.style.use('dark_background')
fig, ax  = plt.subplots()
ax.plot(dia_atual,peso_atual, linewidth=3, c='green' )# c ontrol the thickness of the line
ax.set_title("PESO /  DIA", fontsize=24) # sets the title of the chart
ax.set_xlabel('Dias')
ax.set_ylabel('peso')

ax.tick_params(axis='both', labelsize=14) #tickmarks means the scale

plt.show()
