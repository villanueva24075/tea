try:
    entrada = input("Ingrese nombre del archivo: ")
    archivo =  open(entrada)
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, no existe el archivo")