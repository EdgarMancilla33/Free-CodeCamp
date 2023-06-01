import struct

def main():
    print("p14 Registro de alumnos")
    formato = struct.Struct("i 20s 30s i f 25s")      
             
    while(True):
        print("Ingresa la matricula del estudiante: ")
        nc = int(input())
        print("Ingresa el nobre de estudiante: ")
        nombre = input()
        print("Ingresa el apellido del estudiante: ")
        apellido = input()
        print("Ingresa la edad del estudiante: ")
        edad = int(input())
        print("Ingresa la calificacion del estudiante: ")
        calif = float(input()) 
        print("Ingresa la carrera del estudiante: ")
        carrera = input()
        print("Escripa s o S para salir, c O C para continuar ")
        opc = input()
        with open("data.bin", "wb") as file:
                file.write (formato.pack(nc, nombre.encode().strip(), apellido.encode().strip(), edad, calif, carrera.encode().strip()))
            
        if opc == 'S' or opc == "s": 
            break
            
        elif opc == 'c' or opc == "C":
            continue
        
        else:
            print("Opcion no valida")
            
    print("Ingresa el nombre de deseas buscar")
    busacar = input()
       
    with open("data.bin", "rb") as file:
        while True:
            registro = file.read(formato.size)
            if not registro:
                break
            nc, nombre, apellido, edad, calif, carrera = formato.unpack(registro)
            print(nombre)
            if busacar == nombre.decode().strip("\x00"):
                print("Numero de Control: ", nc, "Nomnbre: ", nombre.decode().strip(), "Apellido: ", apellido.decode().strip(), "Edad: ",edad, "Calificacion: ", calif, "Carrera", carrera.decode().strip())       

        
if __name__ == "__main__":
    main()

        en python a nivel prinsipiante 
        1has un menu de opciones con ciclo while, debera contar con una opcion de salir del programa
        
        2 opcion para crear un archivo para registrar contactos considerando el nombre que el usuario quiera usar para su crecion 
        3 opcion para solicitar en que archivo ingresar los contactos , e insertar registros de contactos hasta que presione s o S .para cada registro a insertar deberan pedir nombre completo,direccion ,telefono.
        4opcion para solisitar de que archivo leer los contactos , e imprimir el registro del contacto buscando por su numero de telefono 
        5 opcion para imprimir todos los registros linea por linea de los contactos del archivo
        6 opcion para imprimir el total de contactos registrados en el archivo 
    