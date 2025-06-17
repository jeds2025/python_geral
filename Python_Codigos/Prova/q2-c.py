def criptografar(texto, chave_palavra):
    resultado = ""
    tamanho_chave = len(chave_palavra)
    
    for i, caractere in enumerate(texto):
        deslocamento = ord(chave_palavra[i % tamanho_chave]) % 26

        if 'A' <= caractere <= 'Z':  # Letras maiúsculas
            novo_caractere = chr(((ord(caractere) - ord('A') + deslocamento) % 26) + ord('A'))
        elif 'a' <= caractere <= 'z':  # Letras minúsculas
            novo_caractere = chr(((ord(caractere) - ord('a') + deslocamento) % 26) + ord('a'))
        else:
            novo_caractere = caractere  # Mantém caracteres inalterados
        
        resultado += novo_caractere
    
    return resultado

def descriptografar(texto_cifrado, chave_palavra):
    resultado = ""
    tamanho_chave = len(chave_palavra)
    
    for i, caractere in enumerate(texto_cifrado):
        deslocamento = ord(chave_palavra[i % tamanho_chave]) % 26

        if 'A' <= caractere <= 'Z':  # Letras maiúsculas
            novo_caractere = chr(((ord(caractere) - ord('A') - deslocamento) % 26) + ord('A'))
        elif 'a' <= caractere <= 'z':  # Letras minúsculas
            novo_caractere = chr(((ord(caractere) - ord('a') - deslocamento) % 26) + ord('a'))
        else:
            novo_caractere = caractere  # Mantém caracteres inalterados
        
        resultado += novo_caractere
    
    return resultado

# Testando a função com os exemplos dados
testes = [
    ("Ola Mundo 123!", "ABC"),
    ("Atacar Base Sul as 0500", "SEGREDO")
]

for texto_original, chave in testes:
    texto_cifrado = criptografar(texto_original, chave)
    texto_decifrado = descriptografar(texto_cifrado, chave)
    
    print(f"Texto Original: {texto_original}")
    print(f"Texto Cifrado: {texto_cifrado}")
    print(f"Texto Decifrado: {texto_decifrado}")