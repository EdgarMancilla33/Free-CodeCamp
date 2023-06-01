def main():
    print(".:::Creacion de archivos:::.")
    #crear archivo metodo no .1
    #archivo = open("prueva.txt","w")
    #archivo.close()
    #print("--> archivo creado")
    #crear archivos metodo2 

    with open ("prueva3.txt","w") as archivo:
        print("archivo creado con exito")
        
if __name__ == "__main__":
    main()