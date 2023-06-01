#escribe en un programa de python que acepte oraciones o cadenas de caracteres hasta que el usuario ingrese la cadena "END", y que guarde los datos dentro de un archivo de texto 


def main():
    print("escribe lo que desees ya l final , teclea la palabra END , para salir")
    
    with open ("LOLITA.txt","w") as archivo:
        print("archivo creado con exito")

        while True:
            cadena = input('Ingresa una cadena de texto (o END para terminar): ')

            if cadena == 'END':
                break  

            archivo.write(cadena + '\n')

        archivo.close()

if __name__ == "__main__":
    main()

    #ejemplo de la maestra 
    
        




 