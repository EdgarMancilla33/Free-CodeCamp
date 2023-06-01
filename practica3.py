def main():
    print("operaciones del los archivos de texto ")

    #creo la lista de lineas (arreglo)de las lineas al guardar el archivo 
    lista_lineas = [
        "linea 1\n",
        "linea 2\n",
        "linea 3\n",
        "linea 4\n"
    
    ]
    with open ("archivo.txt","a") as archivo:
        archivo.writelines(lista_lineas)


if __name__ == "__main__":
    main()




