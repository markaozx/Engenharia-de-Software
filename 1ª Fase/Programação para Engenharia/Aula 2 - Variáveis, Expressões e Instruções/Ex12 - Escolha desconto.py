valor = float(input("Valor produto:  "))
x = float(input("Valor do desconto (0-100, sem %): "))
desc = (valor/100) * x
preco = valor - desc
print("O preo com desconto de ", x,"% fica: ",preco)
