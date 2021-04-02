'''Se você tem 3 varetas, possivelmente de diferentes comprimentos, pode ou não ser possível ajeitá-las para que elas formem um triângulo. Por exemplo, se todos as varetas
tiverem um comprimento de 6cm, pode-se facilmente construir um triângulo equilátero. No entanto, se uma vareta tem 6cm e as outras duas têm apenas 2cm, não dá pra criar um
 triângulo. Em geral, se qualquer uma das varetas é maior ou igual à soma das outras duas, elas não podem ser usadas para formar um triângulo. Caso contrário, o triângulo existe.
Escreva um programa que determine se três comprimentos podem ou não formar um triângulo. O programa recebe 3 parâmetros e retorna um resultado booleano (True ou False).'''


l1 = float(input('tell me the l1 side'))
l2 = float(input('tell me the l2 side'))
l3 = float(input('tell me the l3 side'))

triangle = ''

if l1 >= (l2+l3) or (l2>=(l3+l1) or l3>=(l2+l1)):
    triangle = False
else:
    triangle = True


if triangle:
    print('the triangle was successfully formed')
else:
    print('this triangle can"t be formed')
