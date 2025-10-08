import random
import time

loop_jogo = True 

def criar_tabuleiro():
    tabuleiro = []
    for i in range (15):
        linha = ['🟨'] * 15
        tabuleiro.append(linha)

    return tabuleiro

def gerar_frutas(): # Gera coordenadas frutas boas e ruins
    coordenada_fruta_boa = []
    coordenada_fruta_ruim = []

    for i in range(0,5): # Gera posições frutas boas
        fruta_boa_linha = random.randint(0, 14)
        fruta_boa_coluna = random.randint(0, 14)

        coordenada_fruta_boa.append([fruta_boa_linha, fruta_boa_coluna]) 
    
    for i in range(0,5): # Gera posições frutas ruins
        fruta_ruim_linha = random.randint(0, 14)
        fruta_ruim_coluna = random.randint(0, 14)

        coordenada_fruta_ruim.append([fruta_ruim_linha, fruta_ruim_coluna])
    
    return coordenada_fruta_boa , coordenada_fruta_ruim

def jogo_principal(): 
    frutas_boas , frutas_ruins = gerar_frutas()
    tabuleiro = criar_tabuleiro()
    cobra = [[0,0],[0,1]]
    direcao = [0,1] # Direita

    # while loop_jogo: 
    for coordenada in frutas_boas: # Inserção fruta boa no tabuleiro
        linha = coordenada[0]
        coluna = coordenada[1]

        tabuleiro[linha][coluna] = '🍎'

    for coordenada in frutas_ruins: # Inserção fruta ruins no tabuleiro
        linha = coordenada[0]
        coluna = coordenada[1]

        tabuleiro[linha][coluna] = '🧄'
    
    for coordenada in cobra: # Inserção cobra no tabuleiro
        linha = coordenada[0]
        coluna = coordenada[1]

        if coordenada == cobra[-1]:
            tabuleiro[linha][coluna] = '🐲'
        else: 
            tabuleiro[linha][coluna] = '🟩'

    for linha in tabuleiro:
        print(' '.join(linha))

jogo_principal()
