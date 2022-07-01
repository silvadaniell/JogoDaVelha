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
   print("\n\n==============================================================================")
   print("\t\t\t\tJOGO DA VELHA")
   print("==============================================================================")
   print("\n\t\tAS POSICOES DO TABULEIRO FUNCIONAM DA SEGUINTE FORMA:")
   for k in range(3):
       if k > 0:
           print("\n------")
       for l in range(3):
           if l == 1 or l == 2:
               print("|", end="")
           print(contador, end="")
           contador = contador + 1
    
   print("\n==============================================================================")
   player = int(input("\nQUEM IRA COMECAR O JOGO?\n   1 - IA\n   2 - USER\n     Opcao: "))
  
   if player == 1:
       token = []
       token.append('X')
       token.append('O')
       jogador = 0
       while not test_winner(tabuleiro):
           if jogador == 1:
               print("===============\nJOGADA DO O:\n")
               jogada = user_play(tabuleiro)
               l = positions(jogada)[0]
               k = positions(jogada)[1]
               tabuleiro[l][k] = token[jogador]
           else:
               l = moviment(tabuleiro, jogador, token)[0]
               k = moviment(tabuleiro, jogador, token)[1]
               tabuleiro[l][k] = token[jogador]
               os.system("cls")
               print("JOGADA DO X\n===============\n")
           if test_winner(tabuleiro) == 'X':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nX GANHOU!\n===============")
               return 0
           elif test_winner(tabuleiro) == 'O':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nO GANHOU!\n===============")
               return 0
           elif test_winner(tabuleiro) == 'EMPATE':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nEMPATE!\n===============")
               return 0
           jogador = (jogador + 1) % 2
           jogo_velha(tabuleiro)
   elif player == 2:
       token = []
       token.append('X')
       token.append('O')
       jogador = 1
       os.system("cls")
       while not test_winner(tabuleiro):
           if jogador == 1:
               print("===============\nJOGADA DO O:\n")
               jogada = user_play(tabuleiro)
               l = positions(jogada)[0]
               k = positions(jogada)[1]
               tabuleiro[l][k] = token[jogador]
           else:
               l = moviment(tabuleiro, jogador, token)[0]
               k = moviment(tabuleiro, jogador, token)[1]
               tabuleiro[l][k] = token[jogador]
               os.system("cls")
               print("JOGADA DO X\n===============\n")
           if test_winner(tabuleiro) == 'X':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nX GANHOU!\n===============")
               return 0
           elif test_winner(tabuleiro) == 'O':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nO GANHOU!\n===============")
               return 0
           elif test_winner(tabuleiro) == 'EMPATE':
               os.system("cls")
               jogo_velha(tabuleiro)
               print("===============\nEMPATE!\n===============")
               return 0
           jogador = (jogador + 1) % 2
           jogo_velha(tabuleiro)
   else:
       game()
   
game()

