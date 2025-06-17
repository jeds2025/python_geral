import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("400x400")
        self.palavras = ["python", "programacao", "desenvolvimento", "jogo", "computador"]
        self.letras_adivinhadas = []
        self.erros = 0
        self.max_erros = 6

        # Widgets permanentes
        self.label_palavra = tk.Label(self.root, font=("Arial", 24))
        self.label_palavra.pack(pady=20)

        self.label_erros = tk.Label(self.root, font=("Arial", 16))
        self.label_erros.pack(pady=10)

        self.entry_letra = tk.Entry(self.root, font=("Arial", 16))
        self.entry_letra.pack(pady=10)
        self.entry_letra.bind("<Return>", self.adivinhar_letra)

        self.btn_reset = tk.Button(self.root, text="Reiniciar", command=self.reset_game)
        self.btn_reset.pack(pady=10)

        self.reset_game()

    def reset_game(self):
        self.palavra = random.choice(self.palavras)
        self.letras_adivinhadas = []
        self.erros = 0
        self.atualizar_display()

    def atualizar_display(self):
        # Atualiza os textos dos widgets
        self.label_palavra.config(text=self.obter_palavra_display())
        self.label_erros.config(text=f"Erros: {self.erros}/{self.max_erros}")
        self.entry_letra.delete(0, tk.END)

    def obter_palavra_display(self):
        return " ".join([letra if letra in self.letras_adivinhadas else "_" for letra in self.palavra])

    def adivinhar_letra(self, event):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Entrada Inválida", "Digite apenas uma letra!")
            return

        if letra in self.letras_adivinhadas:
            messagebox.showinfo("Letra Repetida", f"Você já tentou a letra '{letra}'.")
            return

        self.letras_adivinhadas.append(letra)

        if letra not in self.palavra:
            self.erros += 1

        if self.erros >= self.max_erros:
            messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era: {self.palavra}")
            self.reset_game()
        elif all(letra in self.letras_adivinhadas for letra in self.palavra):
            messagebox.showinfo("Fim de Jogo", "Você ganhou!")
            self.reset_game()
        else:
            self.atualizar_display()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()
