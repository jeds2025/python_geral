import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para carregar os dados do estoque do arquivo JSON
def carregar_estoque():
    try:
        with open("estoque_dados.json", "r") as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        estoque = {}
    return estoque

# Função para salvar os dados do estoque no arquivo JSON
def salvar_estoque(estoque):
    with open("estoque_dados.json", "w") as arquivo:
        json.dump(estoque, arquivo)

# Função para adicionar um novo item ao estoque
def adicionar_item():
    codigo = entrada_codigo.get()
    if codigo in estoque:
        messagebox.showerror("Erro", "O código já existe! Escolha outro código.")
        return
    nome = entrada_nome.get()
    quantidade = int(entrada_quantidade.get())
    preco = float(entrada_preco.get())

    estoque[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco}
    salvar_estoque(estoque)
    atualizar_tabela()
    atualizar_grafico()
    limpar_entradas()

# Função para alterar um item existente
def alterar_item():
    codigo = entrada_codigo.get()
    if codigo in estoque:
        confirmar = messagebox.askyesno("Confirmação", "Tem certeza que deseja alterar este item?")
        if not confirmar:
            return
        nome = entrada_nome.get()
        quantidade = int(entrada_quantidade.get())
        preco = float(entrada_preco.get())

        estoque[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco}
        salvar_estoque(estoque)
        atualizar_tabela()
        atualizar_grafico()
        limpar_entradas()

# Função para excluir um produto selecionado
def excluir_selecionado():
    selecao = tabela.selection()
    if selecao:
        codigo = tabela.item(selecao[0], "values")[0]
        if codigo in estoque:
            del estoque[codigo]
            salvar_estoque(estoque)
            atualizar_tabela()
            atualizar_grafico()

# Função para atualizar a tabela de estoque
def atualizar_tabela():
    tabela.delete(*tabela.get_children())
    estoque_ordenado = dict(sorted(estoque.items(), key=lambda x: int(x[0])))  # Ordena o estoque por código numérico
    global total_produtos, valor_total_estoque
    total_produtos = 0
    valor_total_estoque = 0.0
    
    for codigo, dados in estoque_ordenado.items():
        quantidade_formatada = f"{dados['quantidade']:,}".replace(",", ".")
        preco_formatado = f"{dados['preco']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        total = dados["quantidade"] * dados["preco"]
        total_formatado = f"{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        total_produtos += dados["quantidade"]
        valor_total_estoque += total
        
        tabela.insert("", tk.END, values=(codigo, dados["nome"], quantidade_formatada, preco_formatado, total_formatado))

    atualizar_totais()

# Atualizar os totais na interface
def atualizar_totais():
    texto_total_produtos.set(f"Total de Produtos: {total_produtos:,}".replace(",", "."))
    texto_valor_total.set(f"Valor Total: R$ {valor_total_estoque:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Função para atualizar o gráfico de estoque
def atualizar_grafico():
    for widget in quadro_grafico.winfo_children():
        widget.destroy()

    estoque_ordenado = dict(sorted(estoque.items()))
    nomes = [dados["nome"] for dados in estoque_ordenado.values()]
    quantidades = [dados["quantidade"] for dados in estoque_ordenado.values()]

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(nomes, quantidades)
    ax.set_xlabel("Nome do Produto")
    ax.set_ylabel("Quantidade")
    ax.set_title("Estoque")

    canvas = FigureCanvasTkAgg(fig, master=quadro_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Função para limpar as entradas do formulário
def limpar_entradas():
    entrada_codigo.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

# Função para preencher as entradas ao selecionar um item
def selecionar_item(event):
    selecao = tabela.selection()
    if selecao:
        codigo = tabela.item(selecao[0], "values")[0]
        dados = estoque.get(codigo)
        if dados:
            entrada_codigo.delete(0, tk.END)
            entrada_codigo.insert(0, codigo)
            entrada_nome.delete(0, tk.END)
            entrada_nome.insert(0, dados["nome"])
            entrada_quantidade.delete(0, tk.END)
            entrada_quantidade.insert(0, dados["quantidade"])
            entrada_preco.delete(0, tk.END)
            entrada_preco.insert(0, dados["preco"])

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerenciador de Estoque")

# Quadro principal
quadro_principal = tk.Frame(janela)
quadro_principal.grid(row=0, column=0, padx=100, pady=100)

# Área de entrada
quadro_entrada = tk.Frame(quadro_principal)
quadro_entrada.grid(row=0, column=0, padx=50, pady=50)

# Rótulos e entradas
rotulo_codigo = tk.Label(quadro_entrada, text="Código:")
rotulo_codigo.grid(row=0, column=0, padx=5, pady=5)
entrada_codigo = tk.Entry(quadro_entrada)
entrada_codigo.grid(row=0, column=1, padx=5, pady=5)

rotulo_nome = tk.Label(quadro_entrada, text="Nome do Item:")
rotulo_nome.grid(row=1, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(quadro_entrada)
entrada_nome.grid(row=1, column=1, padx=5, pady=5)

rotulo_quantidade = tk.Label(quadro_entrada, text="Quantidade:")
rotulo_quantidade.grid(row=2, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(quadro_entrada)
entrada_quantidade.grid(row=2, column=1, padx=5, pady=5)

rotulo_preco = tk.Label(quadro_entrada, text="Preço:")
rotulo_preco.grid(row=3, column=0, padx=5, pady=5)
entrada_preco = tk.Entry(quadro_entrada)
entrada_preco.grid(row=3, column=1, padx=5, pady=5)

# Botões
quadro_botoes = tk.Frame(quadro_entrada)
quadro_botoes.grid(row=4, column=0, columnspan=2, pady=10)

botao_adicionar = tk.Button(quadro_botoes, text="Adicionar Item", command=adicionar_item, bg="green", fg="white")
botao_adicionar.grid(row=0, column=0, padx=5)

botao_excluir = tk.Button(quadro_botoes, text="Excluir Selecionado", command=excluir_selecionado, bg="red", fg="white")
botao_excluir.grid(row=0, column=1, padx=5)

botao_alterar = tk.Button(quadro_botoes, text="Alterar Item", command=alterar_item, bg="blue", fg="white")
botao_alterar.grid(row=0, column=2, padx=5)

botao_sair = tk.Button(quadro_botoes, text="Sair", command=janela.quit)
botao_sair.grid(row=0, column=3, padx=5)

# Área da tabela
quadro_tabela = tk.Frame(quadro_entrada)
quadro_tabela.grid(row=5, column=0, columnspan=2, pady=10)

tabela = ttk.Treeview(quadro_tabela, columns=("Código", "Nome", "Quantidade", "Preço", "Total"), show="headings")
tabela.heading("Código", text="Código")
tabela.heading("Nome", text="Nome")
tabela.heading("Quantidade", text="Quantidade")
tabela.heading("Preço", text="Preço")
tabela.heading("Total", text="Total")

tabela.column("Código", anchor="center", width=100)
tabela.column("Nome", anchor="w", width=150)
tabela.column("Quantidade", anchor="e", width=100)
tabela.column("Preço", anchor="e", width=100)
tabela.column("Total", anchor="e", width=120)

tabela.pack()
tabela.bind("<<TreeviewSelect>>", selecionar_item)

# Linha para totais
quadro_totais = tk.Frame(quadro_entrada)
quadro_totais.grid(row=6, column=0, columnspan=2, pady=10)

texto_total_produtos = tk.StringVar()
texto_valor_total = tk.StringVar()

rotulo_total_produtos = tk.Label(quadro_totais, textvariable=texto_total_produtos, anchor="w")
rotulo_total_produtos.grid(row=0, column=0, sticky="w")

rotulo_valor_total = tk.Label(quadro_totais, textvariable=texto_valor_total, anchor="e")
rotulo_valor_total.grid(row=0, column=1, sticky="e")

# Área do gráfico
quadro_grafico = tk.Frame(quadro_principal)
quadro_grafico.grid(row=0, column=1, padx=50, pady=50)

# Carregando o estoque inicial
estoque = carregar_estoque()

# Atualizando a tabela, totais e gráfico
atualizar_tabela()
atualizar_grafico()

# Rodando a interface principal
janela.mainloop()