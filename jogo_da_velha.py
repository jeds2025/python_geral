import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.geometry("300x325")
        self.reset_game()

    def reset_game(self):
        self.tabuleiro = [""] * 9
        self.jogador_atual = "X"
        self.botoes = []
        self.criar_botoes()

    def criar_botoes(self):
        for i in range(9):
            botao = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                              command=lambda i=i: self.jogar(i))
            botao.grid(row=i // 3, column=i % 3)
            self.botoes.append(botao)

    def jogar(self, pos):
        if self.tabuleiro[pos] == "":
            self.tabuleiro[pos] = self.jogador_atual
            self.botoes[pos].config(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.reset_game()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_game()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        combinacoes_vitoria = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)              # Diagonais
        ]
        for a, b, c in combinacoes_vitoria:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
