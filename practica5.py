# 1) Realice un script de python que permita
# ejecutar un menú de opciones. Considere las siguientes opciones.
# ---> a) Crear archivo (solicitando nombre de archivo por teclado).
# ---> b) Escribir en el archivo una línea de texto,
#         solicitando la línea por teclado.
# ---> c) Escribir la cantidad n de líneas deseada por el usuario en
#         el archivo, permitiendo su captura por teclado.
# ---> d) Lectura de n bytes en el archivo.
# ---> e) Lectura de todo el archivo.
# ---> f) Lectura línea por línea del archivo.
# ---> g) Salir del programa con s o S.

def main():
    print("Operaciones con archivos")

    bandera = True
    while(bandera==True):
        print("1) Crear archivo: ")
        print("2) Escribir línea: ")
        print("3) Escribir n líneas: ")
        print("4) Lectura de n bytes: ")
        print("5) Leer todo el archivo ")
        print("6) Leer línea por línea ")
        print("Presione s o S para salir" )
        opcion = input()

        if opcion == "1":
            print("Ingrese el nombre para el archivo sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","a") as archivo:
                print("Creación del archivo....")
                print("Achivo creado con éxito")

        elif opcion == "2":
            print("¿En qué archivo quieres escribir? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","w") as archivo:
                print("Ingresa la línea de texto a escribir")
                linea = input()
                archivo.write(linea+"\n")
                print("Línea de texto guardada exitosamente")

        elif opcion == "3":
            print("Escribiendo n líneas de archivo")
            print("¿En qué archivo quieres escribir? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","w") as archivo:
                print("¿Cuántas líneas deseas escribir en el archivo?")
                n_lineas = int(input())
                lineas = []
                for i in range(n_lineas):
                    print("Escribe el texto deseado: ", i)
                    dato = input()
                    lineas.append(dato+"\n")
                archivo.writelines(lineas)

        elif opcion == "4":
            print("Lectura de n bytes")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                print("¿Cuántos bytes (caracteres) deseas leer ")
                n_bytes = int(input())
                print(archivo.read(n_bytes))
        
        elif opcion == "5":
            print("Leer todo el archivo")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                print(archivo.read())

        elif opcion == "6":
            print("Leer línea por línea")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                lista = archivo.readlines()
                for linea in (lista):
                    print (linea)

        elif opcion == "s" or opcion == "S":
            bandera = False
        else:
            print("Opción invalida")


if __name__ == "__main__":
    main()