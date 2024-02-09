# Calcula raízes de uma equação do 2o grau
import math

print("Informe os coeficientes da equação do 2o grau, dada na forma ax²+bx+c.")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c

if (delta < 0):
    print("Não há raízes reais para esta equação.")
else:
    if (delta == 0):
        x = (-b + math.sqrt(delta)) / 2*a
        print("A equação apresenta raízes coincidentes no ponto ", x)
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("A equação apresenta raízes os pontos ", x1, "e", x2, "como raízes.")

print("Fim do programa.")