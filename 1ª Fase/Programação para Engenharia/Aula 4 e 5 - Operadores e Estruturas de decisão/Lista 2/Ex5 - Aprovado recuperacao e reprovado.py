nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aluno aprovado")
elif nota < 7 and nota >= 5:
    print("Aluno em recuperação")
elif nota < 5:
    print("Aluno reprovado")
