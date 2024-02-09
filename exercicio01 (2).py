alunos = int(input("Quantidade de Alunos: "))
cont = 1
somaMedias = 0.0
while cont <= alunos:
  print(f"Aluno #{cont}")
  p1 = float(input("Nota P1: "))
  p2 = float(input("Nota P2: "))
  media = (p1 + p2) / 2
  if media >= 7.0:
    print("    Aprovado direto!")
  somaMedias += media # somaMedias = somaMedias + media
  cont += 1 # cont = cont + 1
mediaGeral = somaMedias / alunos
print(f"Média Geral = {mediaGeral:.1f}")