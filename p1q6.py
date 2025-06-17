# Programa para calcular o tempo gasto com troca de parabrisas
hora_entrada = int(input("Informe a hora da entrada do veiculo: "))
minutos_entrada = int(input("Informe os minutos da entrada do veiculo: "))
qte_parabrisas = int(input("Informe a quantidade de parabrisas a ser trocado: "))
minutos_hora_entrada = hora_entrada * 60
total_minutos_entrada = minutos_hora_entrada + minutos_entrada

# tempo em minutos
tempo = 70 
# calculo do tempo gasto para troca do(s) parabrisa(s)
tempo_gasto = qte_parabrisas * tempo

total_minutos_saida = total_minutos_entrada + tempo_gasto
saida_horas = total_minutos_saida // 60
saida_minutos = total_minutos_saida % 60

print(f"O veiculo entrou às {hora_entrada} horas e {minutos_entrada} minutos e será liberado às {saida_horas} horas e {saida_minutos} minutos para a troca de {qte_parabrisas} parabrisas")