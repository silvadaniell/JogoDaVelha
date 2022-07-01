from sec_funct import jogo_velha
from sec_funct import positions
from sec_funct import test_winner

def positions_null(tabuleiro):
    armazena = []
    contador = 1
    while contador <= 9:
        i = positions(contador)[0]
        j = positions(contador)[1]
        if tabuleiro[i][j] == "":
            armazena.append((i, j))
        contador = contador + 1
    return armazena

score = {
    'X' : 1,
    'O' : -1,
    'EMPATE' : 0
}

def brute_force(tabuleiro, jogador, token):
    winner = test_winner(tabuleiro)
    if(winner):
        return score[winner]
    
    jogador = (jogador + 1) % 2
    
    possibilidades = positions_null(tabuleiro)
    melhor_valor = None
    for coordenadas in possibilidades:
        tabuleiro[coordenadas[0]][coordenadas[1]] = token[jogador]
        valor = brute_force(tabuleiro, jogador, token)
        tabuleiro[coordenadas[0]][coordenadas[1]] = ""

        if(melhor_valor is None):
            melhor_valor = valor
        elif(jogador == 0):
            if(melhor_valor > valor):
                melhor_valor = valor
        elif(jogador == 1):
            if(melhor_valor < valor):
                melhor_valor = valor
    return melhor_valor

def moviment(tabuleiro, jogador, token):
    possibilidades = positions_null(tabuleiro)
    melhor_jogada = None
    melhor_valor = None
    
    for coordenadas in possibilidades:
        tabuleiro[coordenadas[0]][coordenadas[1]] = token[jogador]
        valor = brute_force(tabuleiro, jogador, token)
        tabuleiro[coordenadas[0]][coordenadas[1]] = ""
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_jogada = coordenadas
        elif jogador == 0:
            if melhor_valor < valor:
                melhor_valor = valor
                melhor_jogada = coordenadas
        elif jogador == 1:
            if melhor_valor > valor:
                melhor_valor = valor
                melhor_jogada = coordenadas     
    return melhor_jogada
