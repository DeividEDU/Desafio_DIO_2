def prog():
    try:
        palavra = input("Digite uma palavra: ")
        repeticao = int(input("Digite um número inteiro: "))
        return palavra, repeticao
    except ValueError:
        print("\033[1;31mErro: Digite um número inteiro válido.\033[m")
        return prog()

print("Repetidor de palavras!\n", "+" * 22, "\n")

while True:
    palavra, repeticao = prog()
    print("\nO resultado foi:")
    print((palavra + " ") * repeticao)
    
    continuar = input("\nDeseja repetir? Digite 's' para sim ou qualquer outra tecla para sair: ")
    if continuar.lower() != 's':
        print("\033[1;32mPrograma encerrado!\033[m")
        break



