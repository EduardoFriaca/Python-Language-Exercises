import math

area = float(input("Digite o tamanho em metros quadrados de area a ser pintado"))
litrostinta =  area / 3
latas = litrostinta / 18
qtda_latas = math.ceil(latas)


preco = qtda_latas * 80

print("Quantidade de latas:", qtda_latas)
print("Preço total:", preco)
