import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import shutil

# Configuração inicial do banco de dados
def configurar_banco():
    conn = sqlite3.connect('PCA.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ORGAO (
            codigo TEXT PRIMARY KEY,
            nome TEXT,
            ativo TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UG (
            codigo TEXT PRIMARY KEY,
            nome TEXT,
            ativo TEXT,
            orgao_codigo TEXT,
            FOREIGN KEY (orgao_codigo) REFERENCES ORGAO (codigo)
        )
    """)
    conn.commit()
    conn.close()

# Funções do Banco de Dados
def executar_query(query, parametros=()):
    conn = sqlite3.connect('PCA.db')
    cursor = conn.cursor()
    cursor.execute(query, parametros)
    conn.commit()
    conn.close()

def consultar_query(query, parametros=()):
    conn = sqlite3.connect('PCA.db')
    cursor = conn.cursor()
    cursor.execute(query, parametros)
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def verificar_vinculos_orgao(codigo):
    vinculos = consultar_query("SELECT * FROM UG WHERE orgao_codigo = ?", (codigo,))
    return len(vinculos) > 0

def verificar_vinculos_ug(codigo):
    # Atualmente, não há vínculo para UG; ajuste conforme necessário no futuro
    return False

# Função de backup e restore
def backup_banco():
    try:
        shutil.copy('PCA.db', 'PCA_backup.db')
        messagebox.showinfo("Backup", "Backup realizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao realizar backup: {e}")

def restore_banco():
    try:
        shutil.copy('PCA_backup.db', 'PCA.db')
        messagebox.showinfo("Restore", "Restore realizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao realizar restore: {e}")

# Interface para Cadastro de Órgãos
def orgao_interface():
    janela_orgao = tk.Toplevel()
    janela_orgao.title("Cadastro de Órgãos")

    def listar():
        tree.delete(*tree.get_children())
        for row in consultar_query("SELECT * FROM ORGAO"):
            tree.insert('', 'end', values=row)

    def incluir():
        executar_query(
            "INSERT INTO ORGAO (codigo, nome, ativo) VALUES (?, ?, ?)",
            (codigo_var.get(), nome_var.get(), ativo_var.get())
        )
        listar()

    def alterar():
        executar_query(
            "UPDATE ORGAO SET nome = ?, ativo = ? WHERE codigo = ?",
            (nome_var.get(), ativo_var.get(), codigo_var.get())
        )
        listar()

    def excluir():
        if verificar_vinculos_orgao(codigo_var.get()):
            messagebox.showerror("Erro", "Não é possível excluir este órgão porque ele possui unidades vinculadas.")
        else:
            executar_query("DELETE FROM ORGAO WHERE codigo = ?", (codigo_var.get(),))
            listar()

    codigo_var, nome_var, ativo_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

    tk.Label(janela_orgao, text="Código:").grid(row=0, column=0)
    tk.Entry(janela_orgao, textvariable=codigo_var).grid(row=0, column=1)
    tk.Label(janela_orgao, text="Nome:").grid(row=1, column=0)
    tk.Entry(janela_orgao, textvariable=nome_var).grid(row=1, column=1)
    tk.Label(janela_orgao, text="Ativo (S/N):").grid(row=2, column=0)
    tk.Entry(janela_orgao, textvariable=ativo_var).grid(row=2, column=1)

    tk.Button(janela_orgao, text="Incluir", command=incluir).grid(row=3, column=0)
    tk.Button(janela_orgao, text="Alterar", command=alterar).grid(row=3, column=1)
    tk.Button(janela_orgao, text="Excluir", command=excluir).grid(row=3, column=2)

    tree = ttk.Treeview(janela_orgao, columns=('codigo', 'nome', 'ativo'), show='headings')
    tree.heading('codigo', text='Código')
    tree.heading('nome', text='Nome')
    tree.heading('ativo', text='Ativo')
    tree.grid(row=4, column=0, columnspan=3)

    listar()

# Interface para Cadastro de Unidades Orçamentárias
def ug_interface():
    janela_ug = tk.Toplevel()
    janela_ug.title("Cadastro de Unidades Orçamentárias")

    def listar():
        tree.delete(*tree.get_children())
        for row in consultar_query("SELECT * FROM UG"):
            tree.insert('', 'end', values=row)

    def carregar_orgaos():
        orgaos = consultar_query("SELECT codigo, nome FROM ORGAO")
        orgao_menu['values'] = [f"{codigo} - {nome}" for codigo, nome in orgaos]

    def incluir():
        orgao_codigo = orgao_var.get().split(" - ")[0]
        executar_query(
            "INSERT INTO UG (codigo, nome, ativo, orgao_codigo) VALUES (?, ?, ?, ?)",
            (codigo_var.get(), nome_var.get(), ativo_var.get(), orgao_codigo)
        )
        listar()

    def alterar():
        orgao_codigo = orgao_var.get().split(" - ")[0]
        executar_query(
            "UPDATE UG SET nome = ?, ativo = ?, orgao_codigo = ? WHERE codigo = ?",
            (nome_var.get(), ativo_var.get(), orgao_codigo, codigo_var.get())
        )
        listar()

    def excluir():
        if verificar_vinculos_ug(codigo_var.get()):
            messagebox.showerror("Erro", "Não é possível excluir esta unidade porque ela possui vínculos.")
        else:
            executar_query("DELETE FROM UG WHERE codigo = ?", (codigo_var.get(),))
            listar()

    codigo_var, nome_var, ativo_var, orgao_var = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

    tk.Label(janela_ug, text="Código:").grid(row=0, column=0)
    tk.Entry(janela_ug, textvariable=codigo_var).grid(row=0, column=1)
    tk.Label(janela_ug, text="Nome:").grid(row=1, column=0)
    tk.Entry(janela_ug, textvariable=nome_var).grid(row=1, column=1)
    tk.Label(janela_ug, text="Ativo (S/N):").grid(row=2, column=0)
    tk.Entry(janela_ug, textvariable=ativo_var).grid(row=2, column=1)
    tk.Label(janela_ug, text="Órgão:").grid(row=3, column=0)
    orgao_menu = ttk.Combobox(janela_ug, textvariable=orgao_var)
    orgao_menu.grid(row=3, column=1)

    tk.Button(janela_ug, text="Incluir", command=incluir).grid(row=4, column=0)
    tk.Button(janela_ug, text="Alterar", command=alterar).grid(row=4, column=1)
    tk.Button(janela_ug, text="Excluir", command=excluir).grid(row=4, column=2)

    tree = ttk.Treeview(janela_ug, columns=('codigo', 'nome', 'ativo', 'orgao_codigo'), show='headings')
    tree.heading('codigo', text='Código')
    tree.heading('nome', text='Nome')
    tree.heading('ativo', text='Ativo')
    tree.heading('orgao_codigo', text='Órgão (Código)')
    tree.grid(row=5, column=0, columnspan=3)

    carregar_orgaos()
    listar()

# Submenu para exibir órgãos e unidades vinculadas
def listar_orgaos_com_unidades():
    janela_listagem = tk.Toplevel()
    janela_listagem.title("Lista de Órgãos e Unidades")

    tree = ttk.Treeview(janela_listagem)
    tree['columns'] = ('nome', 'ativo')
    tree.heading('#0', text='Código do Órgão', anchor='w')
    tree.heading('nome', text='Nome', anchor='w')
    tree.heading('ativo', text='Ativo (S/N)', anchor='w')
    tree.column('#0', width=150, anchor='w')
    tree.column('nome', width=300, anchor='w')
    tree.column('ativo', width=100, anchor='center')
    tree.pack(fill=tk.BOTH, expand=True)

    orgaos = consultar_query("SELECT codigo, nome, ativo FROM ORGAO")
    for orgao in orgaos:
        orgao_id = tree.insert('', 'end', text=orgao[0], values=(orgao[1], orgao[2]))
        unidades = consultar_query("SELECT codigo, nome, ativo FROM UG WHERE orgao_codigo = ?", (orgao[0],))
        for unidade in unidades:
            tree.insert(orgao_id, 'end', text=unidade[0], values=(unidade[1], unidade[2]))

# Interface principal
def criar_interface():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro")

    # Botões para cada funcionalidade
    tk.Button(janela, text="Cadastro de Órgãos", command=orgao_interface).pack(pady=5)
    tk.Button(janela, text="Cadastro de Unidades Orçamentárias", command=ug_interface).pack(pady=5)
    tk.Button(janela, text="Lista de Órgãos e Unidades", command=listar_orgaos_com_unidades).pack(pady=5)
    tk.Button(janela, text="Backup", command=backup_banco).pack(pady=5)
    tk.Button(janela, text="Restore", command=restore_banco).pack(pady=5)
    tk.Button(janela, text="Sair", command=janela.destroy).pack(pady=5)

    janela.mainloop()

# Inicialização
if __name__ == "__main__":
    configurar_banco()
    criar_interface()