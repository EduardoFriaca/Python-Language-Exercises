def diferenca(x,y): # funções para fazer os calculos das operações
    if x>y:
        subtra = x - y
        return subtra
    else:
        subtra = y - x
        return subtra

def divisao(x,y):
    if x>y:
        divi = x/y
        return divi
    else:
        divi = y/x
        return divi
    
def soma(x,y):
    so = x + y
    return so

def produto(x,y):
    mult = x*y
    return mult

def menu():
    while True:
        print("1 - Soma dos dois números digitados")
        print("2 - Diferença dos dois números digitados")
        print("3 - Produto dos dois números digitados")
        print("4 - Divisão dos dois números digitados")
        print("0 - Sair")
        x = int(input("Digite um número do menu:"))
        if x in [0, 1, 2, 3, 4]:
            return x
        else:
            print("Opção inválida. Tente novamente.")

while True:
    num1= int(input("Digite um número:"))
    num2= int(input("Digite um número:"))
    x = menu()
    
    if x==0:
        break
    elif x==1:
        s= soma(num1,num2)
        print(s)
    elif x==2:
        dif = diferenca(num1,num2)
        print(dif)
    elif x==3:
        prod= produto(num1,num2)
        print(prod)
    elif x==4:
        div = divisao(num1,num2)
        print(div)
