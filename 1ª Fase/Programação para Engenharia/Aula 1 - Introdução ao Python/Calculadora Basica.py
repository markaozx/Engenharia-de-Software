x = 1
while(x):
    print("--- MENU DE OPÇÕES ---")
    print("1 - Adição \n2 - Subtraçã \n3 - Multiplicação \n4 - Divisão")
    operacao = int(input('Operação escolhida: '))
    if operacao == 1:
        n1 = int(input('Valor 1:'))
        n2 = int(input('Valor 2:'))
        R = n1 + n2
        print('A resposta da adição é: ',R)
    elif operacao == 2:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
        R = n1 - n2
        print('A resposta da subtração é: ', R)
    elif operacao == 3:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
        R = n1 * n2
        print('A resposta da multiplicação é: ', R)
    elif operacao == 4:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
        R = n1 / n2
        print('A resposta da divisão é: ', R)
    else:
        print('Operação invalida')
    escolha=int(input('Deseja continuar:\n1 - Continuar\n2 - Fechar\nEscolha: '))
    if escolha == 2:
        print('Encerrando o programa...')
        x = 0
        
