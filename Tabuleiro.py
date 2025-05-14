from Peca import Peca

class Tabuleiro:

    #inicialização do board (para printar) e do tabuleiro(para manipular as peças)
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.tabuleiro = {
            (i,j) : None
            for i in range(8)
            for j in range(8)
        }
        print("Criando tabuleiro")
        for i in range(8):
            self.board[1][i] = Peca('P', (1,i))
            self.board[6][i] = Peca('P', (6,i))

        tipos = ['T', 'C', 'B', 'RA', 'RE', 'B', 'C', 'T']
        
        for col, tipo in enumerate(tipos):
            self.board[7][col] = Peca(tipo, (7,col))
            self.board[0][col] = Peca(tipo, (0, col))
            self.tabuleiro[(7, col)] = Peca(tipo, (7, col))
            self.tabuleiro[(0, col)] = Peca(tipo, (0, col))

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


                