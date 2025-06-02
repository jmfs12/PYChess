"""

Função MAIN

Faz a lógica PRINCIPAL do jogo!
Faz toda a verificação e validação dos cliques nas peças:
    pega o clique na peça e marca a peça com uma cor diferente
    caso o próximo clique seja um movimento válido, faz o movimento

Faz a validação do vencedor chamando as funções de TABULEIRO

Faz a troca de cores do tabuleiro ao apertar C
"""

import pygame

# Função principal do jogo de xadrez
# Responsável por inicializar o pygame, criar a janela, gerenciar o loop principal e processar eventos
# Controla a lógica de seleção de peças, movimentação, verificação de xeque/mate e troca de turno
# Permite também trocar o tema de cores do tabuleiro ao pressionar a tecla 'C'
def main():
    pygame.init()  # Inicializa o pygame
    screen = pygame.display.set_mode((640, 640))  # Cria a janela do jogo
    pygame.display.set_caption("Jogo de Xadrez")  # Define o título da janela
    clock = pygame.time.Clock()  # Relógio para controlar FPS

    from Interface import it  # Importa interface gráfica
    from Tabuleiro import Tabuleiro  # Importa lógica do tabuleiro

    table = Tabuleiro()  # Cria o tabuleiro do jogo
    interface = it(screen)  # Cria a interface gráfica

    highlighted_square = None  # Casa selecionada
    prev = None  # Casa anterior selecionada
    running = True  # Controle do loop principal

    turn = "branco"  # Define o turno inicial

    # Lista de temas de cores para o tabuleiro
    colors = [
        ("#EEEED2", "#769656"),
        ("#E0F7FA","#006064"),
        ("#2E2E2E","#121212"),
        ("#D7CCC8","#5D4037"),
        ("#F8E8EE","#B8A1C1")
    ]

    color = colors[0]  # Tema inicial
    i=0  # Índice do tema

    # Loop principal do jogo
    while running:
        for event in pygame.event.get():  # Processa eventos
            if event.type == pygame.QUIT:
                running = False  # Sai do loop ao fechar a janela
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Captura clique do mouse e converte para coordenadas do tabuleiro
                x, y = pygame.mouse.get_pos()
                highlighted_square = interface.get_square_at_position(x, y)

                linha, coluna = highlighted_square
                peca_atual = table.tabuleiro[linha][coluna]

                # Se clicou em uma peça e nenhuma peça estava selecionada
                if peca_atual is not None and prev is None:
                    prev = highlighted_square

                # Se já havia uma peça selecionada
                elif prev is not None:
                    linha_prev, coluna_prev = prev
                    peca_prev = table.tabuleiro[linha_prev][coluna_prev]

                    # Se o movimento é válido (casa vazia ou peça inimiga)
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
                                # Troca o turno após movimento válido
                                turn = (
                                    "branco"
                                    if table.tabuleiro[linha][coluna].cor == "preto"
                                    else "preto"
                                )
                                # Verifica xeque e xeque-mate
                                if table.verify_xeque(turn):
                                    if table.not_have_moves(turn):
                                        interface.draw_winner(table.tabuleiro[linha][coluna].cor)
                                        pygame.display.flip()
                                        pygame.time.wait(5000)
                                        running = False
                                    else:
                                        print("rei de ", turn, " em xeque")
                                # verifica afogamento/empate
                                elif table.not_have_moves(turn):
                                    interface.draw()
                                    pygame.display.flip()
                                    pygame.time.wait(5000)
                                    running = False
                                else:
                                    print("movimento de:", turn)
                                highlighted_square = None
                            else:
                                highlighted_square = None
                        else:
                            print("movimento de:", turn)
                            highlighted_square = None
                        prev = None

                    # Se clicou na mesma peça, apenas atualiza seleção
                    elif peca_prev == peca_atual:
                        prev = highlighted_square

                    # Lógica do roque (rei e torre da mesma cor)
                    elif (
                        peca_prev.cor == peca_atual.cor
                        and peca_prev.tipo == "RE"
                        and peca_atual.tipo == "T"
                    ):
                        if turn == peca_prev.cor:
                            print("roque")
                            if coluna == 7:
                                highlighted_square = (linha, 6)
                                coluna = 6
                            elif coluna == 0:
                                highlighted_square = (linha, 2)
                                coluna = 2

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

                    # Clique inválido (mesma cor ou outro erro)
                    else:
                        print("branco com branco ou clique invalido")
                        prev = None
                        highlighted_square = None
            # Troca o tema de cores ao pressionar 'C'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if i < 4: 
                        i+=1
                    else:
                        i=0
                    color = colors[i]

        # Desenha o tabuleiro e peças
        interface.draw_board(highlighted_square, table.tabuleiro,color)
        pygame.display.flip()

    pygame.quit()  # Encerra o pygame

# Executa a função principal se o script for chamado diretamente
if __name__ == "__main__":
    main()