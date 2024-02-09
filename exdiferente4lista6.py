def diferenca(x,y): # funções para fazer os calculos das operações
    if x>y:
        subtra = x - y
        return subtra
    else:
        subtra = y - x
        return subtra

def divisao(x,y):
    if x>y:
        divisao = x/y
        return divisao
    else:
        divisao = y/x
        return divisao



while True:
    print("1 - Soma dos dois números digitados")
    print("2 - Diferença dos dois números digitados")
    print("3 - Produto dos dois números digitados")
    print("4 - Divisão dos dois números digitados")
    print("0 - Sair")
    num1= int(input("Digite um número:"))
    num2= int(input("Digite um número:"))
    x = int(input("Digite um número do menu:"))
    if x==0:
        break
    elif x==1:
        soma= num1+num2
        print(soma)
    elif x==2:
        dif = diferenca(num1,num2)
        print(dif)
    elif x==3:
        produto= num1*num2
        print(produto)
    elif x==4:
        div = divisao(num1,num2)
        print(div)
