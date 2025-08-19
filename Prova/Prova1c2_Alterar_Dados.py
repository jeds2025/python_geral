def alterar_dados(dict_param: dict, num_param: int) -> int:
    print(f"  ID de dict_param DENTRO (inicio): {id(dict_param)}")
    print(f"  ID de num_param DENTRO (inicio): {id(num_param)}")

    # Modificando o objeto original (mutavel)
    dict_param['c'] = 300
    print(f"  ID de dict_param DENTRO (apos modif.): {id(dict_param)}")

    # Reatribuindo a variavel local (nao afeta o objeto original)
    num_param = num_param + 1
    print(f"  ID de num_param DENTRO (apos reatrib.): {id(num_param)}")

    # Reatribuindo a variavel local a um novo objeto
    dict_param = {'x': 99, 'y': 98}
    print(f"  ID de dict_param DENTRO (apos reatrib.): {id(dict_param)}")

    return num_param


x = 100
y = x
print(f"ID de x (inicial): {id(x)}")
print(f"ID de y (inicial): {id(y)}")

y = 101
print(f"ID de x (apos y=101): {id(x)}")
print(f"ID de y (apos y=101): {id(y)}")

meu_dict = {'a': 1, 'b': 2}
outro_dict = meu_dict
print(f"ID de meu_dict (inicial): {id(meu_dict)}")
print(f"ID de outro_dict (inicial): {id(outro_dict)}")

outro_dict['b'] = 20 # Modifica o objeto referenciado por ambos
print(f"ID de meu_dict (apos modif. em outro_dict): {id(meu_dict)}")
print(f"meu_dict (apos modif. em outro_dict): {meu_dict}")

print(f"\n--- Chamando a funcao ---")
num_original = 50
print(f"ID de meu_dict (antes da funcao): {id(meu_dict)}")
print(f"ID de num_original (antes da funcao): {id(num_original)}")

num_retornado = alterar_dados(meu_dict, num_original)

print(f"\n--- Apos a funcao ---")
print(f"ID de meu_dict (depois da funcao): {id(meu_dict)}")
print(f"ID de num_original (depois da funcao): {id(num_original)}")
print(f"ID de num_retornado (depois da funcao): {id(num_retornado)}")

print(f"\n--- Valores Finais ---")
print(f"Valor final de x: {x}")
print(f"Valor final de y: {y}")
print(f"Valor final de meu_dict: {meu_dict}")
print(f"Valor final de outro_dict: {outro_dict}")
print(f"Valor final de num_original: {num_original}")
print(f"Valor final de num_retornado: {num_retornado}")
