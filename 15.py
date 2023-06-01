import struct

# Definimos la estructura de cada registro
formato_registro = "10s f"

# Abrimos el archivo binario en modo lectura binaria
with open("data.bin", "rb") as archivo:
    # Pedimos al usuario que ingrese un nombre
    nombre = input("Ingrese el nombre a buscar: ")
    # Convertimos el nombre a bytes
    nombre_bytes = bytes(nombre, "utf-8")

    # Leemos el primer registro del archivo
    registro = archivo.read(struct.calcsize(formato_registro))

    # Recorremos el archivo buscando el registro correspondiente al nombre ingresado
    while registro:
        # Desempaquetamos el registro en una tupla de nombre y promedio
        registro_desempaquetado = struct.unpack(formato_registro, registro)

        # Si el nombre coincide, imprimimos el nombre y el promedio correspondiente
        if registro_desempaquetado[0].decode().strip() == nombre:
            print(f"El promedio de {nombre} es: {registro_desempaquetado[1]}")
            break

        # Leemos el siguiente registro del archivo
        registro = archivo.read(struct.calcsize(formato_registro))
    else:
        # Si no se encontró el registro, imprimimos un mensaje indicándolo
        print(f"No se encontró el registro correspondiente a {nombre}")


