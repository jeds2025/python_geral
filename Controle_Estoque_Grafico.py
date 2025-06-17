import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import locale
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Configurando o locale para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Produto:
    def __init__(self, codigo, nome, quantidade, valor, categoria):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.categoria = categoria

    def __repr__(self):
        return f"{self.codigo}: {self.nome} - {self.quantidade} unidades - R${self.valor:.2f} - {self.categoria}"

class ControleEstoque:
    def __init__(self, root):
        self.estoque = {}
        self.carregar_estoque()
        self.root = root
        self.root.title("Controle de Estoque")
        self.root.geometry("1000x500")  # Largura ajustada para acomodar a nova coluna

        self.frame_entradas = tk.Frame(root)
        self.frame_entradas.pack(pady=10)

        # Campo Código
        self.label_codigo = tk.Label(self.frame_entradas, text="Código", fg="red", font=("Arial", 12, "bold"))
        self.label_codigo.grid(row=0, column=0, padx=5, pady=5)
        self.entry_codigo = tk.Entry(self.frame_entradas)
        self.entry_codigo.grid(row=1, column=0, padx=5, pady=5)
        self.entry_codigo.bind("<Return>", self.focus_next_widget)
        self.entry_codigo.bind("<Tab>", self.focus_next_widget)

        # Campo Nome
        self.label_nome = tk.Label(self.frame_entradas, text="Nome", fg="red", font=("Arial", 12, "bold"))
        self.label_nome.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame_entradas)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)
        self.entry_nome.bind("<Return>", self.focus_next_widget)
        self.entry_nome.bind("<Tab>", self.focus_next_widget)

        # Campo Quantidade
        self.label_quantidade = tk.Label(self.frame_entradas, text="Quantidade", fg="red", font=("Arial", 12, "bold"))
        self.label_quantidade.grid(row=0, column=2, padx=5, pady=5)
        self.entry_quantidade = tk.Entry(self.frame_entradas)
        self.entry_quantidade.grid(row=1, column=2, padx=5, pady=5)
        self.entry_quantidade.bind("<Return>", self.focus_next_widget)
        self.entry_quantidade.bind("<Tab>", self.focus_next_widget)

        # Campo Valor
        self.label_valor = tk.Label(self.frame_entradas, text="Valor", fg="red", font=("Arial", 12, "bold"))
        self.label_valor.grid(row=0, column=3, padx=5, pady=5)
        self.entry_valor = tk.Entry(self.frame_entradas)
        self.entry_valor.grid(row=1, column=3, padx=5, pady=5)
        self.entry_valor.bind("<Return>", self.focus_next_widget)
        self.entry_valor.bind("<Tab>", self.focus_next_widget)

        # Campo Categoria
        self.label_categoria = tk.Label(self.frame_entradas, text="Categoria", fg="red", font=("Arial", 12, "bold"))
        self.label_categoria.grid(row=0, column=4, padx=5, pady=5)
        self.entry_categoria = tk.Entry(self.frame_entradas)
        self.entry_categoria.grid(row=1, column=4, padx=5, pady=5)
        self.entry_categoria.bind("<Return>", self.focus_next_widget)
        self.entry_categoria.bind("<Tab>", self.focus_next_widget)

        # Configuração da Listbox e Scrollbar
        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.pack(pady=10)
        self.listbox = tk.Listbox(self.listbox_frame, width=130, height=18, font=("Courier", 10))
        self.listbox.pack(side=tk.LEFT, padx=10)
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Botões de Ação
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=10)

        self.btn_incluir = tk.Button(self.frame_botoes, text="Incluir", fg="blue", font=("Arial", 12, "bold"), command=self.incluir_produto)
        self.btn_incluir.grid(row=0, column=0, padx=5, pady=5)

        self.btn_excluir = tk.Button(self.frame_botoes, text="Excluir", fg="blue", font=("Arial", 12, "bold"), command=self.excluir_produto)
        self.btn_excluir.grid(row=0, column=1, padx=5, pady=5)

        self.btn_alterar = tk.Button(self.frame_botoes, text="Alterar", fg="blue", font=("Arial", 12, "bold"), command=self.alterar_produto)
        self.btn_alterar.grid(row=0, column=2, padx=5, pady=5)

        self.btn_consultar = tk.Button(self.frame_botoes, text="Consultar", fg="blue", font=("Arial", 12, "bold"), command=self.consultar_produto)
        self.btn_consultar.grid(row=0, column=3, padx=5, pady=5)

        self.btn_listar = tk.Button(self.frame_botoes, text="Listar", fg="blue", font=("Arial", 12, "bold"), command=self.listar_produtos)
        self.btn_listar.grid(row=0, column=4, padx=5, pady=5)

        self.btn_mostrar_total = tk.Button(self.frame_botoes, text="Saldos", fg="blue", font=("Arial", 12, "bold"), command=self.mostrar_total)
        self.btn_mostrar_total.grid(row=0, column=5, padx=5, pady=5)

        self.btn_backup = tk.Button(self.frame_botoes, text="Backup", fg="blue", font=("Arial", 12, "bold"), command=self.backup)
        self.btn_backup.grid(row=0, column=6, padx=5, pady=5)

        self.btn_restaurar = tk.Button(self.frame_botoes, text="Restaurar", fg="orange", font=("Arial", 12, "bold"), command=self.restaurar)
        self.btn_restaurar.grid(row=0, column=7, padx=5, pady=5)

        self.btn_imprimir = tk.Button(self.frame_botoes, text="Imprimir Estoque", fg="blue", font=("Arial", 12, "bold"), command=self.imprimir_lista_produtos)
        self.btn_imprimir.grid(row=0, column=8, padx=5, pady=5)

        self.btn_sair = tk.Button(self.frame_botoes, text="Sair", fg="red", font=("Arial", 12, "bold"), command=self.sair)
        self.btn_sair.grid(row=0, column=9, padx=5, pady=5)

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def carregar_estoque(self):
        try:
            with open("estoque.json", "r") as file:
                estoque_carregado = json.load(file)
                self.estoque = {}
                for codigo, dados in estoque_carregado.items():
                    # Verifica se a categoria está vazia ou ausente; se sim, atribui "Sem Categoria"
                    if not dados.get("categoria", "").strip():
                        dados["categoria"] = "Sem Categoria"
                    self.estoque[codigo] = Produto(**dados)
        except FileNotFoundError:
            messagebox.showinfo("Info", "Arquivo de estoque não encontrado. Um novo será criado.")

    def salvar_estoque(self):
        with open("estoque.json", "w") as file:
            json.dump({codigo: produto.__dict__ for codigo, produto in self.estoque.items()}, file)
        messagebox.showinfo("Info", "Estoque salvo com sucesso!")

    def incluir_produto(self):
        codigo = self.entry_codigo.get().strip()
        if codigo in self.estoque:
            messagebox.showinfo("Info", "Este código já existe.")
            opcao = messagebox.askyesno("Info", "Deseja acrescentar itens ao produto existente?")
            if opcao:
                quantidade = simpledialog.askinteger("Entrada", "Digite a quantidade de itens a acrescentar:")
                self.estoque[codigo].quantidade += quantidade
                messagebox.showinfo("Info", "Quantidade atualizada com sucesso!")
                self.salvar_estoque()
                return
            else:
                return

        nome = self.entry_nome.get().strip()
        try:
            quantidade = int(self.entry_quantidade.get())
            valor = float(self.entry_valor.get())
        except ValueError:
            messagebox.showinfo("Info", "Quantidade ou Valor inválido!")
            return
        # Se o campo de categoria estiver vazio, atribui "Sem Categoria"
        categoria = self.entry_categoria.get().strip() or "Sem Categoria"
        produto = Produto(codigo, nome, quantidade, valor, categoria)
        self.estoque[codigo] = produto
        messagebox.showinfo("Info", "Produto incluído com sucesso!")
        self.salvar_estoque()

    def excluir_produto(self):
        codigo = self.entry_codigo.get().strip()
        if codigo in self.estoque:
            del self.estoque[codigo]
            messagebox.showinfo("Info", "Produto excluído com sucesso!")
            self.salvar_estoque()
        else:
            messagebox.showinfo("Info", "Produto não encontrado.")

    def alterar_produto(self):
        codigo = self.entry_codigo.get().strip()
        if codigo in self.estoque:
            nome = self.entry_nome.get().strip()
            try:
                quantidade = int(self.entry_quantidade.get())
                valor = float(self.entry_valor.get())
            except ValueError:
                messagebox.showinfo("Info", "Quantidade ou Valor inválido!")
                return
            categoria = self.entry_categoria.get().strip() or "Sem Categoria"
            produto = self.estoque[codigo]
            produto.nome = nome
            produto.quantidade = quantidade
            produto.valor = valor
            produto.categoria = categoria
            messagebox.showinfo("Info", "Produto alterado com sucesso!")
            self.salvar_estoque()
        else:
            messagebox.showinfo("Info", "Produto não encontrado.")

    def consultar_produto(self):
        codigo = self.entry_codigo.get().strip()
        if codigo in self.estoque:
            produto = self.estoque[codigo]
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.insert(0, produto.nome)
            self.entry_quantidade.delete(0, tk.END)
            self.entry_quantidade.insert(0, produto.quantidade)
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.insert(0, produto.valor)
            self.entry_categoria.delete(0, tk.END)
            self.entry_categoria.insert(0, produto.categoria)
        else:
            messagebox.showinfo("Info", "Produto não encontrado.")

    def listar_produtos(self):
        self.listbox.delete(0, tk.END)
        if not self.estoque:
            self.listbox.insert(tk.END, "Não há produtos no estoque.")
        else:
            header = f"| {'CÓDIGO':>10} | {'PRODUTO':<20} | {'CATEGORIA':<15} | {'QUANTIDADE':>10} | {'VALOR':>15} | {'VALOR TOTAL':>18} |"
            self.listbox.insert(tk.END, header)
            self.listbox.insert(tk.END, "=" * len(header))
            total_quantidade = 0
            total_valor_geral = 0.0

            for produto in self.estoque.values():
                valor_total = produto.quantidade * produto.valor
                valor_formatado = locale.format_string('%.2f', produto.valor, grouping=True).replace('.', ',')
                valor_total_formatado = locale.format_string('%.2f', valor_total, grouping=True).replace('.', ',')
                quantidade_formatada = locale.format_string('%d', produto.quantidade, grouping=True)

                self.listbox.insert(tk.END,
                    f"| {produto.codigo:>10} | {produto.nome:<20} | {produto.categoria:<15} | {quantidade_formatada:>10} | {valor_formatado:>15} | {valor_total_formatado:>18} |")
                total_quantidade += produto.quantidade
                total_valor_geral += valor_total

            self.listbox.insert(tk.END, "=" * len(header))
            total_valor_geral_formatado = locale.format_string('%.2f', total_valor_geral, grouping=True).replace('.', ',')
            self.listbox.insert(tk.END, f"{'TOTAL':<49} {total_quantidade:>10} {'':<19} {total_valor_geral_formatado:>18}")

    def imprimir_lista_produtos(self):
        if not self.estoque:
            messagebox.showinfo("Info", "Não há produtos no estoque.")
            return

        # Monta os dados para a tabela do PDF
        dados = []
        cabecalho = ["CÓDIGO", "PRODUTO", "CATEGORIA", "UNIDADES", "VALOR(R$)", "VALOR TOTAL(R$)"]
        dados.append(cabecalho)

        total_quantidade = 0
        total_valor_geral = 0.0
        for produto in self.estoque.values():
            valor_total = produto.quantidade * produto.valor
            linha = [
                produto.codigo,
                produto.nome,
                produto.categoria,
                locale.format_string('%d', produto.quantidade, grouping=True),  # Formata UNIDADES
                locale.format_string('%.2f', produto.valor, grouping=True).replace('.', ','),  # Formata VALOR(R$)
                locale.format_string('%.2f', valor_total, grouping=True).replace('.', ',')  # Formata VALOR TOTAL(R$)
            ]
            dados.append(linha)
            total_quantidade += produto.quantidade
            total_valor_geral += valor_total

        linha_total = [
            "TOTAL",
            "",
            "",
            locale.format_string('%d', total_quantidade, grouping=True),  # Formata TOTAL UNIDADES
            "",
            f"R$ {locale.format_string('%.2f', total_valor_geral, grouping=True).replace('.', ',')}"  # Formata TOTAL VALOR(R$)
        ]
        dados.append(linha_total)

        pdf_nome = "lista_produtos.pdf"
        doc = SimpleDocTemplate(
            pdf_nome,
            pagesize=A4,
            rightMargin=20,
            leftMargin=20,
            topMargin=30,
            bottomMargin=20
        )

        tabela = Table(dados)
        estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),       # Coluna CÓDIGO alinhada à direita
            ('ALIGN', (1, 0), (2, -1), 'LEFT'),        # Colunas PRODUTO e CATEGORIA alinhadas à esquerda
            ('ALIGN', (3, 0), (5, -1), 'RIGHT'),       # Colunas UNIDADES, VALOR(R$), VALOR TOTAL(R$) alinhadas à direita
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
        tabela.setStyle(estilo)

        elementos = [tabela]
        doc.build(elementos)

        try:
            os.startfile(pdf_nome, "print")
            print("Lista de produtos enviada para impressão.")
        except Exception as e:
            messagebox.showinfo("Erro", f"Não foi possível enviar para impressão: {e}")
        
    def mostrar_total(self):
        total_quantidade = sum(produto.quantidade for produto in self.estoque.values())
        total_valor = sum(produto.quantidade * produto.valor for produto in self.estoque.values())
        mensagem = f"Total de produtos em quantidade: {total_quantidade}\nTotal de produtos em valor: R${total_valor:.2f}"
        messagebox.showinfo("Total", mensagem)

    def backup(self):
        with open("estoque_backup.json", "w") as file:
            json.dump({codigo: produto.__dict__ for codigo, produto in self.estoque.items()}, file)
        messagebox.showinfo("Info", "Backup realizado com sucesso!")

    def restaurar(self):
        try:
            with open("estoque_backup.json", "r") as file:
                estoque_backup = json.load(file)
                self.estoque = {}
                for codigo, dados in estoque_backup.items():
                    if not dados.get("categoria", "").strip():
                        dados["categoria"] = "Sem Categoria"
                    self.estoque[codigo] = Produto(**dados)
            messagebox.showinfo("Info", "Restauração realizada com sucesso!")
            self.salvar_estoque()
        except FileNotFoundError:
            messagebox.showinfo("Info", "Arquivo de backup não encontrado.")

    def sair(self):
        if messagebox.askokcancel("Sair", "Tem certeza de que deseja sair?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = ControleEstoque(root)
    root.mainloop()

if __name__ == "__main__":
    main()
