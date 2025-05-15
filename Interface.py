import pygame
from Peca import Peca
from Player import Player
from Tabuleiro import Tabuleiro

isMark = False
rc = None

pecas_brancas = {
    (i, j) : None
    for i in range(8)
    for j in range(8)
}


for i in range(8):
    for j in range(8):
        if (i,j) == (7,0) or (i,j) == (7,7):
            pecas_brancas[(i,j)] = (Peca('T', (i,j), pygame.image.load('resource/torre_branco.png')))
        elif (i,j) == (7,1) or (i,j) == (7,6):
            pecas_brancas[(i,j)] = (Peca('C', (i,j), pygame.image.load('resource/cavalo_branco.png')))       
        elif (i,j) == (7,2) or (i,j) == (7,5):
            pecas_brancas[(i,j)] = (Peca('B', (i,j), pygame.image.load('resource/bispo_branco.png')))       
        elif (i,j) == (7,3):
            pecas_brancas[(i,j)] = (Peca('RA', (i,j), pygame.image.load('resource/rainha_branco.png')))  
        elif (i,j) == (7,4):
            pecas_brancas[(i,j)] = (Peca('RE', (i,j), pygame.image.load('resource/rei_branco.png'))) 
        elif i == 6:
            pecas_brancas[(i,j)] = (Peca('P', (i,j), pygame.image.load('resource/peao_branco.png'))) 
            
player_branco = Player('branco', pecas_brancas)

pecas_pretas = {
    (i, j) : None
    for i in range(8)
    for j in range(8)
}
for i in range(8):
    for j in range(8):
        if (i,j) == (0,0) or (i,j) == (0,7):
            pecas_pretas[(i,j)] = (Peca('T', (i,j), pygame.image.load('resource/torre_preto.png')))
        elif (i,j) == (0,1) or (i,j) == (0,6):
            pecas_pretas[(i,j)] = (Peca('C', (i,j), pygame.image.load('resource/cavalo_preto.png')))       
        elif (i,j) == (0,2) or (i,j) == (0,5):
            pecas_pretas[(i,j)] = (Peca('B', (i,j), pygame.image.load('resource/bispo_preto.png')))       
        elif (i,j) == (0,3):
            pecas_pretas[(i,j)] = (Peca('RA', (i,j), pygame.image.load('resource/rainha_preto.png')))  
        elif (i,j) == (0,4):
            pecas_pretas[(i,j)] = (Peca('RE', (i,j), pygame.image.load('resource/rei_preto.png'))) 
        elif i == 1:
            pecas_pretas[(i,j)] = (Peca('P', (i,j), pygame.image.load('resource/peao_preto.png'))) 


def draw_board(highlight, screen):
    colors = [pygame.Color('#EEEED2'), pygame.Color('#769656')]
    square_size = 80
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(col*square_size, row*square_size, square_size, square_size)
    
            if highlight == (row,col):
                if not isMark:
                    pygame.draw.rect(screen, pygame.Color('#8FBC8F'), rect)
                    isMark = True
                    rc = rect
                else:
                    player_branco.move(player_branco.pecas[(rc.x//80, rc.y//80)], highlight, Tabuleiro.tabuleiro, screen)

            else:
                pygame.draw.rect(screen,color,rect)

    for row in range(6,8):
        for col in range(8):
            if (row, col) in pecas_brancas:
                screen.blit(pecas_brancas[(row, col)].resource, (col*80, row*80))

    
    for row in range(0,2):
        for col in range(8):
            if (row, col) in pecas_pretas:
                screen.blit(pecas_pretas[(row, col)].resource, (col*80, row*80))
            

def get_square_at_position(x, y):
    square_size = 80
    col = x // square_size
    row = y // square_size
    return row, col