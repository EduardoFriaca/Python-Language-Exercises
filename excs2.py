preco = int(input("Digite o preço: "))
formadepagamento = input("Escolha a forma de pagamento: ")
if formadepagamento == "1":
    preco = preco - (preco*0.1)
    print("Deve-se pagar", preco)
elif formadepagamento == "2":
    preco = preco - (preco*0.05)
    print("Deve-se pagar", preco)
elif formadepagamento == "3":
    preco = preco/2
    print("Deve-se pagar em duas prestações de:", preco)
else:
   preco = preco + preco*0.1
   print("Vai se pagar: ", preco)
         
