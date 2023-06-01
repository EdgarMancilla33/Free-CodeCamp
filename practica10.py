import pickle


def main():
    print("Serialización de datos binarios")
    print("Ingresa la matricula del estudiante: ")
    matricula = input()
    print("Ingresa el nombre del alumno: ")
    nombre = input()
    print("Ingresa el apellido paterno del alumno: ")
    apellido_paterno = input()
    print("Ingresa el apellido matrno del alumno: ")
    apellido_materno = input()
    print("Ingresa la edad del alumno: ")
    edad = int(input())
    print("Ingresa el número telefónico del alumno: ")
    numero_tel = input()
    lista_datos = [matricula, nombre, apellido_paterno, apellido_materno, edad, numero_tel]
    with open("archivo.bin", "wb") as archivo:
        pickle.dump(lista_datos, archivo)
    print("Escritura binaria exitosa!!")

    with open("archivo.bin", "rb") as archivo:
        contenido = pickle.load(archivo)
        print(contenido)

if __name__ == "__main__":
    main()
