t = float(input("Digite o valor da tensao (V) em volts: "))
c = float(input("Digite o valor da corrente (I) em amperes: "))
r = float(input("Digite o valor da resistencia (R) em ohms: "))

tensao = c * r
diferenca = abs(tensao - t)/t*100

if diferenca <= 1:
    print("O componente obedece a lei de Ohm.")
else:
    print("O componente não obedece a lei de Ohm.")
