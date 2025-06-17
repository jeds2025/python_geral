def ler_dados_vendas(nome_arquivo):
    """Lê o arquivo de vendas e retorna uma lista de dicionários com os dados."""
    vendas = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            codigo, nome, quantidade, preco = linha.strip().split(';')
            vendas.append({
                'codigo': codigo,
                'nome': nome,
                'quantidade': int(quantidade),
                'preco': float(preco)
            })
    return vendas

def processar_vendas(dados_vendas):
    """Processa os dados de vendas e retorna um dicionário consolidado com totais por produto."""
    produtos = {}
    
    for venda in dados_vendas:
        codigo = venda['codigo']
        if codigo not in produtos:
            produtos[codigo] = {
                'nome': venda['nome'],
                'quantidade_total': 0,
                'valor_total': 0.0
            }
        
        produtos[codigo]['quantidade_total'] += venda['quantidade']
        produtos[codigo]['valor_total'] += venda['quantidade'] * venda['preco']
    
    return produtos

def gerar_relatorio_produto(dados_consolidados, codigo_produto):
    """Imprime um relatório para um produto específico."""
    if codigo_produto in dados_consolidados:
        produto = dados_consolidados[codigo_produto]
        print(f"--- Relatorio Produto: {codigo_produto} ---")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade Total Vendida: {produto['quantidade_total']}")
        print(f"Valor Total Vendido: R$ {produto['valor_total']:.2f}")
    else:
        print(f"Produto {codigo_produto} nao encontrado.")

def gerar_relatorio_geral(dados_consolidados):
    """Imprime um relatório com todos os produtos, suas quantidades totais e valores totais vendidos."""
    print("--- Relatorio Geral de Vendas ---")
    for codigo, produto in sorted(dados_consolidados.items()):
        print(f"Produto: {codigo} - Nome: {produto['nome']} - Qtd: {produto['quantidade_total']} - Total: R$ {produto['valor_total']:.2f}")

def main():
    """Função principal que orquestra a execução do programa."""
    nome_arquivo = 'vendas.txt'  # Caminho do arquivo
    dados_vendas = ler_dados_vendas(nome_arquivo)
    dados_consolidados = processar_vendas(dados_vendas)
    
    print("Dados de vendas processados.\n")
    
    while True:
        codigo_produto = input("Digite o codigo do produto para relatorio (ou 'TODOS', ou 'SAIR'): ").strip()
        
        if codigo_produto == 'SAIR':
            print("Encerrando programa.")
            break
        elif codigo_produto == 'TODOS':
            gerar_relatorio_geral(dados_consolidados)
        else:
            gerar_relatorio_produto(dados_consolidados, codigo_produto)

if __name__ == "__main__":
    main()

