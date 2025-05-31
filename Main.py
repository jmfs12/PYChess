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

turn = 'branco'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            highlighted_square = interface.get_square_at_position(x, y)
            
            if table.tabuleiro[highlighted_square] is not None and prev is None:
                prev = highlighted_square
                print('clique na peca')
            
            elif prev is not None and table.tabuleiro[prev] is not None and (table.tabuleiro[highlighted_square] is None or table.tabuleiro[highlighted_square].cor != table.tabuleiro[prev].cor):
                if(turn == table.tabuleiro[prev].cor):
                    print('movimentacao de ', table.tabuleiro[prev].tipo, table.tabuleiro[prev].cor, ' para ', highlighted_square)
                    sucesso = table.move(table.tabuleiro[prev], highlighted_square)
                    if sucesso:
                        turn = 'branco' if table.tabuleiro[highlighted_square].cor == 'preto' else 'preto'
                        if table.verify_check(turn):
                            if table.not_have_moves(turn):
                                print('o jogador ', table.tabuleiro[highlighted_square].cor, 'ganhou')
                            else:
                                print('rei de ', turn, ' em check')
                        highlighted_square = None
                    else:
                        highlighted_square = None
                else:
                    print('movimento de:', turn)
                    highlighted_square = None
                prev = None
                
            elif prev is not None and table.tabuleiro[prev] == table.tabuleiro[highlighted_square]:
                prev = highlighted_square
            
            elif prev is not None and highlighted_square is not None and table.tabuleiro[prev].cor == table.tabuleiro[highlighted_square].cor and (table.tabuleiro[prev].tipo == 'RE' and table.tabuleiro[highlighted_square].tipo == 'T'):
                if(turn == table.tabuleiro[prev].cor):  
                    print('roque')
                    if highlighted_square[1] == 7:
                        highlighted_square = (highlighted_square[0], 6)
                    elif highlighted_square[1] == 0:
                        highlighted_square = (highlighted_square[0], 2)

                    sucesso = table.move(table.tabuleiro[prev], highlighted_square)
                    if sucesso:
                        turn = 'branco' if table.tabuleiro[highlighted_square].cor == 'preto' else 'preto'
                        highlighted_square = None
                    else:
                        print('movimento de:', turn)
                        highlighted_square = None
                    prev = None
                else:
                    print
            else:
                print('branco com branco ou clique inválido')
                prev = None

    interface.draw_board(highlighted_square, table.tabuleiro)
    pygame.display.flip()

pygame.quit()
