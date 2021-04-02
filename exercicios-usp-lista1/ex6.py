'''O máximo divisor comum (MDC) de dois inteiros positivos, n e m, é o maior número, d, capaz de dividir n e m sem deixar resto. Existem vários algoritmos para determinar d, incluindo o seguinte:

1. inicialize d como o menor entre m e n;
2. enquanto d não dividir exatamente m e n, diminua o valor de d de uma unidade.
Ao final do algoritmo, d sera o MDC de n e m. Escreva um programa que leia dois inteiros positivos do usuário e use esse algoritmo para determinar e relatar seu máximo divisor comum.'''



n = int(input('tell a numbers'))
m =int(input('tell me the other number'))

lower = min(n,m)
while m%lower!=0 or n%lower!=0:
    lower-=1
print(lower)



