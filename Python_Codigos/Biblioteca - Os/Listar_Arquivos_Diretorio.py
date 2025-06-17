import os

class ListarArquivos:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def listar(self):
        arquivos = os.listdir(self.diretorio)
        for arquivo in arquivos:
            print(arquivo)

diretorio_atual = os.getcwd()
listador = ListarArquivos(diretorio_atual)
listador.listar()
