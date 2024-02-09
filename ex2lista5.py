# Solicita ao usuário um número inteiro entre 0 e 15
n = int(input("Digite um número inteiro entre 0 e 15: "))

# Verifica se o número está dentro do intervalo permitido
if n < 0 or n > 15:
    print("Número inválido! Digite um número entre 0 e 15.")
else:
    # Inicializa o fatorial como 1
    fatorial = 1

    # Calcula o fatorial do número digitado pelo usuário
    for i in range(1, n+1):
        fatorial *= i

    # Imprime o resultado
    print(n,"! =",fatorial)
