'''Escreva um programa que implementa o método de Newton para extrair a raiz quadrada de um número digitado pelo usuário.
 O algoritmo é o seguinte:

1. leia x do usuário;
2. inicialize raiz em x / 2;
3. enquanto raiz não for “bom o suficiente,” atualize raiz para a média de raiz e x / raiz.
Quando o algoritmo é concluído, raiz contém uma aproximação da raiz quadrada de x. A qualidade da aproximação depende
de como você define “bom o suficiente,” então adote o seguinte critério de parada: o valor
absoluto da diferença entre raiz * raiz e x deve ser menor que 10−12.'''


x= float(input('tell me a number'))
sqrt = x/2
while abs((sqrt**2 - x )) >= 1.e-12 :
    sqrt = (sqrt + x/sqrt)/2
    print('oi')

print(sqrt)



