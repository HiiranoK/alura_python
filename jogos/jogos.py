import forca
import jogo_adivinha

def escolhe_o_jogo():
    print("*********************************")
    print("*****Escolha entre os jogos!*****")
    print("*********************************")


    validacao = False

    print("(1) Forca (2) Adivinhação")
    while(validacao != True):
        jogo = int(input("Informe o nº do jogo que deseja iniciar."))
        if( jogo < 1 or jogo > 2):
            print("Opção inválida, tente novamente") 
        elif( jogo == 1):
            forca.main()
            validacao = True
        else:
            jogo_adivinha.jogar()
            validacao = True

if(__name__=="__main__"):   # esse comando compara se a váriável name tem o mesmo valor da variável main.
    escolhe_o_jogo()                 # a variável name só recebe esse valor, caso o arquivo seja executado, ou seja, o resultado é falso ao usar o import.1