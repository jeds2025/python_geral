frutas = ['banana', 'maçã', 'uva', 'pera', 'laranja']
numeros = [1, 2, 3, 4, 5]
carros = ['gol', 'palio', 'celta', 'uno']
lista = [frutas, numeros, carros]
print(lista)
print(frutas)
print(numeros)  
print(carros)

print(lista[2][0:2])

frutas.append('kiwi')
print(frutas)

# dicionarios
aluno = {'nome': 'João', 'idade': 20, 'curso': 'Engenharia'}
print(aluno)
print(aluno['nome'])
notas = {'matematica': 8, 'portugues': 7.5, 'ciencias': 9}
print(notas)

print(aluno)

aluno['Foto'] = 'Sim'
print(aluno)