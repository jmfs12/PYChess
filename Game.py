import Tabuleiro
import Player

def main():
    
    t = Tabuleiro.Tabuleiro()  
    t.print_board()
    p = Player.Player("branco")

    print("Movimentos possiveis: ", t.tabuleiro[t.index["B2"]].valid(t.tabuleiro))
    p.move(t.tabuleiro[t.index["B2"]], t.index["B4"], t.tabuleiro, t.board)
    t.print_board()

    print("Movimentos possiveis: ", t.tabuleiro[t.index["C1"]].valid(t.tabuleiro))
    p.move(t.tabuleiro[t.index["C1"]], t.index["B2"], t.tabuleiro, t.board)
    t.print_board()

    

if __name__ == '__main__':
    main()
