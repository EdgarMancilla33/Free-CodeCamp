import tkinter as tk
from tkinter import messagebox

import csv
     
def main():
    def funcion_guardar():
        
        print("Hice click!!")
        nombre = campo_nombre.get()
        apellidop = campo_apellidop.get()
        apellidom = campo_apellidom.get()
        nocontrol = campo_nocontrol.get()
        curp = campo_curp.get()
        print(nombre)
        print(apellidom)
        print(apellidop)
        print(nocontrol)
        print(curp)
        with open("estudiantes.csv", mode="a", newline='')as file:
            escritor = csv.writer(file,delimiter=",")
            estudiante = []
            estudiante.append(nombre)
            estudiante.append(apellidop)
            estudiante.append(apellidom)
            estudiante.append(nocontrol)
            estudiante.append(curp)
            escritor.writerow(estudiante)
            mensaje = messagebox.showinfo(message="Estudiante guardado con éxito",
                                          tittle="Información")
    
    print("funcion principal")
    window= tk.Tk()
    window.title("Ventana Principal")
    
    
    etiqueta_nombre=tk.Label(text="Nombre")
    etiqueta_nombre.pack()
    campo_nombre=tk.Entry()
    campo_nombre.pack()
    
    etiqueta_apellidop=tk.Label(text="Apellido Paterno")
    etiqueta_apellidop.pack()
    campo_apellidop=tk.Entry()
    campo_apellidop.pack()

    etiqueta_apellidom=tk.Label(text="Apellido Materno")
    etiqueta_apellidom.pack()
    campo_apellidom=tk.Entry()
    campo_apellidom.pack()

    etiqueta_nocontrol=tk.Label(text="Número de Control")
    etiqueta_nocontrol.pack()
    campo_nocontrol=tk.Entry()
    campo_nocontrol.pack()

    etiqueta_curp=tk.Label(text="CURP")
    etiqueta_curp.pack()
    campo_curp=tk.Entry()
    campo_curp.pack()

    boton_guardar=tk.Button(text="Guardar",command=funcion_guardar)
    boton_guardar.pack()
    window.mainloop()
     
if __name__ == "__main__":
    main()