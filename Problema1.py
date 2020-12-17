
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

# Loop permitindo que o usuário entre uma chave que se deseja saber se existe ou não
entry_loop = True
while(entry_loop):
	try:
		# Ler a entrada
		chave_desejada = input('> ')

		# Conferir se existe um elemento com a chave entrada
		# e se o valor dela já não foi adicionado à lista resultado
		if(chave_desejada in dados):
			print('Existe um elemento no dicionário com essa chave')
			if(dados[chave_desejada] not in resultado):
				print('O valor da chave ({}) foi inserido na lista\n'.format(dados[chave_desejada]))
				resultado.append(dados[chave_desejada])
			else:
				print('Mas o valor da chave ({}) é repetido e não será inserido na lista\n'.format(dados[chave_desejada]))
		else:
			print('Não existe elemento no dicionário com essa chave\n')

	# Encerro a loop com CTRL+D
	except EOFError:
		entry_loop = False

	# Lida com qualquer erro de memória ou CTRL+C
	except:
		exit()

# Escrever a resposta em um novo arquivo csv
arquivo_csv = 'Resposta1.csv'
arquivo = open(arquivo_csv, 'w')
for i in resultado:
	arquivo.write(i + '\n')

# Printar resultado no terminal
print("Resultado:\n" + str(resultado))
