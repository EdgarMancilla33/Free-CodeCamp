
def main():
    #Edgar y Ramon 
    nombre_archivo = input("dame el nombre del archivo: ")

    with open(nombre_archivo, "w") as archivo:
        texto = input("escribe dentro del archivo: ")
        archivo.write(texto)

    with open(nombre_archivo, "r") as archivo:
        texto = archivo.read()
        palabras = texto.split()
        cantidad_palabras = len(palabras)

    print(" Numero de palabras= " , cantidad_palabras )

    
if __name__ == "__main__":
    main()