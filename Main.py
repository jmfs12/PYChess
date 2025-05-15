import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Jogo de Xadrez")
clock = pygame.time.Clock()

import Interface as it
#from Player import Player

#player1 = Player('branco')

running = True
highlighted_square = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            highlighted_square = it.get_square_at_position(x,y)

    it.draw_board(highlighted_square, screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
