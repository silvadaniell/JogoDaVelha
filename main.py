import random
from sec_funct import positions
from sec_funct import jogo_velha
from sec_funct import test_winner
from sec_funct import user_play
from iastart import moviment
import os



#PRINCIPAL   
def game():
    tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
    k = 0
    l = 0
    contador = 1
    print('='*80)
    print("\t\t\t\tJOGO DA VELHA")
    print('='*80)
    print("\n\t\tAS POSICOES DO TABULEIRO FUNCIONAM DA SEGUINTE FORMA:")
    for k in range(3):
        if k > 0:
            print("\n------")
        for l in range(3):
            if l == 1 or l == 2:
                print("|", end="")
            print(contador, end="")
            contador = contador + 1
    print("\n\nQUEM INICIA O JOGO SEMPRE USA O CARACTERE X")
    print('.'*80) 
    print("")
    print('QUEM IRA COMECAR O JOGO?\n   1 - IA\n   2 - USER')
    print('')
    player = int(input("   >>> Opcao: "))
    
    if player == 1:
        token = []
        token.append('X')
        token.append('O')
        jogador = 0
        while not test_winner(tabuleiro):
            if jogador == 1:
                print("USER = O")
                print('.'*60)
                print('\nJOGADA DO USER:')
                jogada = user_play(tabuleiro)
                l = positions(jogada)[0]
                k = positions(jogada)[1]
                tabuleiro[l][k] = token[jogador]
            else:
                auxiliar = moviment(tabuleiro, jogador, token)
                l = auxiliar[0]
                k = auxiliar[1]
                tabuleiro[l][k] = token[jogador]
                os.system("cls")
                print("IA = X")
                print('.'*60)
                print('\nJOGADA DA IA:')
            if test_winner(tabuleiro) == 'X':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tIA GANHOU!')
                print('='*80)
                return 0
            elif test_winner(tabuleiro) == 'O':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tUSER GANHOU!')
                print('='*80)
                return 0
            elif test_winner(tabuleiro) == 'EMPATE':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tEMPATE!')
                print('='*80)
                return 0
            jogador = (jogador + 1) % 2
            jogo_velha(tabuleiro)
    elif player == 2:
        token = []
        token.append('O')
        token.append('X')
        jogador = 1
        os.system("cls")
        while not test_winner(tabuleiro):
            if jogador == 1:
                print("USER = X")
                print('.'*60)
                print('\nJOGADA DO USER:')
                jogada = user_play(tabuleiro)
                l = positions(jogada)[0]
                k = positions(jogada)[1]
                tabuleiro[l][k] = token[jogador]
            else:
                auxiliar = moviment(tabuleiro, jogador, token)
                l = auxiliar[0]
                k = auxiliar[1]
                tabuleiro[l][k] = token[jogador]
                os.system("cls")
                print("IA = O")
                print('.'*60)
                print('\nJOGADA DA IA:')
            if test_winner(tabuleiro) == 'X':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tUSER GANHOU!')
                print('='*80)
                return 0
            elif test_winner(tabuleiro) == 'O':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tIA GANHOU!')
                print('='*80)
                return 0
            elif test_winner(tabuleiro) == 'EMPATE':
                os.system("cls")
                jogo_velha(tabuleiro)
                print('.'*80)
                print('\t\t\t\t\tEMPATE!')
                print('='*80)
                return 0
            jogador = (jogador + 1) % 2
            jogo_velha(tabuleiro)
    else:
        game()
     
game()
