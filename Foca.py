import random


def jogar_forca ():
    print("--------------------------")
    print("bem vindo ao Jogo de Forca ")
    print("--------------------------")
    print(3//2)
    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas =0
    pontos = 1000


    print("Qaul nivel e dificulpade?")
    print("(1) facil (2) médio (3) dificil")
    nivel = int(input("Definir o nivel: "))
    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 2

    #while(rodada <= total_de_tentativas):
    # print("Tentativas ", rodada, "de", total_de_tentativas)
    for rodada in range(1,total_de_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu Numero:")
        print ("Voçê digitou " , chute_str)
        chute =int (chute_str)

        if(chute < 1 or chute > 100):
            print("Voçê deve digitar um numero entre 1 e 100 !")
            continue


        acertou = chute == numero_secreto
        errou_para_mais = chute > numero_secreto
        errou_para_menos = chute < numero_secreto

        if(acertou):
            print("Parabens!!! e fez {} pontos !".format(pontos))
            break
        else:
            if(errou_para_mais):
                print("Voçê quase acertou foi acima do n° !")
            elif (errou_para_menos):
                print("Voçê quase acertou foi abaixo do n° !")
            pontos_perdido = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdido


    print("-----------------------------------")
    print("FIM DO JOGO !")
if(__name__== "__main__"):
    jogar_forca()