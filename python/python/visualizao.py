# visualizacao de dados em Python


import matplotlib.pyplot as plt
'''

x = [1,2, 5]
y = [2,3, 7]

plt.title(" Grafico curso")
#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x,y) # grafico de linha
plt.show()
'''


'''
x = [1,2, 3, 4, 5]
y = [2,3, 7, 1, 8]

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"


plt.title(titulo)
#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y) # grafico de barras
plt.show()
'''
'''
x1 = [1, 3, 5, 7, 9]
y1=  [2, 3, 7, 1, 8]

x2 = [2, 4, 6, 8, 10]
y2 = [2, 3, 7, 1, 8]

titulo = "Grafico de Barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"


plt.title(titulo)
#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2") # grafico de barras
plt.legend()
plt.show()


'''
'''
x = [1, 3, 5, 7, 9]
y=  [2, 3, 7, 1, 8]



titulo = "Grafico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"


plt.title(titulo)
#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x, y, label = "Meus pontos", color="g", marker='^', s=200 )# color para mudar a cor dos pontos) # Grafico de dispersão
plt.legend()
plt.plot(x, y, color="k", linestyle=":")
plt.legend()
plt.show()
'''
# codigofonte do curso

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
 
# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
 
plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()
plt.show()
plt.savefig("figura1.png", dpi=300)

