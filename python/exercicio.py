# -*- coding: utf-8 -*-

'''
idade = int(input("qual a sua idade?"))
#print("Qual a sua idade?", idade)
if idade >= 18:
	print ("Você é maior de idade")
else:
	print("Você é menor de idade")



nota = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota+nota2)/2

print ("sua media é %f" %(media))  # pq dessa sintaxe %f % antes da variavel

if nota >= 6:
	print("Aprovado")
else:
	print("Reprovado")



#equação de segundo grau

from math import sqrt # função para raiz quadrada

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)


x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %f" %(x1))
print("x2 = %f" %(x2))


# lista

lista = [3,2,1,50,8,6,5,3,2]

lista = sorted(lista) # função do python para ordenar
print (lista)'''
'''
for i in range(len(lista)):
	menor = i
	for j in range(i+1,len(lista)):
		if lista[j] < lista[menor]:
			menor = j

	if lista[i] != lista[menor]:
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux

print (lista)
'''

# 

num1= int(input("digite o primeiro numero: "))
operador = string(input("digite o operador: "))
num2=int(input("digite o segundo numero: "))

#operação

if operador == "+"
	resultado = num1 + num2

elif operador == "-"
	resultado = num1 - num2

elif operador == "*"
	resultado = num1 * num2

elif operador == "/"
	resultado = num1 / num2

print ("%f" %(resultado))

