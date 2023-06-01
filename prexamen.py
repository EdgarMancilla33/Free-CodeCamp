
1) Crear un archivo de texto empleando el nombre del archivo definido por el usuario (5 pts). 
2) Insertar registros en un archivo de texto hasta que el usuario presione "S" o "s". (15 pts)
3) leer e imprimir en pantalla todos los registros de un archivo línea por línea. (20 pts) 
4) buscar un registro determinado por el usuario en el archivo. (20 pts) 
5) Imprimir en pantalla las líneas del archivo de texto numeradas. (20 pts).
#6) Imprimir en pantalla las líneas del archivo de texto impares (20 pts).

def main():

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