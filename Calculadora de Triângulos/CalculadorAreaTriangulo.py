import re

def CalcularArea(lados):
    lados.sort()
    s = 0
    if lados[2] >= lados[0] + lados[1]:
        return "Os lados informados não formam um triângulo"
    else:
        s =sum(lados)/2
        area = round((s*(s-lados[2])*(s-lados[1])*(s-lados[0])) ** 0.5, 2)
        return "A area desse triângulo é igual a " + str(area) 

input("Calculadora de área de triângulos, digite alguma tecla para iniciar.")
print("OBS: Informe apenas números positivos e  inteiros")
sair = False
while sair == False:
        a = input("\nInforme o primeiro lado: ")
        b = input("Informe o segundo lado: ")
        c = input("Informe o último lado: ")
        lados = [a,b,c]
        if all(re.search("[1-9]",x) and x.isdigit() for x in lados):
            print(CalcularArea([int(x) for x in lados]))
            respostaSaida = input("Deseja sair? S/N: ")
            if respostaSaida in ["S","s"]:
                sair = True
        else:
            print("Um ou mais dos valores informados não são números ou são vazios.")
