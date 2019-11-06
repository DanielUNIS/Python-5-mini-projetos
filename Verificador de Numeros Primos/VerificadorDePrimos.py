def VerificadorPrimos(x):
    x = int(x)
    return x>1 and all(x%i!=0 for i in range(2,x))

input("Verificar de números primos, digite qualquer tecla para iniciar")
sair = False
while sair == False:
        numero = input("\nInforme um número: ")
        if str.isdigit(numero):
            print("O número informado é primo" if VerificadorPrimos(numero) else "O número informado não e primo")
            respostaSaida = input("Deseja sair? S/N: ")
            if respostaSaida in ["S","s"]:
                sair = True
        else:
            print("Valor informado não e um número")

