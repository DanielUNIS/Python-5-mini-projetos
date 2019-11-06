import re

input("Inversor de palavras em uma frase. Pressione qualquer tecla para continuar")
sair = False
while sair == False:
        frase =(input("\nDigite uma frase: ")).strip()
        if re.search("[a-zA-z]",frase) and frase.find(" ")!=-1:
            print("Sua frase com as palavras invertidas é: " + " ".join([x[::-1] for x in frase.split(" ")]))
            respostaSaida = input("Deseja sair? S/N: ")
            if respostaSaida in ["S","s"]:
                sair = True
        else:
            print("Valor informado não é uma frase")
