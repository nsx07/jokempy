from random import randint
#   JOKEMPÔ GAME
#   Regras do jogo;
#                  1 =>Pedra: papel > pedra > tesoura
#                  2 =>Papel: tesoura > papel > pedra
#                  3 =>Tesoura: pedra > tesoura > papel
#---Modos_de_jogo------------------------------------------------------------------------------------------------------
print("Seja bem-vindo ao Jokempy\n")
print("   Modos de jogo;\n","1 - Humano vs Humano\n","2 - Humano vs PC\n","3 - PC vs PC\n","4 - Modo Bônus + Lagarto e Spock - Humano vs PC\n","0 - Se deseja parar de jogar.\n")
exit = 0
while exit != 1:
    modo = int(input("Digite o modo de jogo que gostaria: "))
#---Humano_vs_Humano---------------------------------------------------------------------------------------------------
    if modo == 1:
        saida1 = 1
        win1 = 0
        win2 = 0
        tie = 0
        while saida1 != 0:
            print("Você escolheu o modo Humano vs Humano\n")
            print("   Regras do jogo;\n","1 =>Pedra: papel > pedra > tesoura\n","2 =>Papel: tesoura > papel > pedra\n","3 =>Tesoura: pedra > tesoura > papel\n")
            print("   Opções de jogada;\n","1 - Pedra\n","2 - Papel\n","3 - Tesoura\n")
            jogada1 = int(input("Player 1! Digite aqui o número da sua jogada: "))
            jogada2 = int(input("Player 2! Digite aqui o número da sua jogada: "))
            if (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
                print("Player 1 Ganhou!\n")
                win1 = win1 + 1
            elif (jogada2 == 1 and jogada1 == 3) or (jogada2 == 2 and jogada1 == 1) or (jogada2 == 3 and jogada1 == 2):
                print("Player 2 Ganhou!\n")
                win2 = win2 + 1
            elif (jogada1 == jogada2 and (jogada1 and jogada2 in {1,2,3})):
                print("Empate.\n")
                tie = + 1
            elif (jogada1 or jogada2 != {1,2,3}):
                print("Ação inexistente. Tente novamente com jogadas entre 1 e 3.\n")
            #---Sair_Modo----------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            while sair != 0 and sair != 1:
                    print("Ação inexistente. Tente novamente com opções entre 0 e 1")
                    sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            if sair == 0:
                saida1 = 0
            elif sair == 1:
                continue  
        print('As estatísticas foram;\n','O jogador 1 ganhou:',win1,'\n','O jogador 2 ganhou:',win2,'\n','e houveram',tie,'empate(s)\n')
        print("-------------------------------------------")
#---Humano_vs_Computador----------------------------------------------------------------------------------------------- 
    elif modo == 2:
        print("Você escolheu o modo Humano vs PC\n")
        print("   Regras do jogo;\n","1 =>Pedra: papel > pedra > tesoura\n","2 =>Papel: tesoura > papel > pedra\n","3 =>Tesoura: pedra > tesoura > papel\n")
        print("   Opções de jogada;\n","1 - Pedra\n","2 - Papel\n","3 - Tesoura\n")
        saida2 = 1
        winPlayer = 0
        winPC = 0
        tie_humanPC = 0
        while saida2 != 0:
            human = int(input("Player! Digite aqui o número da sua jogada: "))
            pc = randint(1,3)
            print("PC jogou:",pc)
            if (human == 1 and pc == 3) or (human == 2 and pc == 1) or (human == 3 and pc == 2):
                print("Player Ganhou!\n")
                winPlayer = winPlayer + 1
            elif (pc == 1 and human == 3) or (pc == 2 and human == 1) or (pc == 3 and human == 2):
                print("PC Ganhou!\n")
                winPC = winPC + 1
            elif human == pc and ((human and pc) in {1,2,3}):
                print("Empate.\n")
                tie_humanPC = + 1
            elif (human or pc != [1,2,3]):
                print("Ação inexistente. Tente novamente com jogadas entre 1 e 3.\n")
            #---Sair_Modo----------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            while sair != 0 and sair != 1:
                    print("Ação inexistente. Tente novamente com opções entre 0 e 1")
                    sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            if sair == 0:
                break
            elif sair == 1:
                continue                  
        print('As estatísticas foram;\n','O Player ganhou:',winPlayer,'\n','O PC ganhou:',winPC,'\n','e houveram',tie_humanPC,'empate(s)\n')
        print("-------------------------------------------")
#---Computador_vs_Computador-------------------------------------------------------------------------------------------
    elif modo == 3:
        saida3 = 1
        win_pc1 = 0
        win_pc2 = 0
        tie_pcPc = 0
        while saida3 != 0:
            print("Você escolheu o modo PC vs PC\n")
            print("     Regras do jogo;\n","1 =>Pedra: papel > pedra > tesoura\n","2 =>Papel: tesoura > papel > pedra\n","3 =>Tesoura: pedra > tesoura > papel\n")
            pc1 = randint(1,3)
            pc2 = randint(1,3)
            print("A jogada do PC1 foi:",pc1)
            print("A jogada do PC2 foi:",pc2)
            if (pc1 == 1 and pc2 == 3) or (pc1 == 2 and pc2 == 1) or (pc1 == 3 and pc2 == 2):
                print("O PC-1 ganhou!\n")
                win_pc1 = win_pc1 + 1
            elif (pc2 == 1 and pc1 == 3) or (pc2 == 2 and pc1 == 1) or (pc2 == 3 and pc1 == 2):
                print("O PC-2 ganhou!\n")
                win_pc2 = win_pc2 + 1
            elif pc1 == pc2 and (pc1 and pc2) in {1,2,3}:
                print("Empate!")
                tie_pcPc = tie_pcPc + 1
            elif pc1 or pc2 != {1,2,3}:
                print("PC jogou sujo!!!\n")
            #---Sair_Modo----------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            while sair != 0 and sair != 1:
                    print("Ação inexistente. Tente novamente com opções entre 0 e 1")
                    sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            if sair == 0:
                break
            elif sair == 1:
                continue              
        print('As estatísticas foram;\n','O PC-1 ganhou:',win_pc1,'\n','O PC-2 ganhou:',win_pc2,'\n','e houveram',tie_pcPc,'empate(s)\n')
        print("-------------------------------------------")
#---MODO_BÔNUS---------------------------------------------------------------------------------------------------------
    elif modo == 4:
        print("Você escolheu o modo extra - Humano vs PC com adição de mais duas jogadas!!!\n")
        print("     Regras do jogo;\n","1 =>Pedra: papel > spock > |pedra| > tesoura > lagarto\n","2 =>Papel: tesoura > lagarto > |papel| > spock > pedra\n","3 =>Tesoura: spock > pedra > |tesoura| > lagarto > papel\n","4 =>Lagarto: pedra > tesoura > |lagarto| > papel > spock\n","5 =>Spock: lagarto > papel > |spock| > pedra > tesoura\n")
        print("     Opções de jogada;\n","1 - Pedra\n","2 - Papel\n","3 - Tesoura\n","4 - Lagarto\n","5 - Spock\n")
        saida2 = 1
        winPlayer = 0
        winPC = 0
        tie_humanPC = 0
        while saida2 != 0:
            human = int(input("Player! Digite aqui o número da sua jogada: "))
            pc = randint(1,5)
            print("PC jogou:",pc)
            if (human == 1 and (pc == 3 or pc == 4)) or (human == 2 and (pc == 5 or pc == 1)) or (human == 3 and (pc == 4 or pc == 2)) or (human == 4 and (pc == 2 or pc == 5)) or (human == 5 and (pc  == 1 or pc ==3)):
                print("Player Ganhou!\n")
                winPlayer = winPlayer + 1
            elif (pc == 1 and (human == 3 or human == 4)) or (pc == 2 and (human == 5 or human == 1)) or (pc == 3 and (human == 4 or human == 2)) or (pc == 4 and (human == 2 or human == 5)) or (pc == 5 and (human  == 1 or human ==3)):
                print("PC Ganhou!\n")
                winPC = winPC + 1
            elif human == pc and (human and pc) in {1,2,3,4,5}:
                print("Empate.\n")
                tie_humanPC = + 1
            elif (human or pc != [1,2,3,4,5]):
                print("Ação inexistente. Tente novamente com jogadas entre 1 e 3.\n")
                continue
            #---Sair_Modo----------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            while sair != 0 and sair != 1:
                print("Ação inexistente. Tente novamente com opções entre 0 e 1")
                sair = int(input("Se deseja sair do modo de jogo, digite '0'. Caso contrário, digite '1': \n"))
            if sair == 0:
                break
            elif sair == 1:
                continue                  
        print('As estatísticas foram;\n','O Player ganhou:',winPlayer,'\n','O PC ganhou:',winPC,'\n','e houveram',tie_humanPC,'empate(s)\n')
        print("-------------------------------------------")
#---Sair_do_Jogo--------------------------------------------------------------------------------------------------------
    else:
        if modo == 0:
            break
        elif modo != {1,2,3,4}:
            print("Ação inexistente. Escolha opções entre 0 e 4.")
            continue
