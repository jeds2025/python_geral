import os

def criar_arquivo_padrao(nome_arquivo):
    conteudo = """P001;Caneta Azul;10;1.50
P002;Caderno 10 Mat;5;15.00
P001;Caneta Azul;5;1.50
P003;Lapis Grafite;20;0.80
P002;Caderno 10 Mat;2;15.00
P001;Caneta Vermelha;8;1.60
"""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def ler_dados_vendas(nome_arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado. Criando arquivo padrão com dados de conteudo.")
        criar_arquivo_padrao(nome_arquivo)

    dados_vendas = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            codigo, nome, quantidade, preco = linha.strip().split(';')
            dados_vendas.append({
                'codigo': codigo,
                'nome': nome,
                'quantidade': int(quantidade),
                'preco': float(preco)
            })
    return dados_vendas

def processar_vendas(dados_vendas):
    dados_consolidados = {}
    
    for venda in dados_vendas:
        codigo = venda['codigo']
        if codigo not in dados_consolidados:
            dados_consolidados[codigo] = {
                'nome': venda['nome'],
                'quantidade_total': 0,
                'valor_total': 0.0
            }
        
        dados_consolidados[codigo]['quantidade_total'] += venda['quantidade']
        dados_consolidados[codigo]['valor_total'] += venda['quantidade'] * venda['preco']
    
    return dados_consolidados

def gerar_relatorio_produto(dados_consolidados, codigo_produto):
    if codigo_produto in dados_consolidados:
        produto = dados_consolidados[codigo_produto]
        print(f"--- Relatorio Produto: {codigo_produto} ---")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade Total Vendida: {produto['quantidade_total']}")
        print(f"Valor Total Vendido: R$ {produto['valor_total']:.2f}")
    else:
        print(f"Produto {codigo_produto} não encontrado.")

def gerar_relatorio_geral(dados_consolidados):
    print("--- Relatorio Geral de Vendas ---")
    for codigo, produto in sorted(dados_consolidados.items()):
        print(f"Produto: {codigo} - Nome: {produto['nome']} - Qtd: {produto['quantidade_total']} - Total: R$ {produto['valor_total']:.2f}")

def main():
    # Define o caminho do arquivo em C:\PYTHON
    nome_arquivo = r'C:\PYTHON\vendas.txt'
    dados_vendas = ler_dados_vendas(nome_arquivo)
    dados_consolidados = processar_vendas(dados_vendas)
    
    print("Dados de vendas processados.")
    
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
