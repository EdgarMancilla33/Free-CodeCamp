import tkinter as tk
import csv
from tkinter import messagebox
from tkinter import ttk

def main():

    def Editar_Contacto():
        def seleccionar_contacto():
            print("Click en seleccionar contacto")
            indices = lista_estudiantes.curselection()
            for i in indices:
                contacto_seleccionado = list(lista_estudiantes.get(i))
                print(contacto_seleccionado)
                
            no_control= contacto_seleccionado[3]
            messagebox.showinfo(
                title="Ítems seleccionados",
                # Obtener el texto de cada ítem seleccionado
                # y mostrarlos separados por comas.
                message=contacto_seleccionado
            )
            Ventana_Editar.destroy()
            bandera = False
            with open ("estudiantes.csv","r",newline="") as file: 
                contenido_archivo = csv.reader(file)
                print(contenido_archivo)
                for linea in contenido_archivo:
                    if no_control in linea:
                        print("estudiante encontrado")
                        registro = linea
                        bandera = True
                        break
                    
            if bandera == True:
                
                Ventana_Editar_Eestudiante = tk.Toplevel()
                
                etiqueta_nombre = tk.Label (Ventana_Editar_Eestudiante, text="nombre contacto: ")
                etiqueta_nombre.pack()
                campo_nombre= tk.Entry(Ventana_Editar_Eestudiante)
                campo_nombre.insert(0,registro[0])
                campo_nombre.pack()
                
                etiqueta_nombre = tk.Label (Ventana_Editar_Eestudiante, text="apellido paterno: ")
                etiqueta_nombre.pack()
                campo_apellidoP = tk.Entry(Ventana_Editar_Eestudiante)
                campo_apellidoP.insert(0,registro[2])
                campo_apellidoP.pack()
                
                
                
                etiqueta_nombre = tk.Label (Ventana_Editar_Eestudiante, text="apellido materno: ")
                etiqueta_nombre.pack()
                campo_apellidoM = tk.Entry(Ventana_Editar_Eestudiante)
                campo_apellidoM.insert(0,registro[2])
                campo_apellidoM.pack()
                
                etiqueta_nombre = tk.Label (Ventana_Editar_Eestudiante, text="no de control: ")
                etiqueta_nombre.pack()
                campo_noconrol = tk.Entry(Ventana_Editar_Eestudiante)
                campo_noconrol.insert(0,registro[3])
                campo_noconrol.pack()
                
                etiqueta_nombre = tk.Label (Ventana_Editar_Eestudiante, text=" curp ")
                etiqueta_nombre.pack()
                campo_curp = tk.Entry(Ventana_Editar_Eestudiante)
                campo_curp.insert(0,registro[4])
                campo_curp.pack()
                
                boton_guardar = tk.Button (Ventana_Editar_Eestudiante, text=" actualizar contacto ")
                boton_guardar.pack()
                
                
                
                
                
                
                Ventana_Editar_Eestudiante.mainloop
                
            
        
        Ventana_Editar = tk.Toplevel()
        lista_estudiantes = tk.Listbox(Ventana_Editar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("estudiantes.csv","r",newline="") as file:
                lector = csv.reader(file)
                print(lector)
                contactos = list(lector)
                print(contactos)
                lista_estudiantes.insert(0,*contactos)
        boton_seleccionar = tk.Button(Ventana_Editar,text="Seleccionar contacto",
                                       command=seleccionar_contacto)
        boton_seleccionar.pack()
        Ventana_Editar.mainloop()

    def Crear_Contacto():
        def guardar():
            nombre= campo_nombre.get()
            apellidoP = campo_apellidoP.get()
            apellidoM = campo_apellidoM.get()
            noControl = campo_noControl.get()
            curp = campo_CURP.get()
            with open("estudiantes.csv",mode="a",newline="") as file:
                escritor = csv.writer(file, delimiter=",")
                estudiante = []
                estudiante.append(nombre)
                estudiante.append(apellidoP)
                estudiante.append(apellidoM)
                estudiante.append(noControl)
                estudiante.append(curp)
                escritor.writerow(estudiante)
                mensaje = messagebox.showinfo(message="Estudiante guardado con exito",
                                            title="Información")
                Ventana_Crear.destroy()

        Ventana_Crear= tk.Toplevel()
        #Aqui agregar el contenido para 
        #crear contacto
        etiqueta_nombre = tk.Label(Ventana_Crear, text="Nombre Contacto:")
        etiqueta_nombre.pack()
        campo_nombre = tk.Entry(Ventana_Crear)
        campo_nombre.pack()

        etiqueta_apellidoP = tk.Label(Ventana_Crear, text="Apellido Paterno:")
        etiqueta_apellidoP.pack()
        campo_apellidoP = tk.Entry(Ventana_Crear)
        campo_apellidoP.pack()

        etiqueta_apellidoM = tk.Label(Ventana_Crear, text="Apellido Materno:")
        etiqueta_apellidoM.pack()
        campo_apellidoM = tk.Entry(Ventana_Crear)
        campo_apellidoM.pack()

        etiqueta_noControl = tk.Label(Ventana_Crear, text="No Control:")
        etiqueta_noControl.pack()
        campo_noControl = tk.Entry(Ventana_Crear)
        campo_noControl.pack()

        etiqueta_CURP = tk.Label(Ventana_Crear, text="CURP:")
        etiqueta_CURP.pack()
        campo_CURP = tk.Entry(Ventana_Crear)
        campo_CURP.pack()

        boton_guardar = tk.Button(Ventana_Crear, text="Guardar",command=guardar)
        boton_guardar.pack()
        Ventana_Crear.mainloop()

    print("Función principal")
    root = tk.Tk()
    root.title("Agenda de Contactos")
    root.geometry("500x500")
    #Menu
    menu_bar = tk.Menu(root)
    menu = tk.Menu(root,tearoff=0)
    menu_bar.add_cascade(label="Opciones", menu=menu)
    menu.add_command(label="Crear Contacto",command=Crear_Contacto)
    menu.add_command(label="Editar Contacto", command=Editar_Contacto)
    menu.add_command(label="Eliminar Contacto")
    menu.add_command(label="Listar Contactos")
    menu.add_command(label="Salir")
    root.config(menu=menu_bar)
    root.mainloop()

if __name__ == "__main__":
    main()