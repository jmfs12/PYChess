import pygame


class it:
    def __init__(self, screen):
        self.screen = screen

    def draw_board(self, highlight=None, table=None, color=None):
        colors = [pygame.Color(color[0]), pygame.Color(color[1])]
        square_size = 80

        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                rect = pygame.Rect(
                    col * square_size, row * square_size, square_size, square_size
                )

                if highlight == (row, col):
                    pygame.draw.rect(self.screen, pygame.Color("#8FBC8F"), rect)
                else:
                    pygame.draw.rect(self.screen, color, rect)

                peca = table[row][col]
                if peca is not None:
                    self.screen.blit(
                        peca.resource, (col * square_size, row * square_size)
                    )

    def get_square_at_position(self, x, y):
        square_size = 80
        col = x // square_size
        row = y // square_size
        return row, col
    
    def draw_winner(self, cor):
        font = pygame.font.SysFont("Arial", 48, bold=True)
        texto = f"{cor.capitalize()} venceu!"
        texto_surface = font.render(texto, True, pygame.Color('white'))
        texto_rect = texto_surface.get_rect(center=(640 // 2, 640 // 2))

        # Fundo semi-transparente
        overlay = pygame.Surface((640, 640))
        overlay.set_alpha(180)  # Transparência
        overlay.fill((0, 0, 0))  # Cor preta

        self.screen.blit(overlay, (0, 0))
        self.screen.blit(texto_surface, texto_rect)


