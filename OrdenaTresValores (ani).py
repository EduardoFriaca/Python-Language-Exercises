print("Informe três valores inteiros, diferentes entre si.")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a < b):     # se a é menor que b, então ...
    if (b < c): # resta descobrir onde c se encaixa.
        print(a, b, c)
    elif (a < c):
        print(a, c, b)
    else:
       print(c, a, b)
else:           # senão, a é maior que b ...
    if (a < c): # resta descobrir onde c se encaixa.
        print(b, a, c)
    elif (b < c):
        print(b, c, a)
    else:
        print(c, b, a)