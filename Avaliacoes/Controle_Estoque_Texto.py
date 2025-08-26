import json
import os


class Produto:
    def __init__(self, codigo, nome, quantidade, valor, categoria=None):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.categoria = categoria

    def __repr__(self):
        return f"{self.codigo}: {self.nome} - {self.quantidade} unidades - R${self.valor:.2f} - Categoria: {self.categoria}"


class ControleEstoque:
    def __init__(self):
        self.estoque = {}
        self.carregar_estoque()

    def carregar_estoque(self):
        try:
            with open("estoque.json", "r") as file:
                estoque_carregado = json.load(file)
                self.estoque = {codigo: Produto(
                    **dados) for codigo, dados in estoque_carregado.items()}
            print("Estoque carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. Um novo será criado.")

    def salvar_estoque(self):
        with open("estoque.json", "w") as file:
            json.dump({codigo: produto.__dict__ for codigo,
                      produto in self.estoque.items()}, file)
        print("Estoque salvo com sucesso!")

    def incluir_produto(self):
        codigo = input("Digite o código do produto: ")
        if codigo in self.estoque:
            print("Este código já existe.")
            opcao = input(
                "Deseja acrescentar itens ao produto existente? (s/n): ")
            if opcao.lower() == 's':
                quantidade = int(
                    input("Digite a quantidade de itens a acrescentar: "))
                self.estoque[codigo].quantidade += quantidade
                print("Quantidade atualizada com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            valor = float(input("Digite o valor do produto: "))
            categoria = input("Digite a categoria do produto (opcional): ")
            produto = Produto(codigo, nome, quantidade, valor, categoria)
            self.estoque[codigo] = produto
            print("Produto incluído com sucesso!")
        self.salvar_estoque()

    def excluir_produto(self):
        codigo = input("Digite o código do produto que deseja excluir: ")
        if codigo in self.estoque:
            del self.estoque[codigo]
            print("Produto excluído com sucesso!")
            self.salvar_estoque()
        else:
            print("Produto não encontrado.")

    def alterar_produto(self):
        codigo = input("Digite o código do produto que deseja alterar: ")
        if codigo in self.estoque:
            nome = input("Digite o novo nome do produto: ")
            quantidade = int(input("Digite a nova quantidade do produto: "))
            valor = float(input("Digite o novo valor do produto: "))
            categoria = input("Digite a nova categoria do produto (opcional): ")
            produto = self.estoque[codigo]
            produto.nome = nome
            produto.quantidade = quantidade
            produto.valor = valor
            produto.categoria = categoria
            print("Produto alterado com sucesso!")
            self.salvar_estoque()
        else:
            print("Produto não encontrado.")

    def consultar_produto(self):
        codigo = input("Digite o código do produto que deseja consultar: ")
        if codigo in self.estoque:
            print(self.estoque[codigo])
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        if not self.estoque:
            print("Não há produtos no estoque.")
        else:
            print(
                f"{'CÓDIGO':>10} {'PRODUTO':<20} {'UNIDADES':>10} {'VALOR':>12} {'CATEGORIA':<15} {'VALOR TOTAL':>14}")
            print("="*85)
            total_quantidade = 0
            total_valor_geral = 0.0
            for produto in self.estoque.values():
                valor_total = produto.quantidade * produto.valor
                print(
                    f"{produto.codigo:>10} {produto.nome:<20} {produto.quantidade:>10} R${produto.valor:>10.2f} {produto.categoria:<15} R${valor_total:>12.2f}")
                total_quantidade += produto.quantidade
                total_valor_geral += valor_total
            print("="*85)
            print(
                f"{'TOTAL':<31} {total_quantidade:>10} {'':<15} {'':<12} R${total_valor_geral:>12.2f}")

    def imprimir_lista_produtos(self):
        if not self.estoque:
            print("Não há produtos no estoque.")
        else:
            with open("lista_produtos.txt", "w") as file:
                file.write(
                    f"{'CÓDIGO':>10} {'PRODUTO':<20} {'UNIDADES':>10} {'VALOR':>12} {'CATEGORIA':<15} {'VALOR TOTAL':>14}\n")
                file.write("="*85 + "\n")
                total_quantidade = 0
                total_valor_geral = 0.0
                for produto in self.estoque.values():
                    valor_total = produto.quantidade * produto.valor
                    file.write(
                        f"{produto.codigo:>10} {produto.nome:<20} {produto.quantidade:>10} R${produto.valor:>10.2f} {produto.categoria:<15} R${valor_total:>12.2f}\n")
                    total_quantidade += produto.quantidade
                    total_valor_geral += valor_total
                file.write("="*85 + "\n")
                file.write(
                    f"{'TOTAL':<31} {total_quantidade:>10} {'':<15} {'':<12} R${total_valor_geral:>12.2f}\n")

            os.system("notepad /p lista_produtos.txt")
            print("Lista de produtos enviada para impressão.")

    def mostrar_total(self):
        total_quantidade = sum(
            produto.quantidade for produto in self.estoque.values()
        )
        total_valor = sum(
            produto.quantidade * produto.valor for produto in self.estoque.values()
        )
        print(f"Total de produtos em quantidade: {total_quantidade}")
        print(f"Total de produtos em valor: R${total_valor:.2f}")

    def backup(self):
        with open("estoque_backup.json", "w") as file:
            json.dump(
                {codigo: produto.__dict__ for codigo, produto in self.estoque.items()},
                file,
            )
        print("Backup realizado com sucesso!")

    def restaurar(self):
        try:
            with open("estoque_backup.json", "r") as file:
                estoque_backup = json.load(file)
                self.estoque = {
                    codigo: Produto(**dados) for codigo, dados in estoque_backup.items()
                }
            print("Restauração realizada com sucesso!")
            self.salvar_estoque()
        except FileNotFoundError:
            print("Arquivo de backup não encontrado.")

    def menu(self):
        while True:
            print("\nMENU CONTROLE DE ESTOQUE")
            print("1. INCLUIR PRODUTO")
            print("2. EXCLUIR PRODUTO")
            print("3. ALTERAR PRODUTO")
            print("4. CONSULTAR PRODUTO")
            print("5. LISTAR PRODUTOS")
            print("6. IMPRIMIR LISTA DE PRODUTOS")
            print("7. MOSTRAR TOTAL DE PRODUTOS")
            print("8. BACKUP DO ESTOQUE")
            print("9. RESTAURAR ESTOQUE")
            print("10. SAIR")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.incluir_produto()
            elif opcao == "2":
                self.excluir_produto()
            elif opcao == "3":
                self.alterar_produto()
            elif opcao == "4":
                self.consultar_produto()
            elif opcao == "5":
                self.listar_produtos()
            elif opcao == "6":
                self.imprimir_lista_produtos()
            elif opcao == "7":
                self.mostrar_total()
            elif opcao == "8":
                self.backup()
            elif opcao == "9":
                self.restaurar()
            elif opcao == "10":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    controle_estoque = ControleEstoque()
    controle_estoque.menu()
