# Lista inicial de cidades
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

def adicionar_cidade(lista, cidade):
    if cidade not in lista:
        lista.append(cidade)
        print(f"Cidade {cidade} adicionada com sucesso.")
    else:
        print(f"A cidade {cidade} já está na lista.")

def remover_cidade(lista, cidade):
    if cidade in lista:
        lista.remove(cidade)
        print(f"Cidade {cidade} removida com sucesso.")
    else:
        print(f"A cidade {cidade} não está na lista.")

def consultar_cidade(lista, cidade):
    if cidade in lista:
        print(f"A cidade {cidade} está na lista.")
    else:
        print(f"A cidade {cidade} não está na lista.")

def listar_cidades(lista):
    if lista:
        print("Cidades na lista:")
        for cidade in lista:
            print(f"- {cidade}")
    else:
        print("Não há cidades na lista.")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar cidade")
        print("2. Remover cidade")
        print("3. Consultar cidade")
        print("4. Listar cidades")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cidade = input("Digite o nome da cidade a ser adicionada: ")
            adicionar_cidade(cidades, cidade)
        elif opcao == "2":
            cidade = input("Digite o nome da cidade a ser removida: ")
            remover_cidade(cidades, cidade)
        elif opcao == "3":
            cidade = input("Digite o nome da cidade a ser consultada: ")
            consultar_cidade(cidades, cidade)
        elif opcao == "4":
            listar_cidades(cidades)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
