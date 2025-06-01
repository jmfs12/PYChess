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

    def valid(self, tabuleiro, ultimo_movimento, ignorar_roque=False):
        linha, coluna = self.posicao
        movimentos = []

        if self.tipo == "P":
            en_passant = None
            direcao = -1 if self.cor == "branco" else 1
            frente = (linha + direcao, coluna)
            if 0 <= frente[0] < 8 and 0 <= frente[1] < 8 and tabuleiro[frente[0]][frente[1]] is None:
                movimentos.append(frente)
                linha_inicial = 6 if self.cor == "branco" else 1
                duas_frente = (linha + 2 * direcao, coluna)
                if (
                    linha == linha_inicial
                    and 0 <= duas_frente[0] < 8
                    and 0 <= duas_frente[1] < 8
                    and tabuleiro[duas_frente[0]][duas_frente[1]] is None
                ):
                    movimentos.append(duas_frente)

            for dc in [-1, 1]:
                diag = (linha + direcao, coluna + dc)
                if 0 <= diag[0] < 8 and 0 <= diag[1] < 8:
                    alvo = tabuleiro[diag[0]][diag[1]]
                    if alvo is not None and alvo.cor != self.cor:
                        movimentos.append(diag)

            # Verifica se pode capturar en passant
            if self.cor == 'branco' and self.posicao[0] == 3:
                for dx in [-1, 1]:
                    lado = (self.posicao[0], self.posicao[1] + dx)
                    if 0 <= lado[0] < 8 and 0 <= lado[1] < 8 and tabuleiro[lado[0]][lado[1]] is not None:
                        peca_lado = tabuleiro[lado[0]][lado[1]]
                        if (
                            peca_lado.tipo == 'P'
                            and peca_lado.cor != self.cor
                            and ultimo_movimento == (peca_lado, (1, lado[1]), lado)
                        ):
                            movimentos.append((2, lado[1]))  # Casa atrás do peão inimigo
                            en_passant = "en passant"

            elif self.cor == 'preto' and self.posicao[0] == 4:
                for dx in [-1, 1]:
                    lado = (self.posicao[0], self.posicao[1] + dx)
                    if lado in tabuleiro and tabuleiro[lado[0]][lado[1]] is not None:
                        peca_lado = tabuleiro[lado[0]][lado[1]]
                        if (
                            peca_lado.tipo == 'P'
                            and peca_lado.cor != self.cor
                            and ultimo_movimento == (peca_lado, (6, lado[1]), lado)
                        ):
                            movimentos.append((5, lado[1]))  # Casa atrás do peão inimigo
                            en_passant = "en passant"   


            return movimentos, en_passant

        elif self.tipo in ("B", "RA"):
            direcoes = (
                [(1, -1), (1, 1), (-1, 1), (-1, -1)]
                if self.tipo == "B"
                else [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 1),
                    (-1, 1),
                    (-1, -1),
                ]
            )
            for l, c in direcoes:
                mov_linha, mov_coluna = linha + l, coluna + c
                while 0 <= mov_linha < 8 and 0 <= mov_coluna < 8:
                    alvo = tabuleiro[mov_linha][mov_coluna]
                    if alvo is None:
                        movimentos.append((mov_linha, mov_coluna))
                    elif alvo.cor != self.cor:
                        movimentos.append((mov_linha, mov_coluna))
                        break
                    else:
                        break
                    mov_linha += l
                    mov_coluna += c
            return movimentos, None

        elif self.tipo == "C":
            direcoes = [
                (-2, 1),
                (-2, -1),
                (2, 1),
                (2, -1),
                (1, -2),
                (-1, -2),
                (1, 2),
                (-1, 2),
            ]
            for l, c in direcoes:
                nl, nc = linha + l, coluna + c
                if 0 <= nl < 8 and 0 <= nc < 8:
                    alvo = tabuleiro[nl][nc]
                    if alvo is None or alvo.cor != self.cor:
                        movimentos.append((nl, nc))
            return movimentos, None

        elif self.tipo == "RE":
            movimentos = []
            direcoes = [(-1, 0),(1, 0),(0, -1),(0, 1),(1, -1),(1, 1),(-1, 1),(-1, -1)]
            for l, c in direcoes:
                mov_linha, mov_coluna = linha + l, coluna + c
                if 0 <= mov_linha < 8 and 0 <= mov_coluna < 8:
                    alvo = tabuleiro[mov_linha][mov_coluna]
                    if alvo is None or alvo.cor != self.cor:
                        movimentos.append((mov_linha, mov_coluna))


            roque_valido = False
            posicao_torre = [(linha, 0), (linha, 7)]
            if not ignorar_roque and self.inicial:
                for torre_pos in posicao_torre:
                    t_col = torre_pos[1]
                    torre = tabuleiro[linha][t_col]
                    if torre and torre.tipo == "T" and torre.inicial:
                        passo = 1 if t_col > coluna else -1
                        caminho_livre = all(
                            tabuleiro[linha][c] is None
                            for c in range(coluna + passo, t_col, passo)
                        )
                        if caminho_livre:
                            casas_passadas = [
                                (linha, coluna + passo),
                                (linha, coluna + 2 * passo),
                            ]
                            em_check = False
                            for casa in casas_passadas:
                                self.posicao = casa
                                for row in tabuleiro:
                                    for p in row:
                                        if (
                                            p
                                            and p.cor != self.cor
                                            and casa in p.valid(tabuleiro, ignorar_roque=True)[0]
                                        ):
                                            em_check = True
                                if em_check:
                                    break
                            self.posicao = (linha, coluna)
                            if not em_check:
                                movimentos.append((linha, coluna + 2 * passo))
                                roque_valido = True
            return movimentos, "roque" if roque_valido else None


        elif self.tipo == "T":
            direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for l, c in direcoes:
                mov_linha, mov_coluna = linha + l, coluna + c
                while 0 <= mov_linha < 8 and 0 <= mov_coluna < 8:
                    alvo = tabuleiro[mov_linha][mov_coluna]
                    if alvo is None:
                        movimentos.append((mov_linha, mov_coluna))
                    elif alvo.cor != self.cor:
                        movimentos.append((mov_linha, mov_coluna))
                        break
                    else:
                        break
                    mov_linha += l
                    mov_coluna += c
            return movimentos, None
