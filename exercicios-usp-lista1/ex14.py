'''Uma das maneiras de se referir a cores em websites e outras aplicações é a notação RGB (red-green-blue): três inteiros 0≤R,G,B≤255 como identificadores das tonalidades de vermelh
, verde e azul, respectivamente, que, quando mescladas, fornecem a cor desejada. Ao invés de fornecer os três inteiros em base 10, no entanto, é
comum usar base 16. Essa maneira de identificar cores é conhecida como código hexadecimal. Em base 16, precisamos de 16 caracteres para representar os “dígitos” de um número
(veja que em base 2 precisamos de dois, e em base 10, de dez). Usualmente são escolhidos os caracteres 0–9, com os valores usuais, e portanto precisamos de mais seis caracteres para
representar os “dígitos” de de 10 a 15. Usualmente usa-se as letras A–F. Por exemplo,
42 (base 10)=2A (base 16)=
=2×161+10×160.
Números que em base 16 são formados por apenas dois caracteres equivalem aos números de 0 a 255 (=162−1) em base 10. Além disso, no código hexadecimal as três tonalidades são
indicadas por uma única strin de seis caracteres. Por exemplo, o código hexadecimal CD1F41 corresponde aos tons R=205, G=31 e B=65, como você pode conferir aqui. Esse sistema
(ou seja, seis caracteres escolhidos do conjunto 0–9+A–F) é capaz de descrever 2563=16777216 cores diferentes, de 000000 (preto) a FFFFFF (branco). Com base nos exercícios anteriores sobre números binários, monte um algoritmo para converter uma string válida de seis caracteres representando uma cor em código hexadecimal para a notação RGB, ou seja, os três inteiros
0≤R,G,B≤255 com as tonalidades de vermelho,
verde e azul. Implemente também a conversão no sentido contrário, ou seja, dados três inteiros R,G,B∈[0,255], determine o código hexadecimal da cor em questão.'''








red = 0
green = 0
blue = 0


c=0
lista = []
while c<=2:
    base = 0
    cont = 0
    x = input('tell me something')
    A, B, C, D, E, F = 10, 11, 12, 13, 14, 15

    for k in range(1,-1,-1):


        if x[k] == 'A':
            base = base + ((16**cont)*(A))
        elif x[k] =='B':
            base = base + ( (16**cont) *(B))
        elif x[k] == 'C':
            base = base + 16 ** cont * (C)
        elif x[k] == 'D':
            base = base + 16 ** cont * (D)
        elif x[k] == 'E':
            base = base + 16 ** cont * (E)
        elif x[k] == 'F':
            base =  base + 16 ** cont * (F)
        else:
            base = base + ((16**cont)*(int(x[k])))
        cont+=1
    lista.append(base)
    c+=1

print(lista)













