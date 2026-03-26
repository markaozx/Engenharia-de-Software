print("--- MENU DE OPÇÕES ---\nG - GASOLINA\nA - ALCOOL")
x = input("escolha uma opção: ").lower()
match x:
    case "g":
        l = float(input("Digite a litragem desejada: "))
        total = l * 5.57
        if l <= 20:
            #4%
            desc = total - (total * 0.04)
            print(f"O total com desconto ficou: {desc} ")
        elif l > 20:
            #6%
            desc = total - (total * 0.06)
            print(f"O total com desconto ficou: {desc} ")
    case "a":
        l = float(input("Digite a litragem desejada: "))
        total = l * 4.98
        if l <= 20:
            #2%
            desc = total - (total * 0.02)
            print(f"O total com desconto ficou: {desc} ")
        elif l > 20:
            #5%
            desc = total - (total * 0.05)
            print(f"O total com desconto ficou: {desc} ")
    case _ :
        print("Opção invalida")
            
