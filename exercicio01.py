tempo = int(input("Tempo em segundos: "))
hora = tempo // 3600
tempo = tempo % 3600
minuto = tempo // 60
segundo = tempo % 60
print(f"{hora}h {minuto}m {segundo}s")