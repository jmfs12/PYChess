import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Jogo de Xadrez")
clock = pygame.time.Clock()

imgs = ['resource/peao_branco.png', 'resource/torre_branco.png', 'resource/cavalo_branco.png', 'resource/bispo_branco.png', 'resource/rainha_branco.png', 'resource/rei_branco.png',
        'resource/peao_preto.png', 'resource/torre_preto.png', 'resource/cavalo_preto.png', 'resource/bispo_preto.png', 'resource/rainha_preto.png', 'resource/rei_preto.png']

pecas_brancas = [pygame.image.load(imgs[i]).convert_alpha() for i in range (6)]
pecas_pretas = [pygame.image.load(imgs[i]).convert_alpha() for i in range (6,12)]

for i in range(6):
    pecas_brancas[i] = pygame.transform.smoothscale(pecas_brancas[i], (80, 80))

for i in range(6):
    pecas_pretas[i] = pygame.transform.smoothscale(pecas_pretas[i], (80, 80))


def draw_board(highlight):
    colors = [pygame.Color('#EEEED2'), pygame.Color('#769656')]
    square_size = 80
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(col*square_size, row*square_size, square_size, square_size)
    
            if highlight == (row,col):
                pygame.draw.rect(screen, pygame.Color('#8FBC8F'), rect)
            else:
                pygame.draw.rect(screen,color,rect)

    for row in range(8):
        i, flag = 1, False
        for col in range(8):
            if row == 1:
                screen.blit(pecas_pretas[0], (col * square_size, row * square_size))
            elif row == 6:
                screen.blit(pecas_brancas[0], (col * square_size, row * square_size))
            elif row == 0:
                screen.blit(pecas_pretas[i], (col * square_size, row * square_size))
                if not flag:
                    i+=1
                if flag:
                    i-=1
                if col == 4:
                    i-=3
                    flag = True
            elif row == 7:
                screen.blit(pecas_brancas[i], (col * square_size, row * square_size))
                if not flag:
                    i+=1
                if flag:
                    i-=1
                if col == 4:
                    i-=3
                    flag = True

def get_square_at_position(x, y):
    square_size = 80
    col = x // square_size
    row = y // square_size
    return row, col

running = True
highlighted_square = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            highlighted_square = get_square_at_position(x,y)

    draw_board(highlighted_square)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
