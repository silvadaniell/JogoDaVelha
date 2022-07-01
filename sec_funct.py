import re

def positions(assistant):
    if assistant == 1:
        return 0,0
    elif assistant == 2:
        return 0,1
    elif assistant == 3:
        return 0,2
    elif assistant == 4:
        return 1,0
    elif assistant == 5:
        return 1,1
    elif assistant == 6:
        return 1,2
    elif assistant == 7:
        return 2,0
    elif assistant == 8:
        return 2,1
    elif assistant == 9:
        return 2,2

def jogo_velha(tabuleiro):
    i = 0
    j = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "":
                print("- ", end="")
            else:
                print(str(tabuleiro[i][j])+" ", end="")
        print("\n", end="")
    print("\n")
        
def test_winner(tabuleiro):
    #linhas
    if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X":
        return "X"
    elif tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X":
        return "X"
    elif tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X":
        return "X"
        
    #diagonais
    elif tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
        return "X"
    elif tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
        return "X"
        
    #colunas
    elif tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
        return "X"
    elif tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
        return "X"
    elif tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
        return "X"
    
    #linhas
    if tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O":
        return "O"
    elif tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O":
        return "O"
    elif tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O":
        return "O"
        
    #diagonais
    elif tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O":
        return "O"
    elif tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
        return "O"
        
    #colunas
    elif tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O":
        return "O"
    elif tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O":
        return "O"
    elif tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O":
        return "O"
    elif tabuleiro[0][0] != "" and tabuleiro[0][1] != "" and tabuleiro[0][2] != "" and tabuleiro[1][0] != "" and tabuleiro[1][1] != ""\
        and tabuleiro[1][2] != "" and tabuleiro[2][0] != "" and tabuleiro[2][1] != "" and tabuleiro[2][2] != "":
            return "EMPATE"
    
        
def user_play(tabuleiro):
    jogada = int(input("Digite o valor correspondente a posicao: "))
    while 1 > jogada or jogada > 9:
        print("JOGADA INVALIDA!")
        jogada = int(input("Digite o valor correspondente a posicao: "))
    while tabuleiro[positions(jogada)[0]][positions(jogada)[1]] != "":
        print("JOGADA INVALIDA!")
        jogada = int(input("Digite o valor correspondente a posicao: "))
    return jogada










"""def test_possibilit(tabuleiro, x, ia):
    if tabuleiro[0][0] == x and tabuleiro[1][1] == x and tabuleiro[2][2] == "":
        tabuleiro[2][2] = ia
    elif tabuleiro[2][2] == x and tabuleiro[1][1] == x and tabuleiro[0][0] == "":
        tabuleiro[0][0] = ia
    elif tabuleiro[2][2] == x and tabuleiro[0][0] == x and tabuleiro[1][1] == "":
        tabuleiro[1][1] = ia
    #
    elif tabuleiro[0][0] == x and tabuleiro[1][0] == x and tabuleiro[2][0] == "":
        tabuleiro[2][0] = ia
    elif tabuleiro[2][0] == x and tabuleiro[1][0] == x and tabuleiro[0][0] == "":
        tabuleiro[0][0] = ia
    elif tabuleiro[0][0] == x and tabuleiro[2][0] == x and tabuleiro[1][0] == "":
        tabuleiro[1][0] = ia
    #
    elif tabuleiro[0][0] == x and tabuleiro[0][1] == x and tabuleiro[0][2] == "":
        tabuleiro[0][2] = ia
    elif tabuleiro[0][2] == x and tabuleiro[0][1] == x and tabuleiro[0][0] == "":
        tabuleiro[0][0] = ia
    elif tabuleiro[0][0] == x and tabuleiro[0][2] == x and tabuleiro[0][1] == "":
        tabuleiro[0][1] = ia
    #
    elif tabuleiro[2][0] == x and tabuleiro[2][1] == x and tabuleiro[2][2] == "":
        tabuleiro[2][2] = ia
    elif tabuleiro[2][2] == x and tabuleiro[2][1] == x and tabuleiro[2][0] == "":
        tabuleiro[2][0] = ia
    elif tabuleiro[2][0] == x and tabuleiro[2][2] == x and tabuleiro[2][1] == "":
        tabuleiro[2][1] = ia
    #
    elif tabuleiro[0][2] == x and tabuleiro[1][1] == x and tabuleiro[2][0] == "":
        tabuleiro[2][0] = ia
    elif tabuleiro[2][0] == x and tabuleiro[1][1] == x and tabuleiro[0][2] == "":
        tabuleiro[0][2] = ia
    elif tabuleiro[0][2] == x and tabuleiro[2][0] == x and tabuleiro[1][1] == "":
        tabuleiro[1][1] = ia
    #
    elif tabuleiro[0][2] == x and tabuleiro[1][2] == x and tabuleiro[2][2] == "":
        tabuleiro[2][2] = ia
    elif tabuleiro[2][2] == x and tabuleiro[1][2] == x and tabuleiro[0][2] == "":
        tabuleiro[0][2] = ia
    elif tabuleiro[0][2] == x and tabuleiro[2][2] == x and tabuleiro[1][2] == "":
        tabuleiro[1][2] = ia
    #
    elif tabuleiro[0][1] == x and tabuleiro[1][1] == x and tabuleiro[2][1] == "":
        tabuleiro[2][1] = ia
    elif tabuleiro[2][1] == x and tabuleiro[1][1] == x and tabuleiro[0][1] == "":
        tabuleiro[0][1] = ia
    elif tabuleiro[0][1] == x and tabuleiro[2][1] == x and tabuleiro[1][1] == "":
        tabuleiro[1][1] = ia
    #
    elif tabuleiro[1][0] == x and tabuleiro[1][1] == x and tabuleiro[1][2] == "":
        tabuleiro[1][2] = ia
    elif tabuleiro[1][2] == x and tabuleiro[1][1] == x and tabuleiro[1][0] == "":
        tabuleiro[1][0] = ia
    elif tabuleiro[1][0] == x and tabuleiro[1][2] == x and tabuleiro[1][1] == "":
        tabuleiro[1][1] = ia
    else:
        return 0"""
