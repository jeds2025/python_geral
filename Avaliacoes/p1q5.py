# Programa para calculo do valor de uma esfera
# Solicita ao usuario que forneça o valor do raio
raio = float(input("Informe o valor do raio da esfera: "))
volume = 0
v_pi = 3.1416
volume = (4/3)*v_pi*(raio**3)
print(f"O volume da esfera com raio {raio} é {volume:.2f}")