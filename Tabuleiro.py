"""

Classe TABULEIRO

Cria a matriz do tabuleiro e inicializa com cada peça em sua posição inicial, e faz LOAD no resource(imagem) de cada uma
Faz toda a lógica de MOVIMENTAÇÃO de cada peça:
    verifica se a peça tem movimentos válidos, caso não retorna False
    caso sim, faz a movimentação correta

    Contém a lógica de EN PASSANT e ROQUE

Faz a verificação se o REI está em XEQUE
e Verifica se não tem movimentos possíveis de serem feitos (XEQUE MATE)
"""

from Peca import Peca
import pygame as py

# Classe responsável pela lógica do tabuleiro e das regras do xadrez
class Tabuleiro:

    def __init__(self):
        # Cria a matriz 8x8 do tabuleiro, preenchida inicialmente com None
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]

        # Inicializa os peões nas linhas 1 (pretos) e 6 (brancos)
        for i in range(8):
            self.tabuleiro[1][i] = Peca(
                "P", (1, i), py.image.load("resource/peao_preto.png")
            )
            self.tabuleiro[6][i] = Peca(
                "P", (6, i), py.image.load("resource/peao_branco.png")
            )

        # Lista com a ordem das peças principais
        tipos = ["T", "C", "B", "RA", "RE", "B", "C", "T"]
        # Caminhos das imagens das peças brancas
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
        # Caminhos das imagens das peças pretas
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

        # Inicializa as peças principais nas colunas corretas
        for col, tipo in enumerate(tipos):
            self.tabuleiro[7][col] = Peca(
                tipo, (7, col), py.image.load(resources_branco[col])
            )
            self.tabuleiro[0][col] = Peca(
                tipo, (0, col), py.image.load(resources_preto[col])
            )

        self.ultimo_movimento = None  # Guarda o último movimento realizado

    # Realiza a movimentação de uma peça, se for válida
    # Retorna True se o movimento foi feito, False caso contrário
    def move(self, peca, posicao) -> bool:
        movimentos, tipo_mov = peca.valid(self.tabuleiro, self.ultimo_movimento)
        print('movimentos validos para a peça: ', peca.tipo, peca.cor, ' ', movimentos)

        # Verifica se o movimento é permitido ou se é roque
        if posicao in movimentos or tipo_mov == "roque":
            linha_origem, coluna_origem = peca.posicao
            linha_destino, coluna_destino = posicao
            tab_antes = self.tabuleiro[linha_destino][coluna_destino]
            self.tabuleiro[linha_origem][coluna_origem] = None
            self.tabuleiro[linha_destino][coluna_destino] = peca
            origem = peca.posicao

            posicao_ant, inicial_ant = peca.posicao, peca.inicial
            peca.posicao, peca.inicial = posicao, False

            # Verifica se o movimento deixa o rei em xeque (movimento ilegal)
            if self.verify_xeque(peca.cor):
                print("rei em xeque")
                self.tabuleiro[linha_origem][coluna_origem] = peca
                self.tabuleiro[linha_destino][coluna_destino] = tab_antes
                peca.posicao, peca.inicial = posicao_ant, inicial_ant
                print("movimentacao recusada")
                return False

            # Lógica do roque: move a torre junto com o rei
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

            # Lógica do en passant
            if tipo_mov == 'en passant':
                print("en passant")
                linha_capturada = origem[0] if peca.cor == 'branco' else origem[0]
                pos_captura = (linha_capturada, posicao[1])
                self.tabuleiro[pos_captura[0]][pos_captura[1]] = None

            # Atualiza o último movimento
            self.ultimo_movimento = (peca, origem, posicao)
            print(self.ultimo_movimento[0].tipo, ' ', self.ultimo_movimento[1], ' ', self.ultimo_movimento[2])                
                
            # Promoção do peão: transforma em rainha ao chegar no final
            if peca.tipo == 'P':
                if (peca.cor == 'branco' and linha_destino == 0) or (peca.cor == 'preto' and linha_destino == 7):
                    self.tabuleiro[linha_destino][coluna_destino] = Peca('RA', (linha_destino, coluna_destino), py.image.load(f"resource/rainha_{peca.cor}.png"))
                    self.tabuleiro[linha_destino][coluna_destino].cor = peca.cor
            print("movimentação feita")
            return True

        print("movimentação recusada")
        return False

    # Verifica se o rei da cor informada está em xeque
    def verify_xeque(self, cor):
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
            movimentos, _ = peca.valid(self.tabuleiro, self.ultimo_movimento)
            movimentos_inimigo.extend(movimentos)

        return rei.posicao in movimentos_inimigo

    # Verifica se a cor informada não possui nenhum movimento legal (xeque-mate ou empate)
    def not_have_moves(self, cor):
        for linha in self.tabuleiro:
            for peca in linha:
                if peca is not None and peca.cor == cor:
                    movimentos, _ = peca.valid(self.tabuleiro, self.ultimo_movimento)
                    for destino in movimentos:
                        origem = peca.posicao
                        linha_destino, coluna_destino = destino
                        peca_original = self.tabuleiro[linha_destino][coluna_destino]
                        self.tabuleiro[origem[0]][origem[1]] = None
                        self.tabuleiro[linha_destino][coluna_destino] = peca
                        peca.posicao = destino

                        em_xeque = self.verify_xeque(cor)

                        self.tabuleiro[origem[0]][origem[1]] = peca
                        self.tabuleiro[linha_destino][coluna_destino] = peca_original
                        peca.posicao = origem

                        if not em_xeque:
                            return False
        return True
