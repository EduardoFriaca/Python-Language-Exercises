import math
custo = float(input("Custo: "))
ingresso = int(input("Ingressos: "))
minimo = math.ceil(custo / ingresso)
valorLucro = custo + (custo * 0.23)
ingressoLucro = math.ceil(valorLucro / ingresso)
print(f"Mínimo de Ingressos: {minimo}")
print(f"Ingressos para ter lucro de 23%: {ingressoLucro}")