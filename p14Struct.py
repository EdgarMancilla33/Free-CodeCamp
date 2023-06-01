import struct

#********Mapa de caracteres********
#*nc--------------int-------------*
#*nombre----------string(20)------*
#*apellido--------string(30)------*
#*edad------------int-------------*
#*calif-----------float-----------*
#*carrera---------string(25)------*
#**********************************

def main():
    formato = struct.Struct("i 20s 30s i f 25s")

    # Registro de alumnos
    while True:
        print("Ingresa la matricula del estudiante: ")
        nc = int(input())
        print("Ingresa el nombre del estudiante: ")
        nombre = input()
        print("Ingresa el apellido del estudiante: ")
        apellido = input()
        print("Ingresa la edad del estudiante: ")
        edad = int(input())
        print("Ingresa la calificacion del estudiante: ")
        calif = float(input())
        print("Ingresa la carrera del estudiante: ")
        carrera = input()
        with open("data.bin", "ab") as file:
            file.write(formato.pack(nc, nombre.encode().strip(), apellido.encode().strip(), edad, calif, carrera.encode().strip()))
        print("Escriba s o S para salir, c o C para continuar ")
        opc = input()
        if opc.lower() == 's':
            break
        elif opc.lower() != 'c':
            print("Opcion no valida")

    # Búsqueda de registros por nombre
    print("Busqueda de registro por nombre")
    nombre_buscar = input("Ingresa el nombre del estudiante: ")
    encontrado = False
    with open("data.bin", "rb") as file:
        while True:
            registro = file.read(formato.size)
            if not registro:
                break
            nc, nombre, apellido, edad, calif, carrera = formato.unpack(registro)
            if nombre.decode().strip() == nombre_buscar:
                encontrado = True
                print("Numero de Control:", nc, "Nombre:", nombre.decode().strip(), "Apellido:", apellido.decode().strip(), "Edad:", edad, "Calificacion:", calif, "Carrera:", carrera.decode().strip())
    if not encontrado:
        print("Registro no encontrado para el nombre:", nombre_buscar)

if __name__ == "__main__":
    main()