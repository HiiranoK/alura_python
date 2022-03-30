import random
from tracemalloc import stop
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto= random.randrange(1,101)

    pontos = 500
    tentativas = 5
    print("Selecione a dificuldade entre 1 e 3 ")
    print("1 = fácil, 2 = intermediário, 3 = difícil")

    while(True):
        dificuldade = int(input("digite o nº correspondente ao nível: "))
        if(dificuldade < 1 or dificuldade > 3):
            print("O numero informado é inválido, tente novamente")
            continue
        
        if(dificuldade == 1):
            tentativas = 15
            break
        elif(dificuldade == 2):
            tentativas = 10
            break
        else:
            tentativas = 5
            break

    for rodada in range(1,tentativas + 1):

        print("tentativa {0} de {1}".format(rodada,tentativas))
        chute = int(input("digite um numero entre 1 e 100: "))

        if (chute > 100 or chute < 1):
            print("seu numero é inválido, tente com um numero entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou, sua pontuação é {} pontos.".format(pontos))
            break
        else:
            if(maior):
                print("O numero {} é maior que a resposta".format(chute))
                if(rodada == tentativas):
                    print("O numero secreto era {}. você fez {} pontos.".format(numero_secreto,pontos))
            elif(menor):
                print("O numero {} é menor que a resposta".format(chute))
                if(rodada == tentativas):
                    print("O numero secreto era {}. você fez {} pontos.".format(numero_secreto,pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
    print("Fim do Jogo.")

if(__name__=="__main__"):   # esse comando compara se a váriável name tem o mesmo valor descrito em main.
    jogar()                 # a variável name só recebe esse valor, caso o arquivo seja executado, ou seja, o resultado é falso ao usar o import.