from dice import Die
import plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline
die=Die()
x=0
result=[]
while x<1000:
    bet=die.roll()
    result.append(bet)
    x+=1

lista=[]
k=1
for k in range(1,7):
    lista.append(result.count(k))

print(lista)



dict={1:result.count(1),2:result.count(2),
      3:result.count(3),4:result.count(4),5:result.count(5),6:result.count(6)}

x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values, y=lista)]

x_axis_config = {'title':'Result'}
y_axis_config= {'title':'Frequency of  result'}

my_layout = Layout(title='Resuls of rolling the die 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')





