dia = int(input("Digite um numero de 1 a 7: "))

match dia:
    case 1:
        print("Seu dia é domingo")
    case 2:
        print("Seu dia é segunda")
    case 3:
        print("Seu dia é terça")
    case 4:
        print("Seu dia é quarta")
    case 5:
        print("Seu dia é quinta")
    case 6:
        print("Seu dia é sexta")
    case 7:
        print("Seu dia é sabado")
    case _:
        print("Valor invalido")

