from Peca import Peca
import pygame as py


class Tabuleiro:

    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        print("Criando tabuleiro")

        for i in range(8):
            self.tabuleiro[1][i] = Peca(
                "P", (1, i), py.image.load("resource/peao_preto.png")
            )
            self.tabuleiro[6][i] = Peca(
                "P", (6, i), py.image.load("resource/peao_branco.png")
            )

        tipos = ["T", "C", "B", "RA", "RE", "B", "C", "T"]
        resources_branco = [
            "resource/torre_branco.png",
            "resource/cavalo_branco.png",
            "resource/bispo_branco.png",
            "resource/rainha_branco.png",
            "resource/rei_branco.png",
            "resource/bispo_branco.png",
            "resource/cavalo_branco.png",
            "resource/torre_branco.png",
        ]
        resources_preto = [
            "resource/torre_preto.png",
            "resource/cavalo_preto.png",
            "resource/bispo_preto.png",
            "resource/rainha_preto.png",
            "resource/rei_preto.png",
            "resource/bispo_preto.png",
            "resource/cavalo_preto.png",
            "resource/torre_preto.png",
        ]

        for col, tipo in enumerate(tipos):
            self.tabuleiro[7][col] = Peca(
                tipo, (7, col), py.image.load(resources_branco[col])
            )
            self.tabuleiro[0][col] = Peca(
                tipo, (0, col), py.image.load(resources_preto[col])
            )

        self.index = {
            f"{chr(65 + coluna)}{linha + 1}": (7 - linha, coluna)
            for linha in range(8)
            for coluna in range(8)
        }

    def print_board(self):
        for linha in self.tabuleiro:
            for peca in linha:
                if isinstance(peca, Peca):
                    print(peca.tipo + peca.cor, end=" ")
                else:
                    print(" ", end=" ")
            print()

    def move(self, peca, posicao) -> bool:
        movimentos, tipo_mov = peca.valid(self.tabuleiro)
        print(movimentos)

        print("verificando a movimentacao")
        if posicao in movimentos or tipo_mov == "roque":
            linha_origem, coluna_origem = peca.posicao
            linha_destino, coluna_destino = posicao
            tab_antes = self.tabuleiro[linha_destino][coluna_destino]
            self.tabuleiro[linha_origem][coluna_origem] = None
            self.tabuleiro[linha_destino][coluna_destino] = peca
            origem = peca.posicao

            posicao_ant, inicial_ant = peca.posicao, peca.inicial
            peca.posicao, peca.inicial = posicao, False

            if self.verify_check(peca.cor):
                print("rei em check")
                self.tabuleiro[linha_origem][coluna_origem] = peca
                self.tabuleiro[linha_destino][coluna_destino] = tab_antes
                peca.posicao, peca.inicial = posicao_ant, inicial_ant
                print("movimentacao recusada")
                return False

            if tipo_mov == "roque" and peca.tipo == "RE" and (coluna_destino == 6 or coluna_destino == 2):
                linha = origem[0]
                if coluna_destino == 6:
                    torre_origem = (linha, 7)
                    torre_destino = (linha, 5)
                elif coluna_destino == 2:
                    torre_origem = (linha, 0)
                    torre_destino = (linha, 3)
                else:
                    print("Erro: posição de roque inválida")
                    return False

                torre = self.tabuleiro[torre_origem[0]][torre_origem[1]]
                if torre and torre.tipo == "T":
                    self.tabuleiro[torre_origem[0]][torre_origem[1]] = None
                    self.tabuleiro[torre_destino[0]][torre_destino[1]] = torre
                    torre.posicao = torre_destino
                    torre.inicial = False
                else:
                    print("Erro: torre não encontrada no roque")
                    return False
                
            if peca.tipo == 'P':
                if (peca.cor == 'branco' and linha_destino == 0) or (peca.cor == 'preto' and linha_destino == 7):
                    self.tabuleiro[linha_destino][coluna_destino] = Peca('RA', (linha_destino, coluna_destino), py.image.load(f"resource/rainha_{peca.cor}.png"))
                    self.tabuleiro[linha_destino][coluna_destino].cor = peca.cor
            print("movimentação feita")
            return True

        print("movimentação recusada")
        return False

    def verify_check(self, cor):
        pecas_inimigas = []
        rei = None
        for linha in self.tabuleiro:
            for peca in linha:
                if peca is not None:
                    if peca.tipo == "RE" and peca.cor == cor:
                        rei = peca
                    if peca.cor != cor:
                        pecas_inimigas.append(peca)

        movimentos_inimigo = []
        for peca in pecas_inimigas:
            movimentos, _ = peca.valid(self.tabuleiro)
            movimentos_inimigo.extend(movimentos)

        return rei.posicao in movimentos_inimigo

    def not_have_moves(self, cor):
        for linha in self.tabuleiro:
            for peca in linha:
                if peca is not None and peca.cor == cor:
                    movimentos, _ = peca.valid(self.tabuleiro)
                    for destino in movimentos:
                        origem = peca.posicao
                        linha_destino, coluna_destino = destino
                        peca_original = self.tabuleiro[linha_destino][coluna_destino]
                        self.tabuleiro[origem[0]][origem[1]] = None
                        self.tabuleiro[linha_destino][coluna_destino] = peca
                        peca.posicao = destino

                        em_check = self.verify_check(cor)

                        self.tabuleiro[origem[0]][origem[1]] = peca
                        self.tabuleiro[linha_destino][coluna_destino] = peca_original
                        peca.posicao = origem

                        if not em_check:
                            return False
        return True
