import re

padrao = r'Python'
texto = 'Python é uma linguagem de programação poderosa.'

if re.search(padrao, texto):
    print(f"Padrão '{padrao}' encontrado na string. '{texto}'")
else:
    print("Padrão não encontrado na string.")
