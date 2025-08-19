def comprimir_sequencia(texto):
    def compressao_recursiva(indice, caracter_atual, contador):
        # Se chegamos ao final da string, adicionamos o resultado
        if indice == len(texto):
            return (str(contador) + caracter_atual) if contador > 1 else caracter_atual
        
        # Se o caractere atual é igual ao próximo, incrementamos o contador
        if texto[indice] == caracter_atual:
            return compressao_recursiva(indice + 1, caracter_atual, contador + 1)
        else:
            # Se o caractere atual não é igual ao próximo, adicionamos o resultado
            resultado = (str(contador) + caracter_atual) if contador > 1 else caracter_atual
            return resultado + compressao_recursiva(indice + 1, texto[indice], 1)

    if not texto:  # Se a string estiver vazia, retornamos uma string vazia
        return ""
    
    # Iniciamos a recursão com o primeiro caractere e um contador de 1
    return compressao_recursiva(1, texto[0], 1)

# Exemplos de uso
texto_original_1 = "AAABBCDDDAA"
texto_comprimido_1 = comprimir_sequencia(texto_original_1)
print(f"Original: {texto_original_1}")
print(f"Comprimido: {texto_comprimido_1}")

texto_original_2 = "XYZ"
texto_comprimido_2 = comprimir_sequencia(texto_original_2)
print(f"Original: {texto_original_2}")
print(f"Comprimido: {texto_comprimido_2}")

texto_original_3 = "AAAAA"
texto_comprimido_3 = comprimir_sequencia(texto_original_3)
print(f"Original: {texto_original_3}")
print(f"Comprimido: {texto_comprimido_3}")

texto_original_4 = ""
texto_comprimido_4 = comprimir_sequencia(texto_original_4)
print(f"Original: {texto_original_4}")
print(f"Comprimido: {texto_comprimido_4}")
