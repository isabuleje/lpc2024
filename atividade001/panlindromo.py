#panlidromo

def verificacao_panlidromo(palavra):
    """
    Verifica se a palavra é um panlídromo ou não
    """
    palavra = palavra.lower().replace(" ", "")
    palavra_contrario = ''.join(reversed(palavra))
    if palavra == palavra_contrario:
        print(f"{palavra} é um panlídromo!")
    else:
        print(f"{palavra} não é um panlídromo!")


palavra = str(input("Digite uma palavra: "))
verificacao_panlidromo(palavra)
