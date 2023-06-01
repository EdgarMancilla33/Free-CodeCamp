import pickle

def main():

    lista = []
    print("Serialización de datos binarios: diccionario")

    # Solicitamos los datos del contacto
    print("Ingresa el nombre del contacto: ")
    nombre_contacto = input()
    print("Ingresa el apellido del contacto: ")
    apellido_contacto = input()
    print("Ingresa el número de celular del contacto: ")
    numero_celular = input()

    # Creamos un diccionario con los datos del contacto
    contacto = {
        "nombre": nombre_contacto,
        "apellidos": apellido_contacto,
        "celular": numero_celular
    }

    # Imprimimos el tipo de dato del diccionario creado
    print(type(contacto))

    # Imprimimos los valores de las claves del diccionario
    print(contacto["nombre"])
    print(contacto["apellidos"])
    print(contacto["celular"])

    # Guardamos el diccionario serializado en un archivo binario
    with open("contacto.bin", "ab") as archivo:
        pickle.dump(contacto,archivo)

    # Leemos los registros del archivo binario y los guardamos en una lista
    with open("contacto.bin", "rb") as archivo:
        while True:
            try:
                registro = pickle.load(archivo)
            except EOFError:
                # Si llegamos al final del archivo, salimos del ciclo
                break
            lista.append(registro)

    # Imprimimos la lista de registros leídos del archivo binario
    print(lista)

if __name__ == "__main__":
    main()
