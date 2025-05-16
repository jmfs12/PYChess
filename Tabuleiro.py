from Peca import Peca
import pygame as py

class Tabuleiro:

    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.tabuleiro = {
            (i,j) : None
            for i in range(8)
            for j in range(8)
        }
        print("Criando tabuleiro")
        for i in range(8):
            self.board[1][i] = Peca('P', (1,i), py.image.load('resource/peao_preto.png'))
            self.board[6][i] = Peca('P', (6,i), py.image.load('resource/peao_branco.png'))

        tipos = ['T', 'C', 'B', 'RA', 'RE', 'B', 'C', 'T']
        resources_branco = ['resource/torre_branco.png', 'resource/cavalo_branco.png', 'resource/bispo_branco.png', 'resource/rainha_branco.png', 'resource/rei_branco.png', 
                     'resource/bispo_branco.png','resource/cavalo_branco.png', 'resource/torre_branco.png']
        resources_preto = ['resource/torre_preto.png', 'resource/cavalo_preto.png', 'resource/bispo_preto.png', 'resource/rainha_preto.png', 'resource/rei_preto.png', 
                     'resource/bispo_preto.png','resource/cavalo_preto.png', 'resource/torre_preto.png']
        
        for col, tipo in enumerate(tipos):
            self.board[7][col] = Peca(tipo, (7,col), py.image.load(resources_branco[col]))
            self.board[0][col] = Peca(tipo, (0, col), py.image.load(resources_preto[col]))
            self.tabuleiro[(7, col)] = Peca(tipo, (7, col), py.image.load(resources_branco[col]))
            self.tabuleiro[(0, col)] = Peca(tipo, (0, col), py.image.load(resources_preto[col]))

        for i in range(8):
            self.tabuleiro[(1,i)] = self.board[1][i]
            self.tabuleiro[(6,i)] = self.board[6][i]

        self.index = {
            f"{chr(65 + coluna)}{linha + 1}" : (7 - linha, coluna)
            for linha in range(8)
            for coluna in range(8)
        }


        self.winner = ''

    def print_board(self):
        for l in self.board:
            for p in l:
                if (type(p).__name__ == 'Peca'):
                    print(p.tipo + p.cor, end=' ')
                else:
                    print(p, end=' ')
            print()

    def valid_moves(self, peca):
        valid = []

        if peca.tipo == 'P':
            pass

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
                