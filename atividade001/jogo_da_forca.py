#jogo da forca
import random
import sys
caminho_arquivo = sys.argv[1]

def escolher_palavra():
    """
    Abre o arquivo e escolhe uma palavra aleatória.
    """
    with open(caminho_arquivo, "r", encoding="UTF-8") as arquivo:
        palavras = [palavra.strip().lower() for palavra in arquivo.readlines()]

    escolhido = random.choice(palavras)
    return escolhido

def jogo(escolhido):
    """
    Inicia o jogo da forca com a palavra escolhida.
    """
    letras_escolhido = len(escolhido)
    palavra_oculta = ["_"] * letras_escolhido
    print(f"Jogo da Forca: \nSua palavra tem {letras_escolhido} letras! \nVocê tem 6 chances.")

    erros = 0
    letras_erradas = []

    while erros < 6 and "_" in palavra_oculta:
        print(" ".join(palavra_oculta))  # Mostra a palavra oculta com as letras adivinhadas
        tentativa = input("Escolha uma letra: \n").lower()

        if tentativa in escolhido:
            print(f"A letra {tentativa} está na palavra!")
            for i in range(letras_escolhido):
                if escolhido[i] == tentativa:
                    palavra_oculta[i] = tentativa  #Substitui o _pela letra correta
        else:
            if tentativa not in letras_erradas:
                erros += 1
                letras_erradas.append(tentativa)
                print(f"A letra {tentativa} não está na palavra. Você ainda tem {6 - erros} chances.")
            else:
                print(f"Você já tentou a letra {tentativa} antes. Tente outra.")

    if "_" not in palavra_oculta:
        print(f"Parabéns! Você adivinhou a palavra: {escolhido}")
    else:
        print(f"Você foi enforcado! A palavra era: {escolhido}")



palavra_escolhida = escolher_palavra()
jogo(palavra_escolhida)
