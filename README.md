# ♟️ Jogo de Xadrez em Python

Este é um projeto de jogo de xadrez desenvolvido com **Python** e **Pygame**, com suporte a movimentos básicos e especiais como **Roque**, **En Passant**, além da **Promoção** , e detecção de **check** e **fim de jogo**.

## 🎮 Funcionalidades

- Interface gráfica com Pygame.
- Suporte aos movimentos válidos de todas as peças.
- Detecção de **check**.
- Execução de **Roque** (curto e longo).
- Execução de **En passant**.
- **Promoção** do peão à rainha.
- Verificação de **fim de jogo** (sem movimentos válidos).
- Indicação do vencedor na tela.
- Mudança de cor do tabuleiro ao apertar **C**.  

## 🧠 Requisitos

- Python 3.8 ou superior
- Pygame
- Git

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/jmfs12/PYChess.git
cd PYChess
```

2. Instale as dependencias

```bash
pip install -r requirements.txt
```
3. Rode o jogo
```bash
python Main.py
```

## 🗂️ Estrutura
```graphql
pychess/
│
├── Main.py               # Loop principal do jogo
├── Peca.py               # Classe base para peças e regras de movimento
├── Tabuleiro.py          # Inicialização e controle do tabuleiro
├── Interface.py          # Desenho gráfico e interação
├── resource/             # Imagens das peças (PNG)
│   ├── peao_branco.png
│   ├── peao_preto.png
│   ├── bispo_branco.png
│   ├── bispo_preto.png
│   ├── cavalo_branco.png
│   ├── cavalo_preto.png
│   ├── torre_branco.png
│   ├── torre_preto.png
│   ├── rei_branco.png
│   ├── rei_preto.png
│   └── rainha_branco.png
│
└── README.md             # Este arquivo
```

## 📝 Licença
Este projeto está sob a licença MIT.

## 🙋‍♂️ Autor
Desenvolvido por João Miguel. Sinta-se livre para contribuir ou reportar bugs.
