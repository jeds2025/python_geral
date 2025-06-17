def celsius_para_fahrenheit(temp_c):
    """Converte Celsius para Fahrenheit."""
    return (temp_c * 9/5) + 32

def fahrenheit_para_celsius(temp_f):
    """Converte Fahrenheit para Celsius."""
    return (temp_f - 32) * 5/9

def gerenciar_conversoes_temperatura():
    """Gerencia o menu de conversão de temperaturas."""
    while True:
        print("""
              \nMenu de Conversão de Temperatura:
              \n[1]: Celsius para Fahrenheit
              \n[2]: Fahrenheit para Celsius
              \n[3]: Sair
            """)
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if opcao == 1:
            temp_c = float(input("Digite a temperatura em Celsius: "))
            temp_f = celsius_para_fahrenheit(temp_c)
            print(f"{temp_c}°C é igual a {temp_f}°F")
        
        elif opcao == 2:
            temp_f = float(input("Digite a temperatura em Fahrenheit: "))
            temp_c = fahrenheit_para_celsius(temp_f)
            print(f"{temp_f}°F é igual a {temp_c}°C")
        
        elif opcao == 3:
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida.")

# Chama a função principal
gerenciar_conversoes_temperatura()
