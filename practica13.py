import struct

def main():
    print("Practica 13")
    # Estructura de formato para empaquetar y desempaquetar los datos.
    # "30s" significa que el primer valor es una cadena de 30 caracteres y "f" es un valor flotante de 4 bytes.
    rf = struct.Struct("30s f")
    while True:
        print("Ingrese el nombre: ")
        nombre = input()
        print("Ingrese el promedio: ")
        promedio = float(input())
        print("Escribe s o S pra salir, C o c para continuar: ")
        opcion = input()
        # Abrir el archivo en modo "ab" para agregar datos al final del archivo.
        with open("data.bin", "wb")as file:
            # Empaquetar los datos y escribirlos en el archivo.
            file.write(rf.pack((nombre.encode()), promedio))
        if opcion == "S" or opcion == "s":
            break
        elif opcion == "C" or opcion == "c":
            continue
        else:
            print("Opcion no válida")

    # Leer los datos del archivo.
    with open("data.bin", "rb")as file:
        while True:
            # Leer una cantidad de bytes igual al tamaño de la estructura.
            record = file.read(rf.size)
            if not record:
                break
            # Desempaquetar los datos leídos.
            nombre, promedio = rf.unpack(record)
            # Imprimir los datos desempaquetados.
            print("Nombre:", nombre.decode().strip(), "Promedio: ", promedio)

if __name__ == "__main__":
    main()
