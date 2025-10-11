# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet (como por exemplo códigos gerados por IA).
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import random
import os

def limpar():
    os.system('cls')

def criar_tabuleiro():
    matriz = []

    for l in range(15):
        matriz.append([])
        for c in range(15):
            matriz[l].append(0)
    
    return matriz

def canvas_tabuleiro(tabuleiro):
    limpar()
                
    for linha in tabuleiro:
        for num in linha:
            if num == 0:
                print('🟨', end=' ')
            elif num == 1:
                print('🟩', end=' ')
            elif num == 2:
                print('🍎', end=' ')
            else:
                print('🧄', end=' ')
        print()
    
def cobra_inicial(tabuleiro):
    
    tabuleiro[0][1] = 1
    tabuleiro[0][0] = 1

    return [[0, 1], [0, 0]], tabuleiro

def gerar_frutas_boas(tabuleiro):
    coordenada_fruta_boa = []

    for i in range(0,5): # Gera posições frutas boas
            posicao_ocupada = True

            while posicao_ocupada == True:
                fruta_boa_linha = random.randint(0, 14)
                fruta_boa_coluna = random.randint(0, 14)

                if tabuleiro[fruta_boa_linha][fruta_boa_coluna] == 0:
                    tabuleiro[fruta_boa_linha][fruta_boa_coluna] = 2
                    posicao_ocupada = False
        
    return coordenada_fruta_boa

def gerar_frutas_ruins(tabuleiro):
    coordenada_fruta_ruins = []

    for i in range(0,5): # Gera posições frutas boas
        posicao_ocupada = True

        while posicao_ocupada == True:
            fruta_ruim_linha = random.randint(0, 14)
            fruta_ruim_coluna = random.randint(0, 14)

            if tabuleiro[fruta_ruim_linha][fruta_ruim_coluna] == 0:
                tabuleiro[fruta_ruim_linha][fruta_ruim_coluna] = 3
                posicao_ocupada = False

    return coordenada_fruta_ruins

def mover_cobra(posicao_cobra, tabuleiro):

    if mover == 'D':


def jogo_principal():
    tabuleiro = criar_tabuleiro()
    posicao_cobra, tabuleiro = cobra_inicial(tabuleiro)
    frutas_boas = gerar_frutas_boas(tabuleiro)
    frutas_ruins = gerar_frutas_ruins(tabuleiro)

    game_over = False

    while not game_over == True:
        canvas = canvas_tabuleiro(tabuleiro)
        mover = mover_cobra(posicao_cobra, tabuleiro)

        mover_teste = input('Mova com D/A/W/S: ')


jogo_principal()
