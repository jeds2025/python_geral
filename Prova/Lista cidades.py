def menu():
    print("\nMenu:")
    print("1. Incluir cidade")
    print("2. Excluir cidade")
    print("3. Consultar cidade")
    print("4. Listar cidades")
    print("5. Backup")
    print("6. Restore")
    print("7. Sair")
    return input("Escolha uma opção: ")

def incluir_cidade(cidades):
    while True:
        cidade = input("Digite o nome da cidade para incluir: ")
        if cidade not in cidades:
            cidades.append(cidade)
            print(f"{cidade} foi incluída na lista.")
        else:
            print(f"{cidade} já está na lista.")
        continuar = input("Deseja incluir outra cidade? (s/n): ").strip().lower()
        if continuar != 's':
            break

def excluir_cidade(cidades):
    while True:
        cidade = input("Digite o nome da cidade para excluir: ")
        if cidade in cidades:
            cidades.remove(cidade)
            print(f"{cidade} foi removida da lista.")
        else:
            print(f"{cidade} não está na lista.")
        continuar = input("Deseja excluir outra cidade? (s/n): ").strip().lower()
        if continuar != 's':
            break

def consultar_cidade(cidades):
    cidade = input("Digite o nome da cidade para consultar: ")
    if cidade in cidades:
        print(f"{cidade} está na lista.")
    else:
        print(f"{cidade} não está na lista.")

def listar_cidades(cidades):
    if cidades:
        print("Lista de cidades:")
        for cidade in cidades:
            print(f"- {cidade}")
    else:
        print("A lista de cidades está vazia.")
        
def backup_cidades(cidades):
    if cidades:
        try:
            with open("backup_cidades.txt", "w") as arquivo:
                for cidade in cidades:
                    arquivo.write(f"{cidade}\n")
            print("Backup realizado com sucesso! As cidades foram salvas no arquivo 'backup_cidades.txt'.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar realizar o backup: {e}")
    else:
        print("A lista de cidades está vazia. Não há nada para fazer backup.")
        
def restore_cidades(cidades):
    try:
        with open("backup_cidades.txt", "r") as arquivo:
            cidades_restauradas = arquivo.readlines()
            cidades.clear()  # Limpa a lista atual antes de restaurar
            cidades.extend([cidade.strip() for cidade in cidades_restauradas])  # Adiciona as cidades restauradas
        print("Restore realizado com sucesso! As cidades foram restauradas da lista de backup.")
    except FileNotFoundError:
        print("Nenhum arquivo de backup encontrado. Certifique-se de que o backup foi realizado antes.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar realizar o restore: {e}")

def main():
    cidades = []
    while True:
        opcao = menu()
        if opcao == "1":
            incluir_cidade(cidades)
        elif opcao == "2":
            excluir_cidade(cidades)
        elif opcao == "3":
            consultar_cidade(cidades)
        elif opcao == "4":
            listar_cidades(cidades)
        elif opcao == "5":
            backup_cidades(cidades)
        elif opcao == "6":
            restore_cidades(cidades)           
        elif opcao == "7":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
