saldo_conta = 500

def realizar_compra(valor_compra):
    taxa_servico = 10
    # saldo_conta = saldo_conta - valor_compra - taxa_servico # Linha A (comentada)
    novo_saldo_local = saldo_conta - valor_compra - taxa_servico # Linha B
    if novo_saldo_local >= 0:
        print(f"Compra de R${valor_compra} aprovada. Saldo (local) após compra: R${novo_saldo_local}")
        # saldo_conta = novo_saldo_local # Linha C (comentada)
        return True
    else:
        print(f"Compra de R${valor_compra} negada. Saldo insuficiente.")
        return False

print(f"Saldo inicial: R${saldo_conta}")
realizar_compra(100)
print(f"Saldo após primeira tentativa: R${saldo_conta}")
realizar_compra(400)
print(f"Saldo final: R${saldo_conta}")

