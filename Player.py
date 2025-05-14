class Player:
    def __init__(self, cor):
        self.cor = cor
    
    def move(self, peca, posicao, tabuleiro, board) -> bool:
        movimentos = peca.valid(tabuleiro)
        print(posicao)
        if posicao in movimentos:

            board[peca.posicao[0]][peca.posicao[1]] = ' '
            board[posicao[0]][posicao[1]] = peca

            tabuleiro[peca.posicao] = None
            tabuleiro[posicao] = peca

            peca.posicao=posicao
            peca.inicial = False

            return True
        return False
