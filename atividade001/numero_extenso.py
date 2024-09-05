#numero por extenso
def numero_extenso(numero):
    '''
    Transforma o número de formato numeríco para extenso
    '''
    if numero>99 or numero<1:
        print("O número deve ser maior que 1 e menor que 99")
    else:
        dicionario_numeros = {
            0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
            6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
            11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze",
            16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte",
            30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta",
            80: "oitenta", 90: "noventa"
            }
        if numero<=20:
            print(dicionario_numeros[numero])
        else:
            dezena = (numero // 10) * 10
            unidade = numero % 10
            if unidade == 0:
                print(dicionario_numeros[dezena])
            else:
                print(f"{dicionario_numeros[dezena]} e {dicionario_numeros[unidade]} ")

numero = int(input("Digite um número até no formato numérico: "))
numero_extenso(numero)
