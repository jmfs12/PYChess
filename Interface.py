"""

Classe INTERFACE

É responsável pelo desenho e REdesenho do tabuleiro.
Desenha cada quadrado e cada peça em seu devido lugar ultilizando o atributo POSIÇÃO de cada peça
Desenha o vencedor na tela após a vitória
"""

import pygame

# Classe responsável pela interface gráfica do jogo de xadrez
class it:
    def __init__(self, screen):
        self.screen = screen  # Tela onde tudo será desenhado

    # Desenha o tabuleiro, as peças e destaca a casa selecionada
    # highlight: casa a ser destacada
    # table: matriz com as peças
    # color: tupla com as cores do tabuleiro
    def draw_board(self, highlight=None, table=None, color=None):
        colors = [pygame.Color(color[0]), pygame.Color(color[1])]  # Cores do tabuleiro
        square_size = 80  # Tamanho de cada quadrado

        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]  # Alterna as cores
                rect = pygame.Rect(
                    col * square_size, row * square_size, square_size, square_size
                )

                # Destaca a casa selecionada
                if highlight == (row, col):
                    pygame.draw.rect(self.screen, pygame.Color("#8FBC8F"), rect)
                else:
                    pygame.draw.rect(self.screen, color, rect)

                # Desenha a peça na casa, se houver
                peca = table[row][col]
                if peca is not None:
                    self.screen.blit(
                        peca.resource, (col * square_size, row * square_size)
                    )

    # Converte coordenadas de pixel para coordenadas do tabuleiro
    def get_square_at_position(self, x, y):
        square_size = 80
        col = x // square_size
        row = y // square_size
        return row, col
    
    # Exibe o vencedor na tela com sobreposição escura
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

    def draw(self):
        font = pygame.font.SysFont("Arial", 48, bold=True)
        texto = "Empate"
        texto_surface = font.render(texto, True, pygame.Color('white'))
        texto_rect = texto_surface.get_rect(center=(640 // 2, 640 // 2))

        # Fundo semi-transparente
        overlay = pygame.Surface((640, 640))
        overlay.set_alpha(180)  # Transparência
        overlay.fill((0, 0, 0))  # Cor preta

        self.screen.blit(overlay, (0, 0))
        self.screen.blit(texto_surface, texto_rect)


