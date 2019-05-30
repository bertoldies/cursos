dicionario = {"A":"ameixa","B":"bola","C":"cachorro"}

print(dicionario["A"])

for chave in dicionario:
	print(chave)
	print(dicionario[chave])

for i in dicionario.items():
	print(i)
	
for i in dicionario.values():
	print(i)

for i in dicionario.keys():
	print(i)