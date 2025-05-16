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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            highlighted_square = interface.get_square_at_position(x, y)
            
            if table.tabuleiro[highlighted_square] is not None:
                prev = highlighted_square
                print('clique na peca')
            
            elif table.tabuleiro[highlighted_square] is None and prev is not None and table.tabuleiro[prev] is not None:
                print('movimentacao de ', prev, ' para ', highlighted_square)
                sucesso = table.move(table.tabuleiro[prev], highlighted_square)
                if sucesso:
                    prev = None 

            else:
                print('branco com branco ou clique inválido')
                prev = None

    interface.draw_board(highlighted_square, table.tabuleiro)
    pygame.display.flip()

pygame.quit()
