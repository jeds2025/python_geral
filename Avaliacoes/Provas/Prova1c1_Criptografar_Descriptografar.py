def criptografar(texto, chave_palavra):
    texto_cifrado = []
    chave_tamanho = len(chave_palavra)
    
    for i, char in enumerate(texto):
        if char.isalpha():  # Verifica se o caractere é uma letra
            # Determina o deslocamento baseado na chave
            deslocamento = ord(chave_palavra[i % chave_tamanho]) % 26
            
            if char.isupper():  # Se a letra é maiúscula
                novo_char = chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
            else:  # Se a letra é minúscula
                novo_char = chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            
            texto_cifrado.append(novo_char)
        else:
            texto_cifrado.append(char)  # Mantém caracteres não alfabéticos inalterados
    
    return ''.join(texto_cifrado)

def descriptografar(texto_cifrado, chave_palavra):
    texto_decifrado = []
    chave_tamanho = len(chave_palavra)
    
    for i, char in enumerate(texto_cifrado):
        if char.isalpha():  # Verifica se o caractere é uma letra
            # Determina o deslocamento baseado na chave
            deslocamento = ord(chave_palavra[i % chave_tamanho]) % 26
            
            if char.isupper():  # Se a letra é maiúscula
                novo_char = chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
            else:  # Se a letra é minúscula
                novo_char = chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
            
            texto_decifrado.append(novo_char)
        else:
            texto_decifrado.append(char)  # Mantém caracteres não alfabéticos inalterados
    
    return ''.join(texto_decifrado)

# Exemplos de uso
texto = "Ola Mundo 123!"
chave = "ABC"
texto_cifrado = criptografar(texto, chave)
print(f"Texto Cifrado: {texto_cifrado}")
texto_decifrado = descriptografar(texto_cifrado, chave)
print(f"Texto Decifrado: {texto_decifrado}")

texto2 = "Atacar Base Sul as 0500"
chave2 = "SEGREDO"
texto_cifrado2 = criptografar(texto2, chave2)
print(f"Texto Cifrado 2: {texto_cifrado2}")
texto_decifrado2 = descriptografar(texto_cifrado2, chave2)
print(f"Texto Decifrado 2: {texto_decifrado2}")
