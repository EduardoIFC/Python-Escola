notasNum = int(input("quantas notas deseja inserir? "))
notasSomadas = 0

for i in range(notasNum):
    nota = int(input(f"Digite a nota {i + 1}: (0 a 100): "))
    if nota < 0 or nota > 100:
        print("Nota inválida. Deve ser entre 0 e 100.")
    else:
        notasSomadas += nota

media = notasSomadas / notasNum
print(f"Média: {media}")
if media >= 60:
    print("Aprovado")
else:
    print("Reprovado")