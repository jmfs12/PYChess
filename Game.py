import Tabuleiro

def main():
    
    t = Tabuleiro.Tabuleiro()
    print(t.tabuleiro[t.index["B2"]].valid(t.tabuleiro))

if __name__ == '__main__':
    main()
