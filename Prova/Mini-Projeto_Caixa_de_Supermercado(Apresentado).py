"""
=============================================================
Mini-Projeto: Caixa de Supermercado
Autor.....: Prof. Carlos Augusto de S. Almeida
Data......: 26/07/2025
Contato...: carlos.almeida@academico.ifs.edu.br
Licença...: GNU General Public License (GPL)
Requisitos: Python 3.12+

Descrição: Simulação de um sistema de caixa de supermercado em Python. Permite 
    adicionar/remover produtos, consultar estoque, ver carrinho, calcular total
    e emitir recibo formatado para o cliente.
Versão...: 1.0
=============================================================
"""

import unicodedata

#region MÓDULOS DAS QUESTÕES ANTERIORES
# =====================================================================================
# FUNÇÕES AUXILIARES E DE PROCESSAMENTO DEFINIDAS NAS QUESTÕES 1 A 5
# =====================================================================================

def remover_acentos(texto: str) -> str:
    """
    Remove acentos de uma string, convertendo caracteres acentuados para suas versões não
    acentuadas.
    """
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

#-------------------------------------------------------------------------------

def print_carrinho(carrinho_lst: list[str]) -> None:
    """
    Exibe o conteúdo de um carrinho de compras de forma formatada, conforme o exemplo.
    """
    print("--- Itens no Carrinho ---")
    if not carrinho_lst:
        print("O carrinho está vazio.")
    else:
        # Agrupa itens para uma exibição mais clara
        itens_contados = {}
        for item in carrinho_lst:
            itens_contados[item] = itens_contados.get(item, 0) + 1
        for item, qtd in itens_contados.items():
            # Formata o nome do produto para ter 4 caracteres, completando com pontos
            etiqueta_produto = item.ljust(4, '.')
            print(f"- {etiqueta_produto}: {qtd} unid.")
    print("-------------------------")

#-------------------------------------------------------------------------------

def print_estoque(estoque_dct: dict[str, int]) -> None:
    """
    Exibe o conteúdo do estoque de produtos de forma formatada.
    """
    print("--- Estoque Disponível ---")
    if not estoque_dct:
        print("O estoque está vazio.")
    else:
        for produto, quantidade in estoque_dct.items():
            print(f"- {produto}: {quantidade} unid.")
    print("--------------------------")

#-------------------------------------------------------------------------------

def carrinho_adicionar_item(carrinho_lst: list[str], estoque_dct: dict[str, int], nome_produto: str) -> None:
    """
    Adiciona um item ao carrinho de compras e decrementa a sua quantidade no estoque.
    """
    if nome_produto in estoque_dct:
        if estoque_dct[nome_produto] > 0:
            carrinho_lst.append(nome_produto)
            estoque_dct[nome_produto] -= 1
            print(f"'{nome_produto}' adicionado ao carrinho.")
        else:
            print(f"> Erro: Produto '{nome_produto}' fora de estoque.")
    else:
        print(f"> Erro: Produto '{nome_produto}' não encontrado no sistema.")

#-------------------------------------------------------------------------------

def carrinho_remover_item(carrinho_lst: list[str], estoque_dct: dict[str, int], nome_produto: str) -> None:
    """
    Remove um item do carrinho de compras e incrementa a sua quantidade no estoque.
    """
    if nome_produto in carrinho_lst:
        carrinho_lst.remove(nome_produto)
        # Devolve o item ao estoque
        if nome_produto in estoque_dct:
            estoque_dct[nome_produto] += 1
        print(f"'{nome_produto}' removido do carrinho.")
    else:
        print(f"> Erro: Produto '{nome_produto}' não encontrado no carrinho.")

#-------------------------------------------------------------------------------

def print_recibo_final(precos_dct: dict, carrinho_lst: list) -> None:
    """
    Gera e imprime um recibo de compras formatado conforme o exemplo fornecido.
    """
    if not carrinho_lst:
        return

    itens_compra = {}
    for item in carrinho_lst:
        itens_compra[item] = itens_compra.get(item, 0) + 1

    print("--- RECIBO ---")
    print("Itens da compra:")
    total_a_pagar = 0.0
    for produto, quantidade in itens_compra.items():
        preco_unitario = precos_dct.get(produto, 0.0)
        subtotal = quantidade * preco_unitario
        total_a_pagar += subtotal
        # Formata o nome do produto para ter 5 caracteres, completando com pontos
        etiqueta_produto = produto.ljust(5, '.')
        print(f"- {etiqueta_produto}: {quantidade} unid. R$ {preco_unitario:.2f}/unid. >> R$ {subtotal:.2f}")
    
    print("----------------------")
    print(f"TOTAL A PAGAR: R$ {total_a_pagar:.2f}")
    print("----------------------")

#-------------------------------------------------------------------------------

def finalizar_compras(carrinho_lst: list[str], precos_dct: dict[str, float]) -> None:
    if not carrinho_lst:
        print("O carrinho está vazio.")
    else:
        print_recibo_final(precos_dct, carrinho_lst)
        carrinho_lst.clear()  # Limpa o carrinho para o próximo cliente
        print("\nObrigado pela sua compra! Volte sempre.")
        print("Caixa pronto para o próximo cliente.")

#-------------------------------------------------------------------------------

def print_ajuda():
    """Imprime a lista de comandos disponíveis para o operador."""
    print("--- Comandos Disponíveis ---")
    print("  adicionar <produto>  - Adiciona um item ao carrinho.")
    print("  remover <produto>    - Remove um item do carrinho.")
    print("  ver-carrinho         - Exibe o conteúdo do carrinho.")
    print("  estoque              - Exibe a situação do estoque.")
    print("  finalizar            - Fecha a compra e gera o recibo.")
    print("  ajuda                - Mostra esta lista de comandos.")
    print("  sair                 - Encerra o programa.")
    print("----------------------------")

#endregion

#region MÓDULO PRINCIPAL DA APLICAÇÃO (Questão 6)
# =====================================================================================
# FUNÇÃO PRINCIPAL QUE ORQUESTRA A APLICAÇÃO
# =====================================================================================

def caixa_de_supermercado(estoque_dct: dict[str, int], precos_dct: dict[str, float]) -> None:
    """
    Executa o loop principal da aplicação de caixa de supermercado, processando os comandos
    do operador.
    """
    carrinho_lst = []
    print("--- Bem-vindo ao Supermercado SuperBarato ---")

    while True:
        entrada_completa = input("\n$ Comando: ").strip().lower()

        if not entrada_completa:
            continue

        partes = entrada_completa.split()
        comando = partes[0]
        arg_str = " ".join(partes[1:])

        match comando:

        case "adicionar":
            if arg_str:
                print("> Erro: Forneça o nome do produto. Ex: adicionar maca")
            else:
                nome_produto_normalizado = remover_acentos(arg_str)
                carrinho_adicionar_item(carrinho_lst, estoque_dct, arg_str)

        case "remover":
            if not arg_str:
                print("> Erro: Forneça o nome do produto. Ex: remover maca")
            else:
                nome_produto_normalizado = remover_acentos(arg_str)
                carrinho_remover_item(carrinho_lst, estoque_dct, nome_produto_normalizado)

        case "ver-carrinho":
            print_carrinho(carrinho_lst)

        case "estoque":
            print_estoque(estoque_dct)

        case "finalizar":
            finalizar_compras(carrinho_lst, precos_dct)

        case "ajuda":
            print_ajuda()

        case "sair":
            print("> Encerrando o sistema. Até logo!")
            break

        case _:
            print(f"> Comando '{comando}' inválido. Digite 'ajuda' para ver as opções.")

#endregion

#region DADOS E EXECUÇÃO PRINCIPAL
# =====================================================================================
# PONTO DE ENTRADA DA APLICAÇÃO
# =====================================================================================

if __name__ == "__main__":
    # Dados de estoque e preços para simular a aplicação
    # As chaves devem estar normalizadas (minúsculas, sem acentos)
    estoque_dct = {
        'maca': 25, 'pao': 30, 'leite': 20, 'cafe': 15, 'banana': 40,
        'arroz': 10, 'feijao': 10
    }

    # Preços ajustados para corresponder ao cálculo do exemplo de iteração
    precos_dct = {
        'maca': 1.00, 'pao': 0.50, 'leite': 4.50, 'cafe': 8.00, 'banana': 3.00,
        'arroz': 22.00, 'feijao': 9.50
    }

    # Inicia a aplicação principal do caixa
    caixa_de_supermercado(estoque_dct, precos_dct)
#endregion
