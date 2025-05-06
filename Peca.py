#classe para as peças

class Peca:
    def __init__(self, tipo, posicao):
        self.tipo = tipo
        self.posicao = posicao
        self.vivo = True
        if posicao[0] == 0 or posicao[0] == 1:
            self.cor = "preto"
        else:
            self.cor = "branco"
        self.inicial = True

    def valid(self, tabuleiro):
        
        linha, coluna = self.posicao
        direcao = -1 if self.cor == 'branco' else 1
        movimentos = []

        frente = (linha+direcao, coluna)
        if frente in tabuleiro and tabuleiro[frente] is None:
            movimentos.append(frente)

            linha_inicial = 6 if self.cor =='branco' else 1
            duas_frente = (linha + 2*direcao, coluna)
            if linha == linha_inicial and duas_frente in tabuleiro and tabuleiro[duas_frente] is None:
                movimentos.append(duas_frente)
        
        for dc in [-1, 1]:
            diag = (linha + direcao, coluna + dc)
            if diag in tabuleiro:
                alvo = tabuleiro[diag]
                if alvo is not None and alvo.cor != self.cor:
                    movimentos.append(diag)

        return movimentos
        

class Movimento:
    pass