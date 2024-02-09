altura = float(input("Digite a altura em centímetros: "))
sexo = int(input("Digite o sexo (0 = masc, 1 = fem, -1 para sair): "))

total_altura = altura
num_mulheres = 0
num_homens = 0
soma_altura_mulheres = 0

if sexo != -1:
    maior_altura = altura
    menor_altura = altura
else:
    print("Nenhum dado foi inserido.")
    exit()

while sexo != -1:
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    if sexo == 1: #se sexo for feminino, atualiza média de altura das mulheres
        num_mulheres += 1
        soma_altura_mulheres += altura
    else: #se sexo for masculino, incrementa contador de homens
        num_homens += 1

    altura = float(input("Digite a altura em centímetros: "))
    sexo = int(input("Digite o sexo (0 = masc, 1 = fem, -1 para sair): "))

    total_altura += altura

if num_mulheres != 0:
    media_altura_mulheres = soma_altura_mulheres / num_mulheres
    print("Média de altura das mulheres: %.2f cm" % media_altura_mulheres)
else:
    print("Nenhuma mulher foi registrada.")

if num_homens + num_mulheres != 0:
    media_altura_populacao = total_altura / (num_homens + num_mulheres)
    print("Média de altura da população: %.2f cm" % media_altura_populacao)
else:
    print("Nenhum dado foi inserido.")

if num_homens + num_mulheres != 0:
    percentual_homens = num_homens / (num_homens + num_mulheres) * 100
    print("Percentual de homens na população: %.2f%%" % percentual_homens)
else:
    print("Nenhum dado foi inserido.")

print("Maior altura encontrada: %.2f cm" % maior_altura)
print("Menor altura encontrada: %.2f cm" % menor_altura)
