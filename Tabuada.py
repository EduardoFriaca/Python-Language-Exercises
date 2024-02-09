# Este programa apresenta a tabuada de um número,
# entre 1 e 10, escolhido pelo usuário.

n = int(input("Qual a tabuada desejada? "))

for i in range(11):
    print(n, "x", i ,"=", n*i)
