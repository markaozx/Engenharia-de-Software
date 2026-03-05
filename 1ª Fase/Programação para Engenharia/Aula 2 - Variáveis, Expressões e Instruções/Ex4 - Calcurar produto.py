print("Calculadora de compra")

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitario do produto: "))
quant = float(input("Digite a unidade do produto: "))

total = preco * quant
print("Sua compra do ", nome," ficou um total de: ", total)
