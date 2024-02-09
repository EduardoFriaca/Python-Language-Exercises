"""
Um comerciante comprou um produto e quer vendê-lo lucro de 45% 
se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. 
Escreva um programa que receba o valor do produto e exiba o valor da venda.
"""
preco_produto = float(input("Preço do Produto: "))
if preco_produto < 20.00:
  preco_venda = preco_produto + (preco_produto * 0.45)
else:
  preco_venda = preco_produto * 1.30
print(f"Preco de Venda: %.2f" % preco_venda)