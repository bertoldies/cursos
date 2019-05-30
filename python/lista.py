lista = ["abacaxi", "melao","abacate"]
lista2 = [1,2,3,5,7,8]
lista3 = []


print(lista[2])
for item in lista:
	print(item)

#adicionando elementos na lista

lista.append("limao")
print(lista)

if 7 in lista2:
	print("esta na lista")

# remover itens da lista

del lista2 [3:]
print(lista2)

del lista2 [:] # apagar tudo
print(lista2)
print(len(lista2))

lista3.append(57)
print(lista3)