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

    def move(self, peca, posicao) -> bool:
        movimentos, tipo_mov = peca.valid(self.tabuleiro)
        print(movimentos)

        print('verificando a movimentacao')
        if posicao in movimentos or tipo_mov == 'roque':
            tab_antes = self.tabuleiro[posicao]
            self.tabuleiro[peca.posicao], self.tabuleiro[posicao] = None, peca
            origem = peca.posicao

            posicao_ant, inicial_ant = peca.posicao, peca.inicial
            peca.posicao, peca.inicial = posicao, False

            if self.verify_check(peca.cor):
                print('rei em check')
                self.tabuleiro[posicao_ant], self.tabuleiro[posicao] = peca, tab_antes
                peca.posicao, peca.inicial = posicao_ant, inicial_ant
                print('movimentacao recusada')
                return False
                
            if tipo_mov == 'roque' and peca.tipo == 'RE':
                linha = origem[0]
                if posicao[1] == 6:  # Roque pequeno
                    torre_origem = (linha, 7)
                    torre_destino = (linha, 5)
                elif posicao[1] == 2:  # Roque grande
                    torre_origem = (linha, 0)
                    torre_destino = (linha, 3)
                else:
                    print("Erro: posição de roque inválida")
                    return False

                torre = self.tabuleiro[torre_origem]
                if torre and torre.tipo == 'T':
                    self.tabuleiro[torre_origem] = None
                    self.tabuleiro[torre_destino] = torre
                    torre.posicao = torre_destino
                    torre.inicial = False
                else:
                    print("Erro: torre não encontrada no roque")
                    return False
            print('movimentação feita')
            return True

        print('movimentação recusada')
        return False
    
    def verify_check(self, cor):

        pecas_inimigas = []
        rei = None
        for peca in self.tabuleiro.values():
            if peca is not None:
                if peca.tipo == 'RE' and peca.cor == cor:
                    rei = peca
                if peca.cor != cor:
                    pecas_inimigas.append(peca)
            
        movimentos_inimigo = []
        for peca in pecas_inimigas:
            movimentos, _ = peca.valid(self.tabuleiro)
            movimentos_inimigo.extend(movimentos)

        return rei.posicao in movimentos_inimigo

    def not_have_moves(self, cor):
        for peca in self.tabuleiro.values():
            if peca is not None and peca.cor == cor:
                movimentos, _ = peca.valid(self.tabuleiro)
                for destino in movimentos:
                    # Tenta simular o movimento
                    origem = peca.posicao
                    peca_original = self.tabuleiro[destino]
                    self.tabuleiro[origem], self.tabuleiro[destino] = None, peca
                    peca.posicao = destino

                    em_check = self.verify_check(cor)

                    # Reverte o movimento
                    self.tabuleiro[origem], self.tabuleiro[destino] = peca, peca_original
                    peca.posicao = origem

                    if not em_check:
                        return False  # Existe pelo menos um movimento legal
        return True  # Nenhuma peça pode se mover sem deixar o rei em check

                
        