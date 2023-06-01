def main():
    print ("Serializacion de los datos binarios")
    print ("ingresa la metricula del estudiante ")
    matricula = input()
    print ("ingrsa el nombre del estudiante ")

    print ("ingresa ek apellido del estudiante")
    print ("ingresa el apellido materno del estudiante ")
    print ("ingresa la edad del estudiante ")
    print ("numero de telefonfo ferl resudiante")
    
    lista_datos = [
        matricula,
        nombre,
        apellido_paterno,
        apellido materno,
        edad,
        numero_tel

        ]
    with open ("archivo.bin","wb") as archivo

    print("escritura binaria exitosa")
    with open ("archivo.bin","rb") as archivo
        contenido = pikle.load(archivo)
        print (contenido)
if __name__ == "__main__":
    main()