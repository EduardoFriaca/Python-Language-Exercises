# Programa que utiliza o comando for para imprimir
# cada um dos valores pares do intervalo de 0 até
# um valor informado pelo usuário.

n = int(input("Informe o valor limite: "))

for i in range(0, n+1, 2):
    print(i)