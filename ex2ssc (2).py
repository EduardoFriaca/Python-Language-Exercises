n = int(input("Digite a quantidade de números: "))
for x in range(0,n,1):
    nu = int(input("Digite um número para calcular o fatorial: "))
    resp = 1
    i = 1
    for y in range(0,nu,1):
        resp = resp*i
        i += 1
    print(f"O fatorial de {nu} = {resp}\n")
    
