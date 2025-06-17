def modificar_lista(lista_param, valor_param):
    print(f"  ID de lista_param DENTRO (inicio): {id(lista_param)}")
    lista_param.append(40)
    print(f"  ID de lista_param DENTRO (apos append): {id(lista_param)}")
    lista_param = [100, 200] # Reatribuição local
    print(f"  ID de lista_param DENTRO (apos reatribuicao): {id(lista_param)}")
    valor_param += 5
    print(f"  ID de valor_param DENTRO: {id(valor_param)}")
    return valor_param

a = 10
b = a
print(f"ID de a (inicial): {id(a)}")
print(f"ID de b (inicial): {id(b)}")

b = 20
print(f"ID de a (apos b=20): {id(a)}")
print(f"ID de b (apos b=20): {id(b)}")

minha_lista = [10, 20, 30]
outra_lista = minha_lista
print(f"ID de minha_lista (inicial): {id(minha_lista)}")
print(f"ID de outra_lista (inicial): {id(outra_lista)}")

outra_lista.append(35) # Modifica o objeto referenciado por ambos
print(f"ID de minha_lista (apos append em outra_lista): {id(minha_lista)}")
print(f"minha_lista (apos append em outra_lista): {minha_lista}")

c = 5
print(f"ID de c (antes da funcao): {id(c)}")
print(f"ID de minha_lista (antes da funcao): {id(minha_lista)}")

d = modificar_lista(minha_lista, c)

print(f"ID de c (depois da funcao): {id(c)}")
print(f"ID de d (depois da funcao): {id(d)}")
print(f"ID de minha_lista (depois da funcao): {id(minha_lista)}")

print(f"Valor final de a: {a}")
print(f"Valor final de b: {b}")
print(f"Valor final de c: {c}")
print(f"Valor final de d: {d}")
print(f"Valor final de minha_lista: {minha_lista}")
print(f"Valor final de outra_lista: {outra_lista}")
