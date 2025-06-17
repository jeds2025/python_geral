def criptografar(texto, chave_palavra):
    texto_cifrado = ""
    chave_len = len(chave_palavra)

    for i in range(len(texto)):
        char = texto[i]
        if char.isalpha():  # Verifica se o caractere é uma letra
            # Calcula o deslocamento baseado na chave
            deslocamento = ord(chave_palavra[i % chave_len].upper()) - ord('A')
            # Aplica o deslocamento
            if char.isupper():
                novo_char = chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
            else:
                novo_char = chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            texto_cifrado += novo_char
        else:
            texto_cifrado += char  # Mantém caracteres não alfabéticos inalterados

    return texto_cifrado

def descriptografar(texto_cifrado, chave_palavra):
    texto_decifrado = ""
    chave_len = len(chave_palavra)

    for i in range(len(texto_cifrado)):
        char = texto_cifrado[i]
        if char.isalpha():  # Verifica se o caractere é uma letra
            # Calcula o deslocamento baseado na chave
            deslocamento = ord(chave_palavra[i % chave_len].upper()) - ord('A')
            # Aplica o deslocamento inverso
            if char.isupper():
                novo_char = chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
            else:
                novo_char = chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
            texto_decifrado += novo_char
        else:
            texto_decifrado += char  # Mantém caracteres não alfabéticos inalterados

    return texto_decifrado

# Exemplos de uso
if __name__ == "__main__":
    texto = "Ola Mundo 123!"
    chave = "ABC"
    texto_cifrado = criptografar(texto, chave)
    print(f"Texto Cifrado: {texto_cifrado}")  # Saída esperada: "Pna Nuoep 123!"
    texto_decifrado = descriptografar(texto_cifrado, chave)
    print(f"Texto Decifrado: {texto_decifrado}")  # Saída esperada: "Ola Mundo 123!"

    texto2 = "Atacar Base Sul as 0500"
    chave2 = "SEGREDO"
    texto_cifrado2 = criptografar(texto2, chave2)
    print(f"Texto Cifrado 2: {texto_cifrado2}")  # Saída esperada: "Sbflfs Ievf Wao ew 0500"
    texto_decifrado2 = descriptografar(texto_cifrado2, chave2)
    print(f"Texto Decifrado 2: {texto_decifrado2}")  # Saída esperada: "Atacar Base Sul as 0500"
