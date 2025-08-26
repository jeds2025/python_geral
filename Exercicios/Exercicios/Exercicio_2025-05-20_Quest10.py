def simular_caixa_eletronico():
    saldo = 2000.00
    print("Bem-vindo ao Caixa Eletrônico!")
    print(f"Saldo inicial: R$ {saldo:.2f}\n")

    while True:
        print("""
        Menu do Caixa Eletrônico:
        Digite a opção desejada:
        1: Consultar Saldo
        2: Realizar Saque
        3: Realizar Depósito
        4: Sair
        """)
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if opcao == 1:
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 0:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print("Saque realizado com sucesso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor de saque inválido.")
        
        elif opcao == 3:
            valor_deposito = float(input("Digite o valor do depósito: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                print("Depósito realizado com sucesso.")
            else:
                print("Valor de depósito inválido.")
        
        elif opcao == 4:
            print("Obrigado por usar nosso caixa eletrônico.")
            break
        
        else:
            print("Opção inválida.")

# Chamar a função
simular_caixa_eletronico()
