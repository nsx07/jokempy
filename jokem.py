from random import randint
#   JOKEMPÔ GAME
#   Regras do jogo;
#                  1 =>Pedra: papel > pedra > tesoura
#                  2 =>Papel: tesoura > papel > pedra
#                  3 =>Tesoura: pedra > tesoura > papel
#---Modos de jogo------------------------------------------------------------------------------------------------------
print("Seja bem-vindo ao Jokempy\n","Modos de jogo\n","1 - Humano vs Humano\n","2 - Humano vs PC\n","3 - PC vs PC\n")
print("0 - Se deseja parar de jogar qualquer modo.\n")
exit = 0
while exit != "desligar":
    modo = int(input("Digite o modo de jogo que gostaria: "))
#---Humano vs Humano---------------------------------------------------------------------------------------------------
    if modo == 1:
        saida1 = 0
        while saida1 != "sair":
            print("Você escolheu o modo Humano vs Humano\n")
            print("Opções de jogada;\n","1 - Pedra\n","2 - Papel\n","3 - Tesoura\n")
            jogada1 = int(input("Player 1! Digite aqui o número da sua jogada: "))
            jogada2 = int(input("Player 2! Digite aqui o número da sua jogada: "))
            if (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
                print("Player 1 Ganhou!\n")
            elif (jogada2 == 1 and jogada1 == 3) or (jogada2 == 2 and jogada1 == 1) or (jogada2 == 3 and jogada1 == 2):
                print("Player 2 Ganhou!\n")
            elif jogada1 == jogada2:
                print("Empate.\n")
            elif (jogada1 or jogada2 != [1,2,3]):
                print("Ação inexistente. Tente novamente com jogadas entre 1 e 3.\n")
            #---Sair
            sair = input("Se deseja sair do jogo, digite 'sair'. Caso contrário, pressione Enter: \n")
            if sair == "sair":
                saida1 = "sair"            
#---Humano vs Computador----------------------------------------------------------------------------------------------- 
    elif modo == 2:
        print("Você escolheu o modo Humano vs PC\n","Opções de jogada;\n","1 - Pedra\n","2 - Papel\n","3 - Tesoura\n")
        saida2 = 0
        while saida2 != 'sair':
            human = int(input("Player! Digite aqui o número da sua jogada: "))
            pc = randint(1,3)
            print("PC jogou:",pc)
            if (human == 1 and pc == 3) or (human == 2 and pc == 1) or (human == 3 and pc == 2):
                print("Player Ganhou!\n")
            elif (pc == 1 and human == 3) or (pc == 2 and human == 1) or (pc == 3 and human == 2):
                print("PC Ganhou!\n")
            elif human == pc:
                print("Empate.\n")
            elif (human or pc != [1,2,3]):
                print("Ação inexistente. Tente novamente com jogadas entre 1 e 3.\n")
            sair = input("Se deseja sair desse modo, digite 'sair'. Caso contrário pressione Enter: \n")
            if sair == "sair":
                saida2 = "sair"
#---Computador vs Computador-------------------------------------------------------------------------------------------
    elif modo == 3:
        saida3 = 0
        while saida3 != "sair":
            print("Você escolheu o modo PC vs PC\n")
            pc1 = randint(1,3)
            pc2 = randint(1,3)
            print("A jogada do PC1 foi:",pc1)
            print("A jogada do PC2 foi:",pc2)
            if (pc1 == 1 and pc2 == 3) or (pc1 == 2 and pc2 == 1) or (pc1 == 3 and pc2 == 2):
                print("O PC 1 ganhou!\n")
            elif (pc2 == 1 and pc1 == 3) or (pc2 == 2 and pc1 == 1) or (pc2 == 3 and pc1 == 2):
                print("O PC 2 ganhou!\n")
            elif pc1 == pc2:
                print("Empate!")
            elif pc1 or pc2 != {1,2,3}:
                print("PC jogou sujo!!!\n")
            sair = input("Se deseja sair do jogo, digite 'sair'. Caso contrário, pressione Enter: \n")
            if sair == "sair":
                saida2 = "sair"
#---Sair do Jogo--------------------------------------------------------------------------------------------------------
    elif modo  == 0:
        exit = "desligar"
    else:
        print("Ação inexistente. Escolha opções entre 0 e 3.")
