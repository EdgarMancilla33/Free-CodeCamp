# Despliega los datos del archivo creado en la practica No. 6 solo si la linea comienza con Mayúscula
def main():
    print("Seleccionar la línea que tenga Mayúscula al principio")
    print("¿En qué archivo quieres escribir? Ingresa el nombre sin extensión")
    nombre_archivo = input()
    with open(nombre_archivo+".txt","r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea[0].isupper():
                print(linea)

if __name__ == "__main__":
    main()