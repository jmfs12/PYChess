import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Jogo de Xadrez")
clock = pygame.time.Clock()

from Interface import it
from Tabuleiro import Tabuleiro

table = Tabuleiro()
interface = it(screen)

highlighted_square = None
prev = None
running = True

turn = "branco"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            highlighted_square = interface.get_square_at_position(x, y)

            linha, coluna = highlighted_square
            peca_atual = table.tabuleiro[linha][coluna]

            if peca_atual is not None and prev is None:
                prev = highlighted_square
                print("clique na peca")

            elif prev is not None:
                linha_prev, coluna_prev = prev
                peca_prev = table.tabuleiro[linha_prev][coluna_prev]

                if peca_prev is not None and (
                    peca_atual is None or peca_atual.cor != peca_prev.cor
                ):
                    if turn == peca_prev.cor:
                        print(
                            "movimentacao de ",
                            peca_prev.tipo,
                            peca_prev.cor,
                            " para ",
                            highlighted_square,
                        )
                        sucesso = table.move(peca_prev, highlighted_square)
                        if sucesso:
                            turn = (
                                "branco"
                                if table.tabuleiro[linha][coluna].cor == "preto"
                                else "preto"
                            )
                            if table.verify_check(turn):
                                if table.not_have_moves(turn):
                                    print(
                                        "o jogador ",
                                        table.tabuleiro[linha][coluna].cor,
                                        "ganhou",
                                    )
                                    interface.draw_winner(table.tabuleiro[linha][coluna].cor)
                                    pygame.display.flip()
                                    pygame.time.wait(5000)
                                    running = False
                                else:
                                    print("rei de ", turn, " em check")
                            highlighted_square = None
                        else:
                            highlighted_square = None
                    else:
                        print("movimento de:", turn)
                        highlighted_square = None
                    prev = None

                elif peca_prev == peca_atual:
                    prev = highlighted_square

                elif (
                    peca_prev.cor == peca_atual.cor
                    and peca_prev.tipo == "RE"
                    and peca_atual.tipo == "T"
                ):
                    if turn == peca_prev.cor:
                        print("roque")
                        if coluna == 7:
                            highlighted_square = (linha, 6)
                        elif coluna == 0:
                            highlighted_square = (linha, 2)

                        sucesso = table.move(peca_prev, highlighted_square)
                        if sucesso:
                            turn = (
                                "branco"
                                if table.tabuleiro[linha][coluna].cor == "preto"
                                else "preto"
                            )
                            highlighted_square = None
                        else:
                            print("movimento de:", turn)
                            highlighted_square = None
                        prev = None

                else:
                    print("branco com branco ou clique invalido")
                    prev = None
                    highlighted_square = None

    interface.draw_board(highlighted_square, table.tabuleiro)
    pygame.display.flip()

pygame.quit()
