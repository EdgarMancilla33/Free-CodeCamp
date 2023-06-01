def main():
    print("operaciones del los archivos de texto: lectura ")

    #creo la lista de lineas (arreglo)de las lineas al guardar el archivo 
    lista_lineas = [
        "linea 1\n",
        "linea 2\n",
        "linea 3\n"
    
    ]
    #apertura del archivo para la ecritura 
    #sino existe lo crea , si existe lo abre para agregar al final
    with open ("archivo.txt","w") as archivo:
        archivo.writelines(lista_lineas)

    #apertura del archivo para lectura con metodo read
    with open ("archivo.txt","r") as archivo:
        #print (archivo.read())
        print ("5 bytes del archivo", archivo.read(4))
    
    with open ("archivo.txt","r") as archivo:
        print ("1 byte del archivo", archivo.readline())
    
    with open ("archivo.txt","r") as archivo:
        print (archivo.readlines())


if __name__ == "__main__":
    main()




