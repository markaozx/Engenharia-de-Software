n1 = float(input("insira sua nota: "))
n2 = float(input("insira sua nota: "))
n3 = float(input("insira sua nota: "))

nota = (n1 + n2 + n3)/3

if nota >= 7:
    print("Parabéns! Sua média é alta")
elif nota < 7 and nota >= 5:
    print("Sua média é razoável")
elif nota < 5:
    print("Sua média é baixa. É uma boa oportunidade para melhorar")
