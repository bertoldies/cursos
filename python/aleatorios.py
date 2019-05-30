import random # precisa importar o metodo

#random.seed(5) # serve para mostrar sempre o mesmo numero, usar antes da chamada abaixo
numero = random.randint(0, 10) # escolhe um numero aleatorio entre 0 e 10
print(numero)


lista = [5,6,8]
numero = random.choice(lista) # escolha aleatori os numeros da lista
print(numero)