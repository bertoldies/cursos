import random

def geraListaInteiro(tam): # tam é o tamanho da lista ( indefinido)
	lista = [] # lista vazia
	for i in range(tam): # passo o range no for de acordo com o tamanho definido na funcao
		lista.append(random.randint(0, tam)) # com o appente vou adicionar valores na lista de modo aleatorio com o random

	return lista 


