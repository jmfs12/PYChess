import pygame as py
import Interface as it

class Player:
    def __init__(self, cor, pecas):
        self.cor = cor
        self.pecas = pecas
    
    def move(self, peca, posicao, tabuleiro, screen) -> bool:
        movimentos = peca.valid(tabuleiro)

        if posicao in movimentos:

            tabuleiro[peca.posicao] = None
            tabuleiro[posicao] = peca
            linha, col = peca.posicao

            py.draw.rect(
                screen,
                py.Color('#EEEED2') if (linha+col)%2 == 0 else py.Color('#769656'),
                py.Rect(col*80, linha*80, 80, 80) 
            )

            screen.blit(peca.resource, (col*80, linha*80))

            peca.posicao=posicao
            peca.inicial = False

            return True
        return False
