def main():
    print("funcion prinsipal")
    bandera = True
    while   (bandera==True):
        print("ingresa un numero entero ")
        numero1 = int(input())
        print("ingresa otro numero entero ")
        numero2 = int(input())
        resultado = numero1 + numero2
        print("resultado",resultado)
        print("presiona s para salir ")
        opcion = input
        if opcion =="s" or opcion =="S":
            bandera = False
        else:
            bandera = True


if __name__ == "__main__":
    main()