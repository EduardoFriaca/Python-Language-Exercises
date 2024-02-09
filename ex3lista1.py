salariominimo = float(input("Digite o salário mínimo:"))
qtdidade = float(input("Digite o total de água consumida no mês:"))

#Cálculos a se fazer

porcentagem = (qtdidade/1000)*0.02
valorpago = porcentagem * salariominimo

#Resultado do calculo
print("O valor da conta de água é de", valorpago)

#Desconto
totalcomdesconto = valorpago*0.85
print("O valor a ser pago com o desconto de 15% é de", totalcomdesconto)
