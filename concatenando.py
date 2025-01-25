def frase():
    str1 = input("\033[mDigite uma palavra: ")
    str2 = input("Digite a segunda palavra: ")

    print("Sua frase foi: ",str1,str2,".")
    veirifica()

def veirifica():
    print("Para continuar digite 1 ou 0 para sair.")
    seguir = input("Deseja continuar? \033[1;31m")

    if seguir == "1":
        frase()
    elif seguir == "0":
        print("\033[m*"*20,"\033[0;32mPrograma encerrado!\033[m","*"*20,"\n")
    else:
        print("\033[1;32m Digite uma opção válida!\033[m")
        veirifica()

print("Vamos formar uma pequna frase de duas palavras!")
print("\033[32m-"*48+"\033[m\n")

frase()