import json
def main():
    
    print("Ejercicio 3: Creación y escritura de archivo JSON")
    
    # se crea la lista para almacenar los datos de los estudiantes
    estudiantes = []

    bandera = True
    while(bandera==True):
        print("1) Crear registro del estudiante ")
        print("2) Modificar registro ")
        print("3) Eliminar registro ")
        print("Presione s o S para salir" )
        opcion = input()

        if opcion == "1":
            print("Ingrese el nombre del estudiante:")
            campo_nombre = input()
            print("Ingrese el apellido paterno: ")
            campo_apellidoP = input()
            print("Ingrese el apellido materno: ")
            campo_apellidoM = input()
            print("Ingrese el número de control: ")
            campo_noControl = input()
            print("Ingrese el CURP: ")
            campo_CURP = input()
            print("Ingrese el correo electrónico: ")
            campo_correo = input()
                
            estudiante = {
                'Nombre': campo_nombre, 
                'Apellido_Paterno': campo_apellidoP, 
                'Apellido_Materno': campo_apellidoM, 
                'No. de Control': campo_noControl, 
                'CURP': campo_CURP, 
                'Correo electrónico': campo_correo
                }
            estudiantes.append(estudiante)
            print("Registro agregado con éxito!")

            # garda lso datos dentro de estudiantes.json 
            with open('estudiantes.json', 'w') as f:
                json.dump(estudiantes, f)
                print("Datos guardados en el archivo estudiantes.json")

        if opcion == "2":
            # modificar el archivo
            print("Ingresa No. de Control a buscar: ")
            noControl_buscar = input()
            with open("estudiantes.json", "r") as file:
                reader = json.load(file)
                estudiantes_copia = []
                print(reader)
                for estudiante in reader: 
                    print('Estudiante', estudiante)             
                    if estudiante ['No. de Control'] == noControl_buscar:
                        print("Encontrado")
                        print("Ingresa los nuevos datos: ")
                        print("Nuevo nombre: ")
                        nNombre = input()
                        print("Nuevo Apellido Paterno: ")
                        nApellidoPaterno = input()
                        print("Nuevo Apellido Materno: ")
                        nApellidoMaterno = input()
                        print("Nuevo CURP: ")
                        nCURP = input()
                        print("Nuevo Correo: ")
                        nCorreo = input()
                        estudiante['Nombre'] = nNombre
                        estudiante['Apelldo_Paterno'] = nApellidoPaterno
                        estudiante['Apelldo_Materno'] = nApellidoMaterno
                        estudiante['CURP'] = nCURP
                        estudiante['Correo'] = nCorreo
                        print(estudiante)
                    estudiantes_copia.append(estudiante)
                    print("hola",estudiantes_copia)

            with open("estudiantes.json", "w") as file:
                json.dump(estudiantes_copia, file)  

        if opcion == "3":
             # elimina el contenido del archivo
            print("Ingresa No. de Control a eliminar: ")
            noControl_buscar = input()
            with open("estudiantes.json", "r") as file:
                reader = json.load(file)
                estudiantes_copia = []
                print(reader)
                for estudiante in reader:              
                    if estudiante ['No. de Control'] == noControl_buscar:
                        print("Encontrado para eliminar")
                    else:
                        estudiantes_copia.append(estudiante)
                
                print(estudiantes_copia)
            
            with open("estudiantes.json", "w") as file:
                json.dump(estudiantes_copia, file)

        elif opcion =="s" or opcion =="S":
            bandera = False
        else:
            bandera = True

if __name__ == "__main__":
    main()
    
