while(True):
    valor1 = float(input("Insira a Nota 1: "))
    valor2 = float(input("Insira a Nota 2: "))
    valor3 = float(input("Insira a Nota 3: "))

    media = (valor1 + valor2 + valor3)/3

    print("A media calculada foi: ", media)
    opcao = int(input("Deseja continuar?\n1 = sim\n2 = não"))
    if opcao == 2:
        print("Encerrando...")
        break
    
