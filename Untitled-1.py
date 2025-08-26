def saudacao(nome: str = "Ninguém") -> str:
    return f"\nOlá, {nome}!"

print(saudacao("Mundo"), saudacao("Alice"), saudacao())
print()

def dados(n1: str, v1: int):
    print(f"Nome: {n1}")
    print(f"Valor: {v1}")

dados("Produto A", 150)

print()

def cadastrar_produto(n1: str, v1: int) -> tuple[str, int]:
    return n1, v1

# Exemplos de uso
print(cadastrar_produto("Teclado Gamer", 199), ("Mouse sem fio", 89))

print()

def dados(info: dict):
    print(f"Nome: {info['n1']}")
    print(f"Valor: {info['v1']}")

dados({"n1": "Produto A", "v1": 150})

print()

def dados(**kwargs):
    print(f"Nome: {kwargs.get('n1')}")
    print(f"Valor: {kwargs.get('v1')}")

dados(n1="Produto A", v1=150)

print()