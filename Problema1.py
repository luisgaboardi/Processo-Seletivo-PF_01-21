
# Declaradas as estruturas de dados a serem utilizadas
dados = {}
resultado = []

# Abrir o arquivo com a lista de dicionários
try:
	arquivo_csv = 'entrada1.csv'
	arquivo = open(arquivo_csv, 'r')
except Exception as e:
	print('Arquivo não encontrado.\n' + str(e))
	exit()

# Armazenar a string contida no arquivo
dados_brutos = arquivo.read().splitlines()

# Para cada linha do conteúdo do arquivo, filtrar a chave e o valor
# e colocá-los em um dicionário
for linha in dados_brutos:
	(chave, valor) = linha.split(',')
	dados[chave] = valor

# Dados preliminares obtidos e armazenados no dicionário _dados_