import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("qual nivel de dificuldade?")
    print("(1) facil (2) médio (3) dífícil")

    nivel = int(input("define o nivel:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_ss = input("Digite o seu numero: ")
        print("você digitou ", chute_ss)
        chute = int(chute_ss)

        if(chute < 1 or chute > 100):
            print("vocẽ deve digitar um numero de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou! você fez {} pontos".format(pontos))
            break
        else :
            if(maior) :
                print("Você errou! Chutou alto")
            elif(menor) :
                print("Você errou! Chutou baixo")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()