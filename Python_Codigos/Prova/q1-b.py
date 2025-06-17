def comprimir_sequencia(texto):
    # Função recursiva que comprime a sequência
    def compress_helper(texto, index):
        # Caso base: se chegamos ao final da string
        if index >= len(texto):
            return ""
        
        # Contar o número de repetições do caractere atual
        count = 1
        while index + 1 < len(texto) and texto[index] == texto[index + 1]:
            count += 1
            index += 1
        
        # Construir a parte comprimida
        parte = (str(count) if count > 1 else "") + texto[index]
        
        # Chamada recursiva para o próximo caractere
        return parte + compress_helper(texto, index + 1)

    # Inicia a compressão a partir do primeiro caractere
    return compress_helper(texto, 0)

# Exemplos de uso
if __name__ == "__main__":
    texto_original = "AAABBCDDDAA"
    texto_comprimido = comprimir_sequencia(texto_original)
    print(f"Original: {texto_original}")
    print(f"Comprimido: {texto_comprimido}")

    texto_original = "XYZ"
    texto_comprimido = comprimir_sequencia(texto_original)
    print(f"Original: {texto_original}")
    print(f"Comprimido: {texto_comprimido}")

    texto_original = "AAAAA"
    texto_comprimido = comprimir_sequencia(texto_original)
    print(f"Original: {texto_original}")
    print(f"Comprimido: {texto_comprimido}")

    texto_original = ""
    texto_comprimido = comprimir_sequencia(texto_original)
    print(f"Original: {texto_original}")
    print(f"Comprimido: {texto_comprimido}")
