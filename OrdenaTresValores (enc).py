print("Informe três valores inteiros, diferentes entre si.")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a < b) and (b < c):
    print(a, b, c)
elif (a < c) and (c < b):
    print(a, c, b)
elif (c < a) and (a < b):
    print(c, a, b)
elif (b < a) and (a < c):
    print(b, a, c)
elif (b < c) and (c < a):
    print(b, c, a)
else:
    print(c, b, a)