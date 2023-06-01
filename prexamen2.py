
#1) Crear un menú con las siguientes opciones: (5 pts). 
    #- Insertar lineas de texto en el archivo hasta que el usuario presione "S" o "s". (15 pts)
#3) leer e imprimir en pantalla todos los registros de un archivo línea por línea. (5 pts) 
#4) Contar e imprimir en pantalla el número de líneas que tiene el archivo (10 pts).
#5) Contar e imprimir en pantalla el total de palabras que contiene el archivo (10 pts). 
#6) Buscar e imprimir la o las líneas de texto que contenga una palabra ingresada por el usuario. (15 pts) 
#7) Imprimir en pantalla las líneas del archivo de texto numeradas. (20 pts).
#6) Imprimir en pantalla las líneas del archivo de texto pares (20 pts).


def main():


    bandera = True
    while(bandera==True):
        print("1) leer e imprimir en pantalla todos los registros de un archivo línea por línea: ")
        print("2) Contar e imprimir en pantalla el número de líneas que tiene el archivo : ")
        print("3) Contar e imprimir en pantalla el total de palabras que contiene el archivo: ")
        print("4) Buscar e imprimir la o las líneas de texto que contenga una palabra ingresada por el usuario: ")
        print("5) Imprimir en pantalla las líneas del archivo de texto numeradas.")
        print("6) Imprimir en pantalla las líneas del archivo de texto pares ")
        print("Presione s o S para salir" )
        opcion = input()

        if opcion == "1":
            print("leer e imprimir en pantalla todos los registros de un archivo línea por línea")
            print("Leer todo el archivo")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                print(archivo.read())

        elif opcion == "2":
            print("Contar e imprimir en pantalla el número de líneas que tiene el archivo")

        

            nombre_archivo = input()
            with open(nombre_archivo+".txt","w") as archivo:
                print("Ingresa la línea de texto a escribir")
                linea = input()
                archivo.write(linea+"\n")
                print("Línea de texto guardada exitosamente")

        elif opcion == "3":
            print("Contar e imprimir en pantalla el total de palabras que contiene el archivo")
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
            print("Buscar e imprimir la o las líneas de texto que contenga una palabra ingresada por el usuario")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                print("¿Cuántos bytes (caracteres) deseas leer ")
                n_bytes = int(input())
                print(archivo.read(n_bytes))
        
        elif opcion == "5":
            print("Imprimir en pantalla las líneas del archivo de texto numeradas")
            print("¿En qué archivo deseas leer? Ingresa el nombre sin extensión")
            nombre_archivo = input()
            with open(nombre_archivo+".txt","r") as archivo:
                print(archivo.read())

        elif opcion == "6":
            print("Imprimir en pantalla las líneas del archivo de texto pares")
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

    nombre_archivo = input("Introduce el nombre del archivo: ")

    
    archivo = topen(nombre_archivo, "w")

    while True:
        registro = input("Introduce un registro: ")
        archivo.write(registro + "\n")
        respuesta = input("¿Deseas introducir otro registro? (S/N): ")
        if respuesta == "S" or respuesta == "s":
            continue
        else:
            break
    archivo.close()

    archivo = open(nombre_archivo, "r")
    registros = archivo.readlines()
    for registro in registros:
        print(registro.strip())
    archivo.close()

if __name__ == "__main__":
    main() 