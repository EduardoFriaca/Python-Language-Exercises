n = int(input("Número: "))
menor = n
maior = n
while n >= 0:
  if n < menor:
    menor = n
  if n > maior:
    maior = n
  n = int(input("Número: "))
if menor >= 0:
  print("Menor = ", menor)
  print("Maior = ", maior)
else:
  print("Nenhum número positivo informado.")