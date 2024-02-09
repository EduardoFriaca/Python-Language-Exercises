def CelsiusToFahrenheit(celsius):
    fahrenheit = (9/5)*celsius + 32
    return fahrenheit

def TabelaDeTemperatura(minimo, maximo, espacamento=5):
    print("Celsius  Fahrenheit")
    for celsius in range(minimo, maximo+1, espacamento):
        fahrenheit = CelsiusToFahrenheit(celsius)
        print(f"{celsius} °C\t{fahrenheit:.2f} °F")

# Exemplo de uso
minimo = int(input("Digite o valor mínimo em graus Celsius: "))
maximo = int(input("Digite o valor máximo em graus Celsius: "))
espacamento = input("Digite o espaçamento entre os valores (é opcional, se nada for inserido o padrão é 5): ")
if espacamento == "":
    TabelaDeTemperatura(minimo, maximo)
else:
    TabelaDeTemperatura(minimo, maximo, int(espacamento))
