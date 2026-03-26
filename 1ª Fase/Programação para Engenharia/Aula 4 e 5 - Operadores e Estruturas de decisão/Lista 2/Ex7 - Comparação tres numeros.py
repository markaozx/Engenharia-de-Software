x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))
z = float(input("Digite outro numero: "))

if x > z and x > y:
    print(f"{x} é o maior")
elif z > y and z > x:
    print (f"{z} é o maior")
elif y > x and y > z:
    print ("f{y} [e o maior")
elif x == y or x == z or z == y:
    print ("existem dois numero iguais")
    

