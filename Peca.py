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

        if self.tipo == 'P':
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

            #falta o en passant

            return movimentos, None
        
        elif self.tipo == 'B' or self.tipo == 'RA':
            linha, coluna = self.posicao
            movimentos = []

            if self.tipo == 'B':
                direcoes = [(1,-1),(1,1),(-1,1),(-1,-1)]
            else:
                direcoes = [(-1,0),(1,0),(0,-1),(0,1),(1,-1),(1,1),(-1,1),(-1,-1)]

            for l, c in direcoes:
                movimento = (linha+l, coluna+c)

                while movimento in tabuleiro:

                    if tabuleiro[movimento] is None:
                        movimentos.append(movimento)

                    elif tabuleiro[movimento] is not None and tabuleiro[movimento].cor != self.cor:
                        movimentos.append(movimento)
                        break

                    else:
                        break

                    movimento = (movimento[0]+l, movimento[1]+c)
            return movimentos, None

        elif self.tipo == 'C':
            linha, coluna = self.posicao
            movimentos = []

            direcoes = [(-2,1),(-2,-1),(2,1),(2,-1),(1,-2),(-1,-2),(1,2),(-1,2)]

            for l, c in direcoes:

                movimento = (linha+l, coluna+c)

                if movimento in tabuleiro:

                    if tabuleiro[(movimento)] is None:
                        movimentos.append(movimento)

                    elif tabuleiro[movimento] is not None and tabuleiro[movimento].cor != self.cor:
                        movimentos.append(movimento)

            return movimentos, None
    
        elif self.tipo == 'RE':
            linha, coluna = self.posicao
            movimentos = []

            direcoes = [(-1,0),(1,0),(0,-1),(0,1),(1,-1),(1,1),(-1,1),(-1,-1)]

            for l, c in direcoes:

                movimento = (linha+l, coluna+c)

                if movimento in tabuleiro:

                    if tabuleiro[(movimento)] is None:
                        movimentos.append(movimento)

                    elif tabuleiro[movimento] is not None and tabuleiro[movimento].cor != self.cor:
                        movimentos.append(movimento)

            posicao_torre = [(7,7),(7,0)] if self.cor == 'branco' else [(0,7),(0,0)]
            if self.inicial:
                for torre in posicao_torre:
                    if tabuleiro[torre] is not None and tabuleiro[torre].inicial:
                        flag, c = False, coluna
                        while not flag and c != torre[1]:
                            c = c+1 if coluna < torre[1] else c-1
                            if tabuleiro[(linha, c)] is not None:
                                flag = True

                        if not flag:
                            col = coluna + 2 if torre[1] > coluna else coluna - 2
                            movimentos.append((linha,col))
                return movimentos, 'roque'

                
            return movimentos, None
    
        elif self.tipo == 'T':
            linha, coluna = self.posicao
            movimentos = []

            direcoes = [(-1,0),(1,0),(0,-1),(0,1)]

            for l, c in direcoes:
                movimento = (linha+l, coluna+c)

                while movimento in tabuleiro:

                    if tabuleiro[movimento] is None:
                        movimentos.append(movimento)

                    elif tabuleiro[movimento] is not None and tabuleiro[movimento].cor != self.cor:
                        movimentos.append(movimento)
                        break

                    else:
                        break

                    movimento = (movimento[0]+l, movimento[1]+c)
            
            rei = (7,4) if self.cor == 'branco' else (0,4)
            if self.inicial:
                if tabuleiro[rei] is not None and tabuleiro[rei].inicial:
                    flag, c = False, coluna
                    while not flag and c != rei[1]:
                        c = c+1 if coluna < rei[1] else c-1
                        if tabuleiro[(linha, c)] is not None:
                            flag = True

                    if not flag:
                        col = coluna + 2 if rei[1] > coluna else coluna - 2
                        movimentos.append((linha,col))
                return movimentos, 'roque'

            return movimentos, None