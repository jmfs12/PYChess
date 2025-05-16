import pygame as py
import Interface as it

class Player:
    def __init__(self, cor, tabuleiro):
        self.cor = cor
        self.tabuleiro = tabuleiro
    
    def move(self, peca, posicao) -> bool:
        movimentos = peca.valid(self.tabuleiro)
        print(movimentos)

        if posicao in movimentos[0]:
            print('atualizando o tabuleiro')
            self.tabuleiro[peca.posicao] = None
            self.tabuleiro[posicao] = peca

            peca.posicao = posicao
            peca.inicial = False

            print('movimentação feita')
            return True

        print('movimentação recusada')
        return False

