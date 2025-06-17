def comprimir_sequencia(texto, index=0):
    # Caso base: Se a string estiver vazia ou se chegamos ao final dela
    if index >= len(texto):
        return ""
    
    # Conta repetições consecutivas do caractere atual
    contador = 1
    while index + contador < len(texto) and texto[index] == texto[index + contador]:
        contador += 1
    
    # Define a parte comprimida (quantidade seguida do caractere, ou apenas o caractere)
    parte_comprimida = f"{contador}{texto[index]}" if contador > 1 else texto[index]
    
    # Chamada recursiva avançando no texto
    return parte_comprimida + comprimir_sequencia(texto, index + contador)

# Testando a função com os exemplos dados
testes = ["AAABBCDDDAA", "XYZ", "AAAAA", ""]
for texto_original in testes:
    texto_comprimido = comprimir_sequencia(texto_original)
    print(f"Original: {texto_original}")
    print(f"Comprimido: {texto_comprimido}")