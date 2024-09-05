import random

lista_de_numeros = []
qntd_1 = qntd_2 = qntd_3 = qntd_4 = qntd_5 = qntd_6 = 0

def gerador_numeros():
    for i in range(100):
        numero = random.randint(1,6)
        lista_de_numeros.append(numero)

def qntd_repetidas(lista_de_numeros):
    qntd_1 = qntd_2 = qntd_3 = qntd_4 = qntd_5 = qntd_6 = 0
    for numero in lista_de_numeros:
        if numero == 1:
            qntd_1 += 1
        if numero == 2:
            qntd_2 += 1
        if numero == 3:
            qntd_3 += 1
        if numero == 4:
            qntd_4 += 1
        if numero == 5:
            qntd_5 += 1
        if numero == 6:
            qntd_6 += 1 

    print("A qunantidade de vezes que o número 1 do dado se repete: ", qntd_1)
    print("A qunantidade de vezes que o número 2 do dado se repete: ", qntd_2)
    print("A qunantidade de vezes que o número 3 do dado se repete: ", qntd_3)
    print("A qunantidade de vezes que o número 4 do dado se repete: ", qntd_4)
    print("A qunantidade de vezes que o número 5 do dado se repete: ", qntd_5)
    print("A qunantidade de vezes que o número 6 do dado se repete: ", qntd_6)

gerador_numeros()
qntd_repetidas(lista_de_numeros)