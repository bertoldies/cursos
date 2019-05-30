

import re

seq1 = "hhhjjjkl"
seq2 = "jijij"

'''
seq1 = input("Digite a sequencia 1:")
seq2 = input("Digite a sequencia 2:")
 
if seq1 == seq2:
	print("Sequencia iguais")

else:
	print("Sequencia diferentes")
'''


busca = re.match(seq1,seq2)

if busca:
	print ("Sequencia iguais")
	print busca.group()
else:
	print ("Sequencia diferentes")

