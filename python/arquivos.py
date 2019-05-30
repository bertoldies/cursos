'''
arquivo = open("Arquivo.txt")

linhas = arquivo.readlines() # essa funcao ja converte em uma lista
print(linhas)

for linha in linhas:
	print(linha)

texto_completo = arquivo.read()
print(texto_completo)
'''

w =  open("arquivo2.txt","a")

w.write("Esse e o meu arquivo2\n") # escrever no arquivo
w.close() # para fechar o arquivo
'''
w =  open("arquivo.txt","w") # w vai sobreescrever

w.write("Esse e o meu arquivo") # escrever no arquivo
w.close() # para fechar o arquivo

w =  open("arquivo.txt","a") # vai adicionar a frase no arquivo

w.write("\nEsse e o meu arquivo2 \n") # escrever no arquivo
w.close() # para fechar o arquivo
'''