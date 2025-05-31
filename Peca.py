import pygame

class Peca:
    def __init__(self, tipo, posicao, resource):
        self.tipo = tipo
        self.posicao = posicao
        if posicao[0] == 0 or posicao[0] == 1:
            self.cor = "preto"
        else:
            self.cor = "branco"
        self.inicial = True
        self.resource = pygame.transform.smoothscale(resource, (80, 80))
        

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
                    if tabuleiro[(movimento)] is None or tabuleiro[movimento].cor != self.cor:
                        movimentos.append(movimento)

            # Verificação de Roque
            posicao_torre = [(linha, 7), (linha, 0)]
            roque_valido = False
            if self.inicial:
                for torre_pos in posicao_torre:
                    torre = tabuleiro.get(torre_pos)
                    if torre and torre.tipo == 'T' and torre.inicial:
                        col_torre = torre_pos[1]
                        passo = 1 if col_torre > coluna else -1

                        # Verifica se há peças entre rei e torre
                        caminho_livre = True
                        for c in range(coluna + passo, col_torre, passo):
                            if tabuleiro.get((linha, c)) is not None:
                                caminho_livre = False
                                break

                        # Verifica se o rei está ou passará por xeque
                        if caminho_livre:
                            casas_passadas = [(linha, coluna), (linha, coluna + passo), (linha, coluna + 2*passo)]
                            em_check = False
                            for casa in casas_passadas:
                                temp_pos = self.posicao
                                self.posicao = casa
                                if any(casa in inimigo.valid(tabuleiro)[0] for inimigo in tabuleiro.values() if inimigo and inimigo.cor != self.cor):
                                    em_check = True
                                self.posicao = temp_pos
                                if em_check:
                                    break

                            if not em_check:
                                movimentos.append((linha, coluna + 2*passo))
                                roque_valido = True

            return movimentos, 'roque' if roque_valido else None

    
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

            return movimentos, None