# Estrutura de diretórios simulada
estrutura_diretorios = {
    "/home": {"tipo": "dir", "conteudo": ["user"]},
    "/home/user": {"tipo": "dir", "conteudo": ["documentos", "foto.jpg", "notas.txt"]},
    "/home/user/documentos": {"tipo": "dir", "conteudo": ["trabalho.docx", "relatorio.txt"]},
    "/home/user/foto.jpg": {"tipo": "arq"},
    "/home/user/notas.txt": {"tipo": "arq"},
    "/home/user/documentos/trabalho.docx": {"tipo": "arq"},
    "/home/user/documentos/relatorio.txt": {"tipo": "arq"}
}

# Funções auxiliares
def eh_diretorio(caminho: str) -> bool:
    return estrutura_diretorios.get(caminho, {}).get("tipo") == "dir"

def eh_arquivo(caminho: str) -> bool:
    return estrutura_diretorios.get(caminho, {}).get("tipo") == "arq"

def listar_conteudo(caminho_dir: str):
    return estrutura_diretorios.get(caminho_dir, {}).get("conteudo", [])

# Função recursiva para listar arquivos com a extensão desejada
def listar_arquivos_recursivo(caminho: str, extensao: str):
    arquivos_encontrados = []
    
    # Verifica se o caminho é um diretório
    if eh_diretorio(caminho):
        # Lista o conteúdo do diretório
        conteudo = listar_conteudo(caminho)
        
        for item in conteudo:
            # Cria o caminho completo do item
            caminho_completo = f"{caminho}/{item}" if caminho != "/" else item
            
            # Verifica se o item é um arquivo
            if eh_arquivo(caminho_completo):
                # Se for um arquivo e a extensão corresponder, adiciona à lista
                if caminho_completo.endswith(extensao):
                    arquivos_encontrados.append(caminho_completo)
            # Se for um diretório, chama a função recursivamente
            elif eh_diretorio(caminho_completo):
                arquivos_encontrados.extend(listar_arquivos_recursivo(caminho_completo, extensao))
    
    return arquivos_encontrados

# Exemplo de uso
arquivos_txt = listar_arquivos_recursivo("/home", ".txt")
print(f"Arquivos .txt encontrados: {arquivos_txt}")

arquivos_jpg = listar_arquivos_recursivo("/home", ".jpg")
print(f"Arquivos .jpg encontrados: {arquivos_jpg}")

arquivos_pdf = listar_arquivos_recursivo("/home", ".pdf")
print(f"Arquivos .pdf encontrados: {arquivos_pdf}")
