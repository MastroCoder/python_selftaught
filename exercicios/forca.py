import random
import string
import os

def forca(palavra):
    erros = 0
    ganhou = False
    estagios = ["",
                "________         ",
                "|                ",
                "|       |        ",
                "|       0        ",
                "|      /|\       ",
                "|      / \       ",
                "|                "
                ]
    palavra = palavra.upper()
    letras = list(palavra)
    tabuleiro = ["__"] * len(palavra)
    lerros = []
    print("JOGO DA FORCA")
    print("\n")
    print(" ".join(tabuleiro))
    while erros < len(estagios) -  1:
        
        print("\n")
        palpite = input("Insira uma letra: ")
        palpite = palpite.upper()
         
        if palpite in letras:
            indice_acerto = letras.index(palpite)
            tabuleiro[indice_acerto] = palpite
            letras[indice_acerto] = "#" # caractere aleatório para não repetir
        elif len(palpite) > 1:
            print("Insira somente caracteres únicos!")
        else:
            lerros.append(palpite)
            erros += 1

        print("\nLETRAS ERRADAS:\n")
        print(" - ".join(lerros))
        print("\n")
        print(" ".join(tabuleiro))
        
        # variável para usar o fatiamento
        e = erros + 1
        print("\n".join(estagios[0: e]))

        if "__" not in tabuleiro:
              print("VITÒRIA!")
              print(" ".join(tabuleiro))
              ganhou = True
              break
            
    if not ganhou:
        print("\n".join(estagios[0: erros]))
        print("\nDERROTA. A PALAVRA ERA {}".format(palavra))

l = ["Chatoyant", "Bungalow", "Ephemeral", "Serendipity", "Idyllic", "Lullaby",
     "Nefarious", "Pristine", "Quintessence", "Sanguine", "Syzygy",
     "Werewithal"]
i = random.randint(0, len(l))
forca(l[i])    
