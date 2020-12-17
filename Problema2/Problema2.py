
import csv

# Estrutura de dados a ser utilizada
dados = []

# Abrir o arquivo com a lista de informações
try:
	arquivo_csv = 'entrada2.csv'
	arquivo = open(arquivo_csv, 'r')
except Exception as e:
	print('Arquivo não encontrado.\n' + str(e))
	exit()

# Armazenar a string contida no arquivo
dados_brutos = arquivo.read().splitlines()

# Para cada linha do conteúdo do arquivo, filtrar a chave e o valor
# e colocá-los em um dicionário
for linha in dados_brutos:
	(idd, nome, tel, idade) = linha.split(';')
	elemento = [idd,nome,tel,idade]
	dados.append(elemento)

# Ordendar a lista sendo o nome a chave determinante
dados.sort(key = lambda x: x[1]) 

# Escrever a resposta em um novo arquivo CSV
with open('Resposta2.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	writer.writerows(dados)

# Printar a lista resultante no terminal
print("Resultado:")
for d in dados:
	print(d)