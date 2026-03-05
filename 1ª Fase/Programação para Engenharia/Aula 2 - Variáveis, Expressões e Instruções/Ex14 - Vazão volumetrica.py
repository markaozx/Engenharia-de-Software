diametro = float(input("Diametro do tubo em M: "))
vel = float(input("Velocidade do fluido (m/s): "))

A = (3.14 * diametro**2)/4
Q = A * vel

print("A vazão volumetrica do fluido é: ", Q)
