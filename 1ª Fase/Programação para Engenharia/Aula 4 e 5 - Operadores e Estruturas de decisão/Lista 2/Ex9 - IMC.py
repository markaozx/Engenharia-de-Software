kg = float(input("Insira seu peso em kg: "))
alt = float(input("Inisira sua altura em m: "))

imc = kg / (alt * alt)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrpeso")
elif imc >= 30:
    print("Obesidade")
    
