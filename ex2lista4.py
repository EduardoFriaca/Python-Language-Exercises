num = int(input("Digite um número inteiro: "))
divisores = 0
x = 1

while x <= num:
    if num % x == 0:
        divisores += 1
    x += 1

if divisores == 2:
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")
