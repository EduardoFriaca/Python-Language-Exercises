n1 = int(input("Escreva um numero inteiro:"))
n2 = int(input("Escreva um numero inteiro:"))

print('O primeiro número é:', n1)
print('O segundo número é:', n2)
print('Invertendo fica:')

backup = n2
n2 = n1
n1 = backup

print('O primeiro número é:', n1)
print("O segundo número é:", n2)
