import unicodedata
from typing import List, Dict

def remover_acentos(texto: str) -> str:
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def print_carrinho(carrinho: List[str]) -> None:
    print("--- Itens no Carrinho ---")
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        itens = {}
        for item in carrinho:
            itens[item] = itens.get(item, 0) + 1
        for item, qtd in itens.items():
            print(f"- {item.ljust(4, '.')}: {qtd} unid.")
    print("-------------------------")

def print_estoque(estoque: Dict[str, int]) -> None:
    print("--- Estoque Disponível ---")
    if not estoque:
        print("O estoque está vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"- {produto}: {quantidade} unid.")
    print("--------------------------")

def carrinho_adicionar_item(carrinho: List[str], estoque: Dict[str, int], nome_produto: str) -> None:
    if nome_produto in estoque:
        if estoque[nome_produto] > 0:
            carrinho.append(nome_produto)
            estoque[nome_produto] -= 1
            print(f"'{nome_produto}' adicionado ao carrinho.")
        else:
            print(f"> Erro: Produto '{nome_produto}' fora de estoque.")
    else:
        print(f"> Erro: Produto '{nome_produto}' não encontrado no sistema.")

def carrinho_remover_item(carrinho: List[str], estoque: Dict[str, int], nome_produto: str) -> None:
    if nome_produto in carrinho:
        carrinho.remove(nome_produto)
        if nome_produto in estoque:
            estoque[nome_produto] += 1
        print(f"'{nome_produto}' removido do carrinho.")
    else:
        print(f"> Erro: Produto '{nome_produto}' não encontrado no carrinho.")

def print_recibo_final(precos: Dict[str, float], carrinho: List[str]) -> None:
    if not carrinho:
        return
    itens = {}
    for item in carrinho:
        itens[item] = itens.get(item, 0) + 1
    print("--- RECIBO ---")
    print("Itens da compra:")
    total = 0.0
    for produto, qtd in itens.items():
        preco = precos.get(produto, 0.0)
        subtotal = qtd * preco
        total += subtotal
        print(f"- {produto.ljust(5, '.')}: {qtd} unid. R$ {preco:.2f}/unid. >> R$ {subtotal:.2f}")
    print("----------------------")
    print(f"TOTAL A PAGAR: R$ {total:.2f}")
    print("----------------------")

def finalizar_compras(carrinho: List[str], precos: Dict[str, float]) -> None:
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print_recibo_final(precos, carrinho)
        carrinho.clear()
        print("\nObrigado pela sua compra! Volte sempre.")
        print("Caixa pronto para o próximo cliente.")

def print_ajuda() -> None:
    print("--- Comandos Disponíveis ---")
    print("  adicionar <produto>")
    print("  remover <produto>")
    print("  ver-carrinho")
    print("  estoque")
    print("  finalizar")
    print("  ajuda")
    print("  sair")
    print("----------------------------")

def caixa_de_supermercado(estoque: Dict[str, int], precos: Dict[str, float]) -> None:
    carrinho = []
    print("--- Bem-vindo ao Supermercado ---")
    while True:
        entrada = input("\n$ Comando: ").strip().lower()
        if not entrada:
            continue
        partes = entrada.split()
        comando = partes[0]
        arg = " ".join(partes[1:])
        nome_produto = remover_acentos(arg)
        match comando:
            case "adicionar":
                if not arg:
                    print("> Erro: Forneça o nome do produto.")
                else:
                    carrinho_adicionar_item(carrinho, estoque, nome_produto)
            case "remover":
                if not arg:
                    print("> Erro: Forneça o nome do produto.")
                else:
                    carrinho_remover_item(carrinho, estoque, nome_produto)
            case "ver-carrinho":
                print_carrinho(carrinho)
            case "estoque":
                print_estoque(estoque)
            case "finalizar":
                finalizar_compras(carrinho, precos)
            case "ajuda":
                print_ajuda()
            case "sair":
                print("> Encerrando o sistema. Até logo!")
                break
            case _:
                print(f"> Comando '{comando}' inválido. Digite 'ajuda' para ver as opções.")

if __name__ == "__main__":
    estoque = {
        'maca': 25, 'pao': 30, 'leite': 20, 'cafe': 15, 'banana': 40,
        'arroz': 10, 'feijao': 10
    }
    precos = {
        'maca': 1.00, 'pao': 0.50, 'leite': 4.50, 'cafe': 8.00, 'banana': 3.00,
        'arroz': 22.00, 'feijao': 9.50
    }
    caixa_de_supermercado(estoque, precos)
