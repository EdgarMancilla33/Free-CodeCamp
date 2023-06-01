import tkinter as tk
import csv
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from tkinter import ttk

def main():
    def Editar_Contacto():
        def seleccionar_estudiante():
            def actualizar_estudiante():
                print("Click en el botón para actualizar estudiante")
                nombre_n = campo_nombre.get()
                apellidoP_n = campo_apellidoP.get()
                apellidoM_n = campo_apellidoM.get()
                edad_n = campo_edad.get()
                genero_n = campo_genero.get()
                no_control_n = campo_noControl.get()
                curp_n = campo_CURP.get()
                registro_nuevo = [
                    nombre_n, apellidoP_n, apellidoM_n, edad_n, genero_n, no_control_n, curp_n
                ]
                print(registro_nuevo)
                print(contador)
                with open("estudiantes.csv", "r", newline="") as file:
                    contenido = list(csv.reader(file))
                    for i, linea in enumerate(contenido):
                        if registro in linea:
                            contenido[i] = registro_nuevo
                            break
                print("contenido nuevo", contenido)
                with open("estudiantes.csv", "w", newline="") as file:
                    escritor = csv.writer(file)
                    escritor.writerows(contenido)
                print("archivo modificado")
                Ventana_Editar_Estudiante.destroy()

            print("Click en el estudiante que desea seleccionar")
            indices = lista_estudiantes.curselection()
            for i in indices:
                contacto_seleccionado = list(lista_estudiantes.get(i))
                print(contacto_seleccionado)

            no_control = contacto_seleccionado[5]
            messagebox.showinfo(title="Items seleccionados", message=contacto_seleccionado)

            Ventana_Editar.destroy()
            bandera = False
            registro = None
            with open("estudiantes.csv", "r", newline="") as file:
                contenido_archivo = csv.reader(file)
                print(contenido_archivo)
                contador = 0
                for linea in contenido_archivo:
                    if no_control in linea:
                        print("Estudiante encontrado")
                        registro = linea
                        bandera = True
                        break
                    contador += 1
                print(contador)
            if bandera:
                Ventana_Editar_Estudiante = tk.Toplevel()
                etiqueta_nombre = tk.Label(Ventana_Editar_Estudiante, text="Nombre Contacto:")
                etiqueta_nombre.pack()
                campo_nombre = tk.Entry(Ventana_Editar_Estudiante)
                campo_nombre.insert(0, registro[0])
                campo_nombre.pack()

                etiqueta_apellidoP = tk.Label(Ventana_Editar_Estudiante, text="Apellido Paterno:")
                etiqueta_apellidoP.pack()
                campo_apellidoP = tk.Entry(Ventana_Editar_Estudiante)
                campo_apellidoP.insert(0, registro[1])
                campo_apellidoP.pack()

                etiqueta_apellidoM = tk.Label(Ventana_Editar_Estudiante, text="Apellido Materno:")
                etiqueta_apellidoM.pack()
                campo_apellidoM = tk.Entry(Ventana_Editar_Estudiante)
                campo_apellidoM.insert(0, registro[2])
                campo_apellidoM.pack()

                etiqueta_edad = tk.Label(Ventana_Editar_Estudiante, text="Edad:")
                etiqueta_edad.pack()
                campo_edad = tk.Entry(Ventana_Editar_Estudiante)
                campo_edad.insert(0, registro[3])
                campo_edad.pack()

                etiqueta_genero = tk.Label(Ventana_Editar_Estudiante, text="Sexo:")
                etiqueta_genero.pack()
                campo_genero = tk.Entry(Ventana_Editar_Estudiante)
                campo_genero.insert(0, registro[4])
                campo_genero.pack()

                etiqueta_noControl = tk.Label(Ventana_Editar_Estudiante, text="No Control:")
                etiqueta_noControl.pack()
                campo_noControl = tk.Entry(Ventana_Editar_Estudiante)
                campo_noControl.insert(0, registro[5])
                campo_noControl.pack()

                etiqueta_CURP = tk.Label(Ventana_Editar_Estudiante, text="CURP:")
                etiqueta_CURP.pack()
                campo_CURP = tk.Entry(Ventana_Editar_Estudiante)
                campo_CURP.insert(0, registro[6])
                campo_CURP.pack()

                boton_actualizar = tk.Button(Ventana_Editar_Estudiante, text="Actualizar Contacto",
                                            command=actualizar_estudiante, bg='#800080', fg="white", font=("Arial", 12),
                                            width=15)
                boton_actualizar.pack()
                Ventana_Editar_Estudiante.mainloop()
                    
        Ventana_Editar = tk.Toplevel()
        Ventana_Editar.config(bg='#008080')
        Ventana_Editar.geometry("400x300")
        lista_estudiantes = tk.Listbox(Ventana_Editar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("estudiantes.csv", "r", newline="") as file:
            lector = csv.reader(file)
            contactos = list(lector)
            for contacto in contactos:
                lista_estudiantes.insert(tk.END, contacto)
        boton_seleccionar = tk.Button(Ventana_Editar, text="Seleccionar contacto", command=seleccionar_estudiante, bg='#008080', fg="white", font=("Arial", 12), width=20)
        boton_seleccionar.pack()
        Ventana_Editar.mainloop()

    def Crear_Contacto():
        def guardar():
            nombre = campo_nombre.get()
            apellidoP = campo_apellidoP.get()
            apellidoM = campo_apellidoM.get()
            edad = campo_edad.get()
            genero = campo_genero.get()
            noControl = campo_noControl.get()
            curp = campo_CURP.get()
            with open("estudiantes.csv", mode="a", newline="") as file:
                escritor = csv.writer(file, delimiter=",")
                estudiante = [nombre, apellidoP, apellidoM, edad, genero, noControl, curp]
                escritor.writerow(estudiante)
                mensaje = messagebox.showinfo(message="Estudiante guardado con éxito", title="Información")
            Ventana_Crear.destroy()

        Ventana_Crear = tk.Toplevel()
        Ventana_Crear.config(bg='#008080')
        Ventana_Crear.geometry("400x300")

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

        etiqueta_edad = tk.Label(Ventana_Crear, text="Edad:")
        etiqueta_edad.pack()
        campo_edad = tk.Entry(Ventana_Crear)
        campo_edad.pack()

        etiqueta_genero = tk.Label(Ventana_Crear, text="Género:")
        etiqueta_genero.pack()
        campo_genero = tk.Entry(Ventana_Crear)
        campo_genero.pack()

        etiqueta_noControl = tk.Label(Ventana_Crear, text="No Control:")
        etiqueta_noControl.pack()
        campo_noControl = tk.Entry(Ventana_Crear)
        campo_noControl.pack()

        etiqueta_CURP = tk.Label(Ventana_Crear, text="CURP:")
        etiqueta_CURP.pack()
        campo_CURP = tk.Entry(Ventana_Crear)
        campo_CURP.pack()

        boton_guardar = tk.Button(Ventana_Crear, text="Guardar", command=guardar, bg='#008080', fg="white", font=("Arial", 12), width=10)
        boton_guardar.pack()

        Ventana_Crear.mainloop()
        Ventana_Crear.destroy()

    def Listar_Contacto():
        ventana_listar = tk.Toplevel()
        ventana_listar.config(bg='#008080')
        ventana_listar.geometry("400x200")

        lista_estudiantes = tk.Listbox(ventana_listar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()

        with open("estudiantes.csv", "r", newline="") as file:
            lector = csv.reader(file)
            contactos = list(lector)
            lista_estudiantes.insert(0, *contactos)

        ventana_listar.mainloop()

    
    def Eliminar_Contacto():

        def seleccionar_estudiante():
            print("Click en el estudiante que desea seleccionar")
            indices = lista_estudiantes.curselection()
            contacto_seleccionado = list(lista_estudiantes.get(indices))
            no_control = contacto_seleccionado[5]
            ventana_eliminar.destroy()
            nuevo = []
            with open("estudiantes.csv", "r", newline="") as file:
                contenido_archivo = csv.reader(file)
                for linea in contenido_archivo:
                    if no_control not in linea:
                        nuevo.append(linea)
            with open("estudiantes.csv", "w", newline="") as file:
                escritor = csv.writer(file)
                escritor.writerows(nuevo)
            print("Archivo Modificado")
            messagebox.showinfo(title="Contacto Eliminado", message="Contacto eliminado con éxito")

        ventana_eliminar = tk.Toplevel()
        ventana_eliminar.config(bg='#008080')
        ventana_eliminar.geometry("400x200")

        lista_estudiantes = tk.Listbox(ventana_eliminar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()

        with open("estudiantes.csv", "r", newline="") as file:
            lector = csv.reader(file)
            contactos = list(lector)
            lista_estudiantes.insert(0, *contactos)

        boton_seleccionar = tk.Button(ventana_eliminar, text="Seleccionar contacto", command=seleccionar_estudiante, bg='#800080', fg="white", font=("Arial", 12), width=20)
        boton_seleccionar.pack()

        ventana_eliminar.mainloop()

        
    def Salir():
        root.destroy()
        
    def Reporte():
        def Grafico():
            print("Reporte Gráfico")

            # Gráfica de Pastel (Género)
            # Leer el archivo CSV
            with open("estudiantes.csv", "r") as archivo:
                lector = csv.reader(archivo)
                # Saltar la primera línea que contiene los encabezados
                next(lector)
                masculinos = 0
                femeninos = 0
                for fila in lector:
                    # Si la columna de género es "Masculino", incrementar el contador de hombres.
                    if fila[4] == "Masculino":
                        masculinos += 1
                    # Si la columna de género es "Femenino", incrementar el contador de mujeres.
                    elif fila[4] == "Femenino":
                        femeninos += 1

            # Crear listas con los datos para el gráfico
            categorias = ["Masculinos", "Femeninos"]
            num_estudiantes = [masculinos, femeninos]

            # Colores para el gráfico
            colores = ["blue", "pink"]

            # Crear una figura y un gráfico de pastel
            figura, ax = plt.subplots()
            ax.pie(num_estudiantes, labels=categorias, autopct="%1.1f%%", colors=colores)

            # Configurar el título del gráfico
            ax.set_title("Conteo de estudiantes por género")

            # Mostrar el gráfico
            plt.show()

        ventana_reporte = tk.Toplevel()
        ventana_reporte.config(bg='#008080')
        ventana_reporte.geometry("400x200")

        boton_grafico = tk.Button(ventana_reporte, text="Generar Gráfico", command=Grafico, bg='#800080', fg="white", font=("Arial", 12), width=20)
        boton_grafico.pack()

        ventana_reporte.mainloop()
                

            
    def Tabular():
        print("Reporte Tabular")
        ventana_reporte_tabular = tk.Toplevel()
        columnas = ["Nombre", "A.Paterno", "A.Materno", "Edad", "Sexo", "No.Control", "CURP"]
        tree = ttk.Treeview(ventana_reporte_tabular, columns=columnas, show="headings")

        tree.heading("Nombre", text="Nombre Estudiante")
        tree.heading("A.Paterno", text="Apellido Paterno")
        tree.heading("A.Materno", text="Apellido Materno")
        tree.heading("Edad", text="Edad")
        tree.heading("Sexo", text="Sexo")
        tree.heading("No.Control", text="No. de Control")
        tree.heading("CURP", text="CURP")

        with open("estudiantes.csv", "r") as file:
            lector = csv.reader(file)
            contactos = list(lector)
            for contacto in contactos:
                tree.insert("", tk.END, values=contacto)
        tree.pack()

        ventana_reporte_tabular.mainloop()
            
            
        def Jerarquica():
            print("Reporte Jerarquico")

            # Creación de la ventana del Reporte Jerarquico
            ventana_reporte_jerarquico = tk.Toplevel()
            ventana_reporte_jerarquico.title("Reporte de Estudiantes")
            ventana_reporte_jerarquico.config(bg='#008080')
            ventana_reporte_jerarquico.geometry("400x300")

            treeview = ttk.Treeview(ventana_reporte_jerarquico)
            treeview.pack()

            with open("estudiantes.csv", "r") as file:
                lector = csv.reader(file)
                contactos = list(lector)

                for contacto in contactos:
                    if not treeview.exists(contacto[4]):
                        treeview.insert("", tk.END, contacto[4], text=contacto[4])

                    if contacto[4] == "Femenino":
                        treeview.insert("Femenino", tk.END, text=contacto[0])
                    elif contacto[4] == "Masculino":
                        treeview.insert("Masculino", tk.END, text=contacto[0])

            ventana_reporte_jerarquico.mainloop()
            
            
                
        
        Ventana_Reporte = tk.Toplevel()
        Ventana_Reporte.config(bg='#008080')
        Ventana_Reporte.geometry("400x200")

        # Personalizar botón "Reporte Gráfico"
        boton_reporgrafico = tk.Button(Ventana_Reporte, text="Reporte Gráfico", command=Grafico, bg='#FFA500', fg="white", font=("Arial", 12))
        boton_reporgrafico.place(x=150, y=10)

        # Personalizar botón "Reporte Tabular"
        boton_reportabular = tk.Button(Ventana_Reporte, text="Reporte Tabular", command=Tabular, bg='#008000', fg="white", font=("Arial", 12))
        boton_reportabular.place(x=150, y=50)

        # Personalizar botón "Reporte Jerárquico"
        boton_reporjerarquico = tk.Button(Ventana_Reporte, text="Reporte Jerárquico", command=Jerarquica, bg='#FF0000', fg="white", font=("Arial", 12))
        boton_reporjerarquico.place(x=143, y=90)

        Ventana_Reporte.mainloop()
        
        
        

    # Contenido dentro de la ventana principal
    print("Función principal")
    root = tk.Tk()
    root.title("Registro de Estudiantes")
    root.geometry("500x500")
    root.configure(bg='#800080')
    
    # Crear una etiqueta 
    text_label = tk.Label(root, text="Registro de Estudiantes ", font=("Arial", 20), bg='#800080')
    text_label.pack(pady=20)
    
    # Cargar la imagen
    image = Image.open("C:\\Users\\edgar\\OneDrive\\Imágenes\\383px-Oxford-University-Circlet.png")
    photo = ImageTk.PhotoImage(image)
    imagen_widget = tk.Label(root, image=photo)
    imagen_widget.pack()

    
    #Menu
    menu_bar = tk.Menu(root)
    menu = tk.Menu(root,tearoff=0)
    menu_bar.add_cascade(label="Opciones", menu=menu)
    menu.add_command(label="Crear Contacto",command=Crear_Contacto)
    menu.add_command(label="Editar Contacto", command=Editar_Contacto)
    menu.add_command(label="Eliminar Contacto", command=Eliminar_Contacto)
    menu.add_command(label="Listar Contactos", command=Listar_Contacto)
    menu.add_command(label="Reporte", command=Reporte)
    menu.add_command(label="Salir", command=Salir)
    root.config(menu=menu_bar)
    root.mainloop()

if __name__ == "__main__":
    main()