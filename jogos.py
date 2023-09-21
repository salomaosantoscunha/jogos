import Foca
import  Jogo_adivinhacao

def escolha_jogos():


    print("----------------------------------")
    print("---------Escolha seu jogo---------")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo ?"))

    if(jogo == 1 ):
        print("Jogando forca")
        Foca.jogar_forca()
    elif(jogo == 2):
     print("jogando adivinhação ")
Jogo_adivinhacao.jogar_adivinhacao()

  if(__name__ =="__main__"):
     escolha_jogos()