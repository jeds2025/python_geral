import tkinter as tk
import random

# Configuração do tabuleiro
TAMANHO = 8
TAMANHO_CELULA = 60

class JogoDeDamas:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Damas")
        self.canvas = tk.Canvas(root, width=TAMANHO*TAMANHO_CELULA, height=TAMANHO*TAMANHO_CELULA)
        self.canvas.pack()
        self.pecas = {}  # Armazena posições das peças
        self.jogador_cor = None
        self.computador_cor = None
        self.turno = None
        self.selecionada = None
        self.criar_tabuleiro()
        self.colocar_pecas()
        self.inicializar_selecao_de_cor()

    def criar_tabuleiro(self):
        """Desenha o tabuleiro com células alternadas."""
        for linha in range(TAMANHO):
            for coluna in range(TAMANHO):
                cor = "white" if (linha + coluna) % 2 == 0 else "gray"
                x1 = coluna * TAMANHO_CELULA
                y1 = linha * TAMANHO_CELULA
                x2 = x1 + TAMANHO_CELULA
                y2 = y1 + TAMANHO_CELULA
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor)

    def colocar_pecas(self):
        """Posiciona peças pretas e brancas no tabuleiro."""
        for linha in range(3):  # Peças pretas
            for coluna in range(TAMANHO):
                if (linha + coluna) % 2 != 0:
                    self.adicionar_peca(linha, coluna, "black")
        for linha in range(5, TAMANHO):  # Peças brancas
            for coluna in range(TAMANHO):
                if (linha + coluna) % 2 != 0:
                    self.adicionar_peca(linha, coluna, "white")

    def adicionar_peca(self, linha, coluna, cor):
        """Adiciona uma peça na posição especificada."""
        x1 = coluna * TAMANHO_CELULA + 10
        y1 = linha * TAMANHO_CELULA + 10
        x2 = x1 + TAMANHO_CELULA - 20
        y2 = y1 + TAMANHO_CELULA - 20
        peca = self.canvas.create_oval(x1, y1, x2, y2, fill=cor)
        self.pecas[(linha, coluna)] = peca

    def inicializar_selecao_de_cor(self):
        """Permite ao jogador selecionar a cor clicando em uma peça."""
        self.root.title("Clique em uma peça para escolher sua cor")
        self.canvas.bind("<Button-1>", self.selecionar_cor)

    def selecionar_cor(self, event):
        """Define a cor do jogador com base na peça clicada."""
        coluna = event.x // TAMANHO_CELULA
        linha = event.y // TAMANHO_CELULA
        peca = self.pecas.get((linha, coluna))
        if peca:
            cor = self.canvas.itemcget(peca, "fill")
            if cor in ["black", "white"]:
                self.jogador_cor = cor
                self.computador_cor = "black" if cor == "white" else "white"
                self.turno = "white"  # Branco sempre começa
                self.canvas.unbind("<Button-1>")
                self.root.title("Jogo de Damas")
                self.iniciar_jogo()

    def iniciar_jogo(self):
        """Inicia o jogo e ativa os eventos necessários."""
        self.canvas.bind("<Button-1>", self.manipular_clique)

    def manipular_clique(self, event):
        """Gerencia cliques do jogador no tabuleiro."""
        if self.turno != self.jogador_cor:
            return  # Ignora cliques fora do turno do jogador

        coluna = event.x // TAMANHO_CELULA
        linha = event.y // TAMANHO_CELULA

        if self.selecionada:
            if self.movimento_valido(self.selecionada, (linha, coluna)):
                self.mover_peca(self.selecionada, (linha, coluna))
                self.selecionada = None
                self.turno = self.computador_cor
                self.computador_jogar()
            else:
                self.selecionada = None
        else:
            if (linha, coluna) in self.pecas and self.e_peca_do_jogador(linha, coluna):
                self.selecionada = (linha, coluna)

    def e_peca_do_jogador(self, linha, coluna):
        """Verifica se uma peça pertence ao jogador atual."""
        peca = self.pecas.get((linha, coluna))
        if peca:
            cor = self.canvas.itemcget(peca, "fill")
            return cor == self.jogador_cor
        return False

    def movimento_valido(self, origem, destino):
        """Valida se o movimento é permitido."""
        linha_origem, coluna_origem = origem
        linha_destino, coluna_destino = destino

        # Movimento diagonal simples (1 célula)
        if abs(linha_destino - linha_origem) == 1 and abs(coluna_destino - coluna_origem) == 1:
            return (linha_destino, coluna_destino) not in self.pecas  # Verifica se o destino está vazio
        return False

    def mover_peca(self, origem, destino):
        """Move uma peça de uma posição para outra."""
        linha_origem, coluna_origem = origem
        linha_destino, coluna_destino = destino
        peca = self.pecas.pop(origem)
        x1 = coluna_destino * TAMANHO_CELULA + 10
        y1 = linha_destino * TAMANHO_CELULA + 10
        x2 = x1 + TAMANHO_CELULA - 20
        y2 = y1 + TAMANHO_CELULA - 20
        self.canvas.coords(peca, x1, y1, x2, y2)
        self.pecas[(linha_destino, coluna_destino)] = peca

    def computador_jogar(self):
        """Realiza a jogada do computador."""
        movimentos = []
        for (linha, coluna), peca in self.pecas.items():
            if self.canvas.itemcget(peca, "fill") == self.computador_cor:
                destino1 = (linha + 1, coluna + 1)
                destino2 = (linha + 1, coluna - 1)
                if self.movimento_valido((linha, coluna), destino1):
                    movimentos.append(((linha, coluna), destino1))
                if self.movimento_valido((linha, coluna), destino2):
                    movimentos.append(((linha, coluna), destino2))

        if movimentos:
            movimento = random.choice(movimentos)
            self.mover_peca(*movimento)
        else:
            print("Computador não pode realizar movimentos válidos.")
        self.turno = self.jogador_cor

# Inicializa o jogo
root = tk.Tk()
jogo = JogoDeDamas(root)
root.mainloop()
