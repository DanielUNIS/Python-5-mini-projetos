
def CalcularIdade(x):
    x = int(x)
    return str(int(x/365)) + " ano(s) ou " + str(int(x/30)) + " mes(es) ou " + str(x) + " dia(s)." 

input("Programa que retorna a idade em anos, meses e dias, digite alguma tecla para iniciar.")
sair = False
while sair == False:
        dias = input("\nInforme sua idade em dias: ")
        if str.isdigit(dias):
            print("Sua idade pode ser lida como: " + CalcularIdade(dias))
            respostaSaida = input("Deseja sair? S/N: ")
            if respostaSaida in ["S","s"]:
                sair = True
        else:
            print("Valor informado não é um número")
