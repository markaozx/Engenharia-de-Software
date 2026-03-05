valor = float(input("Valor do produto: "))
desconto = (valor/100) * 20
preco = valor - desconto

print("Voce ganhou R$",desconto," de desconto, o total ficou: ", preco)
