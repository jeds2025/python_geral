import os

def criar_arquivo_padrao(nome_arquivo):
    """Cria um arquivo padrão com dados de exemplo."""
    conteudo = """2025001;Ana Silva;8.5;9.0;7.5
2025002;Bruno Costa;5.0;6.5;7.0
2025003;Carla Dias;4.0;5.5;3.0
2025001;Ana Silva;9.5;9.0;8.0
2025004;Daniel Farias;10.0;9.5;9.0
2025002;Bruno Costa;6.0;7.0;7.0
"""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def ler_dados_alunos(nome_arquivo):
    """Lê o arquivo e retorna um dicionário com as informações dos alunos."""
    dados_alunos = {}

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado. Criando arquivo padrão com dados de exemplo.")
        criar_arquivo_padrao(nome_arquivo)

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            matricula, nome_aluno, nota1, nota2, nota3 = linha.strip().split(';')
            if matricula not in dados_alunos:
                dados_alunos[matricula] = {
                    'nome': nome_aluno,
                    'notas': [float(nota1), float(nota2), float(nota3)]
                }
    return dados_alunos

def processar_situacao_alunos(dados_alunos):
    """Processa os dados dos alunos e retorna um dicionário com média e situação."""
    dados_consolidados = {}
    for matricula, info in dados_alunos.items():
        media = sum(info['notas']) / len(info['notas'])
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        dados_consolidados[matricula] = {
            'nome': info['nome'],
            'notas': info['notas'],
            'media': media,
            'situacao': situacao
        }
    return dados_consolidados

def gerar_relatorio_aluno(dados_consolidados, matricula):
    """Imprime um relatório detalhado para um aluno específico."""
    aluno = dados_consolidados.get(matricula)
    if aluno:
        print(f"--- Relatorio do Aluno: {matricula} ---")
        print(f"Nome: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")
    else:
        print(f"Matricula {matricula} nao encontrada.")

def gerar_relatorio_geral(dados_consolidados, filtro):
    """Imprime um relatório de todos os alunos que correspondem a um filtro."""
    filtro = filtro.upper()
    print(f"--- Relatorio Geral: {filtro} ---")
    valid_situacoes = {"APROVADOS": "Aprovado", "REPROVADOS": "Reprovado", "TODOS": "TODOS"}
    if filtro not in valid_situacoes:
        print("Filtro inválido.")
        return

    situacao_filtrar = valid_situacoes[filtro]
    alunos_filtrados = [
        (mat, aluno) for mat, aluno in dados_consolidados.items()
        if situacao_filtrar == "TODOS" or aluno['situacao'] == situacao_filtrar
    ]

    if not alunos_filtrados:
        print(f"Nenhum aluno encontrado para o filtro '{filtro}'.")
        return

    for matricula, aluno in sorted(alunos_filtrados):
        print(f"Mat: {matricula} | Nome: {aluno['nome']} | Média: {aluno['media']:.2f} | Situação: {aluno['situacao']}")

def main():
    nome_arquivo = r'C:\Python\notas.txt'  # Caminho fixo para o arquivo notas.txt
    dados_alunos = ler_dados_alunos(nome_arquivo)
    dados_consolidados = processar_situacao_alunos(dados_alunos)

    print("Dados dos alunos processados.")

    while True:
        entrada = input("Digite a matricula ou um filtro ('APROVADOS', 'REPROVADOS', 'TODOS', 'SAIR'): ").strip().upper()

        if entrada == 'SAIR':
            print("Encerrando programa.")
            break
        elif entrada in ['APROVADOS', 'REPROVADOS', 'TODOS']:
            gerar_relatorio_geral(dados_consolidados, entrada)
        else:
            gerar_relatorio_aluno(dados_consolidados, entrada)

if __name__ == "__main__":
    main()
