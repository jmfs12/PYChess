import pygame

class it:
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self, highlight=None, table=None):
        colors = [pygame.Color('#EEEED2'), pygame.Color('#769656')]
        square_size = 80

        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)

                if highlight == (row, col):
                    pygame.draw.rect(self.screen, pygame.Color('#8FBC8F'), rect)
                else:
                    pygame.draw.rect(self.screen, color, rect)

                peca = table[row][col]
                if peca is not None:
                    self.screen.blit(peca.resource, (col * square_size, row * square_size))

    def get_square_at_position(self, x, y):
        square_size = 80
        col = x // square_size
        row = y // square_size
        return row, col
