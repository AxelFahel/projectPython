'''
Code projeto curso data science academy
'''

import random

palavras = ["python", "programacao", "computador", "jogos", "internet"]
palavra = random.choice(palavras)
letras_erradas = []
letras_certas = []
tentativas = 6

print("Adivinhe a palavra secreta!")
print("A palavra tem", len(palavra), "letras.")
print(len(palavra) * "-")

while True:
    letra = input("Digite uma letra: ")

    if letra in letras_certas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente novamente.")

    elif letra in palavra:
        letras_certas.append(letra)
        print("Parabéns! A letra", letra, "está na palavra.")
        # Mostra a palavra com as letras certas adivinhadas até agora
        palavra_mostrada = ""
        for letra_palavra in palavra:
            if letra_palavra in letras_certas:
                palavra_mostrada += letra_palavra
            else:
                palavra_mostrada += "-"
        print(palavra_mostrada)

        if palavra_mostrada == palavra:
            print("Parabéns, você ganhou!")
            break

    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("A letra", letra, "não está na palavra. Você perdeu uma tentativa. Restam", tentativas, "tentativas.")

        # Desenha o boneco da forca
        partes_do_corpo = ["O", "|", "/", "\\", "/", "\\"]
        boneco_da_forca = ""
        for i in range(tentativas):
            boneco_da_forca += partes_do_corpo[i]
        print(boneco_da_forca)

        if tentativas == 0:
            print("Você perdeu! A palavra era", palavra)
            break