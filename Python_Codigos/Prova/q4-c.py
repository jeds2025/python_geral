def ler_dados_vendas(nome_arquivo):
    """Lê o arquivo de vendas e retorna uma lista de dicionários com os dados."""
    vendas = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            codigo, nome, quantidade, preco = linha.strip().split(";")
            vendas.append({
                "codigo": codigo,
                "nome": nome,
                "quantidade": int(quantidade),
                "preco": float(preco)
            })
    return vendas

def processar_vendas(dados_vendas):
    """Processa os dados de vendas e retorna um dicionário consolidado."""
    consolidado = {}
    for venda in dados_vendas:
        codigo = venda["codigo"]
        if codigo not in consolidado:
            consolidado[codigo] = {
                "nome": venda["nome"],
                "quantidade_total": 0,
                "valor_total": 0.0
            }
        consolidado[codigo]["quantidade_total"] += venda["quantidade"]
        consolidado[codigo]["valor_total"] += venda["quantidade"] * venda["preco"]
    return consolidado

def gerar_relatorio_produto(dados_consolidados, codigo_produto):
    """Gera um relatório para um produto específico."""
    if codigo_produto in dados_consolidados:
        produto = dados_consolidados[codigo_produto]
        print(f"--- Relatório Produto: {codigo_produto} ---")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade Total Vendida: {produto['quantidade_total']}")
        print(f"Valor Total Vendido: R$ {produto['valor_total']:.2f}")
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def gerar_relatorio_geral(dados_consolidados):
    """Gera um relatório geral de vendas, ordenado pelo código do produto."""
    print("--- Relatório Geral de Vendas ---")
    for codigo, produto in sorted(dados_consolidados.items()):
        print(f"Produto: {codigo} - Nome: {produto['nome']} - Qtd: {produto['quantidade_total']} - Total: R$ {produto['valor_total']:.2f}")

# Programa principal
def main():
    nome_arquivo = "vendas.txt"
    dados_vendas = ler_dados_vendas(nome_arquivo)
    dados_consolidados = processar_vendas(dados_vendas)
    
    print("Dados de vendas processados.")

    while True:
        codigo_produto = input("\nDigite o código do produto para relatório (ou 'TODOS', ou 'SAIR'): ").strip().upper()
        if codigo_produto == "SAIR":
            print("Encerrando programa.")
            break
        elif codigo_produto == "TODOS":
            gerar_relatorio_geral(dados_consolidados)
        else:
            gerar_relatorio_produto(dados_consolidados, codigo_produto)

# Executar o programa principal
if __name__ == "__main__":
    main()