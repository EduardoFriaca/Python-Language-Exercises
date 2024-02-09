"""
Escreva um programa que leia dois números reais 
e mostre o resultado da diferença do maior valor pelo menor valor.
"""
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

if n1 >= n2:
  print(n1 - n2)
else:
  print(n2 - n1)