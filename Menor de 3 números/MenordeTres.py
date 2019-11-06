
input("Programa que retorna o menor de 3 números, digite alguma tecla para iniciar.")
sair = False
while sair == False:
        print("\n")
        numeros = [input(f'Informe o {x+1}º número: ') for x in range(3)]
        if all(str.isdigit(x) for x in numeros):
            print("O menor número é: " + min(numeros))
            respostaSaida = input("Deseja sair? S/N: ")
            if respostaSaida in ["S","s"]:
                sair = True
        else:
            print("Um ou mais dos valores informados não é um número inteiro")
