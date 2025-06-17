senha_correta = "python123"

senha_digitada = ""

while senha_digitada != senha_correta: # Loop que continua até a senha correta ser digitada
    senha_digitada = input("Digite a senha: ")
    
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Acesso concedido!")
