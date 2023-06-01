import pickle
def main():
    nombre = None
    apellidos = None
    celular = None
    print("serializacion de datos binarios : diccionario")
    print("ingresa el nombre del contacto:")
    nombre_contacto = input()
    print("ingrsa el apellido del contacto:")
    apellido_contacto = input()
    print("ingresa el numero del celular:")
    numero_celular = input()
   
    contacto = {
        "nombre": nombre_contacto,
        "apellidos": apellido_contacto,
        "celular": numero_celular
    }

    with open ("contactos.bin", "wb") as archivo:
        pickle.dump(contacto,archivo)

    with open ("contactos.bin", "rb") as archivo:
        print (pickle.load(archivo))

        while True:
            try:
                registro = pickle.load(archivo)
            except E0FError:
                break




if __name__ == "__main__":
    main()