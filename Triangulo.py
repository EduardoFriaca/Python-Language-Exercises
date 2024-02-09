print('Informe a medida dos três lados da figura.')
a = int('Lado 1: ')
b = int('Lado 2: ')
c = int('Lado 3: ')

if (a < b+c) and (b < a+c) and (c < a+b):
    if (a==b) and (b==c):
        print('Essas medidas formam um triângulo equilátero.')
    elif (a!=b) and (b!=c) and (a!=c):
        print('Essas medidas foram um escaleno.')
    else:
        print('Essas medidas formam um triângulo isósceles.')
else:
    print('Essas medidas não formam um triângulo.')