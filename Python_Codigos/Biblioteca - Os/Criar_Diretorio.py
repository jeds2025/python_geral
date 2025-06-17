import os

class CriarDiretorio:
    def __init__(self, nome):
        self.nome = nome

    def criar(self):
        os.makedirs(self.nome)
        print("Diretório", self.nome, "criado com sucesso.")

novo_diretorio = "meu_novo_diretorio"
criador = CriarDiretorio(novo_diretorio)
criador.criar()
