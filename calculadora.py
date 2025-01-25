print("\033[1;33mVamos calcular!\033[m\n")

continuar = 1
while continuar != 0:
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))

    while True:
        print("Digite a operação desejada\n + Adição\n- Subtração\n/ Divisão\n* Multiplicação")
        op = input("Digite a operação: ")
        if op == "+":
            print(f"O resultado da Adição é: {n1+n2}")
            break
        elif op == "/":
            print(f"O resultado da Divisão é: {n1/n2}")
            break
        elif op == "-":
            print(f"O resultado da Subtração é: {n1-n2}")
            break
        elif op == "*":
            print(f"O resultado da Multiplicação é: {n1*n2}")
            break
        else:
            print("Digite uma operação válida")
    continuar = int(input("Deseja continuar? 1-Sim 0- SAIR"))
print("\033[1;31mPrograma encerrado\033[m")

