def main():
    
    #Edgar y Ramón
    
    print("Archivo que lea los caracteres del texto")
    
    nombre = input("Ingresa el nombre del archivo ")

    with open(nombre, "w") as archivo:
        texto = input("Escribe dentro del archivo ")
        archivo.write(texto)
            
    with open(nombre, "r") as archivo:
        texto = archivo.read()
        contador = len (texto)
        
        print("El archivo tiene", contador, "caracteres.")
    

if __name__ == "__main__":
    main()