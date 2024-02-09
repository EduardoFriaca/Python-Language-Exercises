n = int(input("Digite o valor de n (1 ≤ n ≤ 20): "))

# Verifica se o valor de n está no intervalo permitido
while n < 1 or n > 20:
    n = int(input("Digite um valor de n válido (1 ≤ n ≤ 20): "))

# Gera a sequência e imprime os n primeiros termos
for x in range(1, n+1):
    termo = x**2
    print(termo, end=' ')
