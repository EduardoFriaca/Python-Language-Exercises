"""
Um pescador comprou um computador para controlar o rendimento diário. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do Estado de São Paulo (50 quilos), deve pagar uma multa de R$ 4,00 por quilo 
excedente. Escreva um programa que leia o peso de peixes, e verifique se há excesso. 
Se houver, determine o peso excedente e o valor da multa. Caso contrário, 
mostrar "Dentro do Regulamento.".
"""
peso = float(input("Peso dos Peixes: "))
if peso > 50.0:
  excedente = peso - 50.0
  multa = excedente * 4.00
  print(f"Peso Excendentede %.1f kg" % excedente)
  print(f"Valor da Multa = R$ %.2f" % multa)
else:
  print("Dentro do Regulamento.")