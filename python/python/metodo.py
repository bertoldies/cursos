# -*- coding: utf-8 -*-

a= "teste"
b= "agora"
concatenar = a +" "+ b
print(concatenar)
print(concatenar.lower()) # mostrar string minusculo
print(concatenar.upper()) # mostrar string maisculo

# aplicar esse metodo a variavel
concatenar = concatenar.upper()
print(concatenar)


# "\n" quebra de linha
# remover espaços ou caracter

print(concatenar.strip())

# converte sequencia em lista

string = " o rato roeu"
lista = string.split() # separa por virgula
print(lista)
lista = string.split("o") #separa por virgula e apaga o letra r
print(lista)


# busca de sub string
string = " o rato roeu"

busca = string.find("roeu")

print(busca) # mostra a posição da string
print(string[:busca]) # posso usar como lista para mostrar oq ue eu quero

busca = string.find("não tem") # se não existir a string é retornado -1
print(busca)


# substitui parte da string por outra
string = " o rato roeu"
string = string.replace("rato","castor")
print(string)

