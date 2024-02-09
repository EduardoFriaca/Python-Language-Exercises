def graphBar(a, b, c, d, e): #aqui é a função
    values = [a, b, c, d, e]
    for i in values:
        print('#' * i)
        
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))

graphBar(a, b, c, d, e)


