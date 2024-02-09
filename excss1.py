dias = int(input("Quantos dias você vai ficar no hospital:"))
quarto = input("Qual o tipo de quarto? ")
wifi = input("Foi utilizado o Wifi? ")
tv = input("Foi utilizado TV a cabo? ")
diaria = 0
total = 0
custotv = 0
custowifi = 0

if quarto == "Particular" or quarto == "particular":
    diaria = 360*dias
elif quarto == "Semi-particular" or quarto == "semi-particular":
    diaria = 210*dias
else:
    diaria = 185*dias
if tv == "Sim" or tv == "sim":
    custotv = 4
if wifi == "Sim" or wifi == "sim":
    custowifi = 3
total = diaria + custotv + custowifi
print("Número de dias:", dias)
print("Tipo de quarto:", quarto)
print("Diaria:", diaria)
print("Wifi:", custowifi)
print("TV a cabo:", custotv)
print("TOTAL:", total)


    
