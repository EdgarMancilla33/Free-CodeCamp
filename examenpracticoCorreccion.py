def main():
    while True:
        print("1. Crear archivo de contactos")
        print("2. Insertar registro de contacto")
        print("3. Buscar contacto por número de teléfono")
        print("4. Imprimir todos los registros de contacto")
        print("5. Imprimir el total de contactos registrados")
        print("6. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            nombre_archivo = input("Ingrese el nombre del archivo donde desea insertar el registro: ")
            insertar_contacto(nombre_archivo)
        elif opcion == "3":
            nombre_archivo = input("Ingrese el nombre del archivo donde desea buscar el contacto: ")
            buscar_contacto(nombre_archivo)
        elif opcion == "4":
            nombre_archivo = input("Ingrese el nombre del archivo que desea imprimir: ")
            imprimir_contactos(nombre_archivo)
        elif opcion == "5":
            nombre_archivo = input("Ingrese el nombre del archivo que desea imprimir: ")
            imprimir_total_contactos(nombre_archivo)
        elif opcion == "6":
            print("")
            break


def crear_archivo():
    nombre_archivo = input("Ingrese el nombre para el archivo de contactos: ")
    archivo = open(nombre_archivo, "w")
    archivo.close()
    print("Archivo creado exitosamente.")


def insertar_contacto(nombre_archivo):
    while True:
        nombre = input("Ingrese el nombre completo del contacto (o 's' para salir): ")
        if nombre == "s":
            break
        direccion = input("Ingrese la dirección del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        registro = nombre + ", " + direccion + ", " + telefono + "\n"
        with open(nombre_archivo, "a") as archivo:
            archivo.write(registro)
        print("Registrado" + nombre )




#(no imprime la busqueda)

def buscar_contacto(nombre_archivo):
    telefono = input("Ingrese el número de teléfono del contacto que desea buscar: ")
    with open(nombre_archivo, "r") as archivo:
        for registro in archivo:
            
            datos = registro.split(", ")
            if datos[2].strip() == telefono:
                print("Nombre:  " + datos[0])
                print("Dirección:  " + datos[1])
                print("Teléfono:   " + datos[2])
                return
    print("no se encontró ningún contacto con el número de teléfono " + telefono)



def imprimir_contactos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        for registro in archivo:
            datos = registro.split(", ")
            print("Nombre: " + datos[0])
            print("Dirección: " + datos[1])
            print("Teléfono: " + datos[2])


def imprimir_total_contactos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        print("Total de contactos: " +  str(len(lineas)))

if __name__ == "__main__":
    main()

