import random

def main():

    imprime_mensagem_inicial()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta] #cria uma série de "_" na mesma quantidade de caracteres da palavra secreta.
    print(letras_acertadas)

    #condições para encerramento do jogo.
    enforcou = False 
    acertou = False
    erros = 0

    #enquanto (True e True)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta,chute,letras_acertadas)  
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da forca***!")
    print("*********************************")

def carregar_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra 
        index += 1   

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__=="__main__"):   # esse comando compara se a váriável name tem o mesmo valor da variável main.
    main()                 # a variável name só recebe esse valor, caso o arquivo seja executado, ou seja, o resultado é falso ao usar o import.