soma = 0                # variável acumuladora
contador = 1            # variável contador

while contador <= 5:    # laço de repetição
    num = int(input("{}° valor: ".format(contador)))
    soma = soma + num           # acumulo dos resultados parciais
    contador = contador + 1     # incremento para contagem

print(soma)