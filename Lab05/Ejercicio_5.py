cadena = 'X-DSPAM-Confidence:0.8475' 
inicio = cadena.find(":") + 1
final = len(cadena)
print(inicio, final)
print(cadena[inicio:final])