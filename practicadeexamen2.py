
#1) Crear un menú con las siguientes opciones: (5 pts). 
    #- Insertar lineas de texto en el archivo hasta que el usuario presione "S" o "s". (15 pts)
#3) leer e imprimir en pantalla todos los registros de un archivo línea por línea. (5 pts) 
#4) Contar e imprimir en pantalla el número de líneas que tiene el archivo (10 pts).
#5) Contar e imprimir en pantalla el total de palabras que contiene el archivo (10 pts). 
#6) Buscar e imprimir la o las líneas de texto que contenga una palabra ingresada por el usuario. (15 pts) 
#7) Imprimir en pantalla las líneas del archivo de texto numeradas. (20 pts).
#6) Imprimir en pantalla las líneas del archivo de texto pares (20 pts).


def main():
    archivo = open("archivo.txt", "w")

    opcion = ""

    while opcion != "7":
        print("1. Insertar líneas de texto en el archivo")
        print("2. Leer y mostrar todos los registros del archivo")
        print("3. Contar y mostrar el número de líneas del archivo")
        print("4. Contar y mostrar el total de palabras del archivo")
        print("5. Buscar líneas que contengan una palabra")
        print("6. Mostrar líneas numeradas del archivo")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = ""
            while texto.lower() != "s":
                texto = input("Escriba una línea de texto (presione 'S' para salir): ")
                if texto.lower() != "s":
                    archivo.write(texto + "\n")

        elif opcion == "2":
            archivo = open("archivo.txt", "r")
            for linea in archivo:
                print(linea.strip())
            archivo.close()

        elif opcion == "3":
            archivo = open("archivo.txt", "r")
            num_lineas = len(archivo.readlines())
            print(f"numero de líneas = ", num_lineas)
            archivo.close()

        elif opcion == "4":
            archivo = open("archivo.txt","r")
            num_palabras = 0
            for linea in archivo:
                num_palabras += len(linea.split())
            print(f"numero de palabras del archivo = ." , num_palabras)
            archivo.close()

        elif opcion == "5":
            archivo = open("archivo.txt", "r")
            palabra = input("Ingrese una palabra para buscar : ")
            for linea in archivo:
                if palabra in linea:
                    print(linea.strip())
            archivo.close()

        elif opcion == "6":
            archivo.close()
        
        
        
        else:
            print("opción inválida")

if __name__ == "__main__":
    main() 