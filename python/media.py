# media, mediana, moda
'''
from statistics import * # para importar todos os metodos de statistics



'''


def media(lista):
	#mean(lista) # metodo facil pelo python
	media = sum(lista)/float(len(lista))

	return media



def mediana(lista): # vai ordenar e pegar os numeros centrais e tirar a média, se for impar só mostra o numero
	#median(lista) # metodo facil pelo python
	lista_ordenada = sorted(lista) # para ordenar a lista
	t = len(lista_ordenada) # saber o tamanho da lista

	if t % 2 == 0:
		mediana = lista_ordenada[int(t/2)]+lista_ordenada[int((t/2)+1)]/2
	elif t % 2 == 1:
		mediana = lista_ordenada[int((t/2))]

	return mediana
	return t

def moda(lista): # vai ver qual o numero que mais e repete
	#mode(lista) # metodo facil pelo python
	lista_dic = {}

	for l in lista:
		if l not in lista_dic:
			lista_dic[l] = 1
		else:
			lista_dic[l] += 1

	maior_repticao = max(lista_dic.values())

	for i in lista_dic:
		if lista_dic[i] == maior_repticao:
			moda = i

	return moda

''' Exemplo pelo python
def mediana(lista):
	return median(lista):
'''