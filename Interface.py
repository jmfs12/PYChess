import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Jogo de Xadrez")
clock = pygame.time.Clock()

def draw_board():
    colors = [pygame.Color('#EEEED2'), pygame.Color('#769656')]
    square_size = 80
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*square_size, row*square_size, square_size, square_size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
