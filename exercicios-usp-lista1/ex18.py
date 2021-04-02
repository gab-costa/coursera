'''Escreva um programa que leia uma data do usuário e calcule o dia seguinte. Por exemplo, se o usuário inserir valores que representem 18/11/2013,
o programa deve exibir 19/11/2013. A data deve ser inserida em formato numérico com três declarações de entrada separadas,
 uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa funcione corretamente para anos bissextos.'''

#I'm going to import the exercise 1, where I find the bissextile year
import ex1


months = {'01':31, '02':28 ,'03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31,'11':30,'12':31}


day = int(input('tell me a day'))
month = input('tell me a month')
year = int(input('tell me a year'))

if ex1.bissextile(year)== True:

    months['02']=29





if day == months[month]:
    if month =='12':
        year+=1
        month=1
        day =1
    else:

        month = int(month) + 1
        day=1

else:
    day+=1


print(day, month, year)

