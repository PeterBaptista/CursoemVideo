# Aula 9 - MANIPULANDO TEXTO
#
# frase = 'C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n'
#          0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 18 19 20
# print(frase[9])
# V
# print(frase[9:13])
# Víde
# print(frase[9:14)
# Vídeo
# print(frase[9:21])
# Vídeo Python
# print(frase[9:21:2])
# VdoPto
# print(frase[:5])
# Curso
# print(frase[15:])
# Python
# print(frase[9::3])
# VePh


frase = 'Curso em Vídeo Python'
dividido = frase.split()

print(dividido[3][1])