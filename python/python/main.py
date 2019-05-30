# importar os outros arquivos, precisam estar na mesmo pasta

import modolarizacao as a
import media as m


lista = a.geraListaInteiro(6)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)



print("lista")
print(lista)

print("A media da minha lista e "+str(media))
print("A mediana da minha lista e "+str(mediana))
print("A moda da minha lista e "+str(moda))