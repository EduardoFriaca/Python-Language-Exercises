#Cálculo de bonus salarial
salario = float(input("Informe o salário: "))
tempo = int(input("Informe o tempo de trabalho: "))

if tempo >= 5:
    bonus= salario * 0.20
else:
    bonus= salario * 0.10

print("O valor do bonus é: %.2f" %(bonus))
print("O salário atualizado é: %.2f" %(salario + bonus))