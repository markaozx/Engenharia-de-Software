x = int(input("Digite o numero 1:"))
y = int(input("Digite o numero 2:"))

if x > y:
    print(f"{x} é maior que {y}")
elif y > x:
    print(f"{y} é maior que {x}")
elif x == y:
    print("os valores são iguais")
