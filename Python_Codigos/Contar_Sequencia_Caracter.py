def comprimir_sequencia(texto, indice=0):
    
    if indice >= len(texto): # verifica se a string está vazia
        return ""
    
    contador=1
    while indice + contador < len(texto) and texto[indice] == texto[indice+contador]:
        contador += 1
    if contador > 1:
        parte_comprimida = f"{contador}{texto[indice]}"
    else:
        parte_comprimida = texto[indice]
    
    return parte_comprimida + comprimir_sequencia(texto, indice + contador)

def main():
    texto = input("Digite a sequência de caracteres: ")
    print(f"Sequência original: {texto}")   
    resultado = comprimir_sequencia(texto)
    print(f"Sequência comprimida: {resultado}")
    
main()