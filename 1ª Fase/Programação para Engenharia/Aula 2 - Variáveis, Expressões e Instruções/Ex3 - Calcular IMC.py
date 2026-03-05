print("Calculadora IMC")

peso = float(input("Digite seu peso em KGs: \n"))
altura = float(input("Digite sua altura em metros: \n"))

imc = peso/(altura**2)

print("Seu IMC é: ", imc)
