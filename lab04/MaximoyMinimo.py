try: 
    #defino programas
    def mostrarminimo(m): 
        print('\nE1 numero minimo es: ',m)

    def mostrarmaximo(M):
        print('\nE1 numero maximo es: ',M)

    def perdirdato():
        minimo=None
        maximo=None
        while True:
            n=input('Ingrese un numero: ')
            if n=='fin':
                break
            if maximo is None or n>maximo:
                maximo=n
            if minimo is None or n<minimo:
                minimo=n
        mostrarmaximo(maximo)
        mostrarminimo(minimo)
#comienza Programa 
    perdirdato()
#Fin del programa
except:
    print('\nError!! Ingrese un numero o la palabra "fin".\nE1 programa ha finalizado')