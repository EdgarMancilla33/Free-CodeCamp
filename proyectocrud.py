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
                registro_nuevo = []
                registro_nuevo.append(nombre_n)
                registro_nuevo.append(apellidoP_n)
                registro_nuevo.append(apellidoM_n)
                registro_nuevo.append(edad_n)
                registro_nuevo.append(genero_n)
                registro_nuevo.append(no_control_n)
                registro_nuevo.append(curp_n)
                print(registro_nuevo)
                print(contador)
                with open("tareas.csv", "r", newline="") as file:
                    contenido = csv.reader(file)
                    contenido = list(contenido)
                    for linea in contenido:
                        if registro in linea:
                            contenido.pop(contador)
                            contenido.insert(contador, registro_nuevo)
                            break
                        contador += 1
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
            with open("tareas.csv", "r", newline="") as file:
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

                etiqueta_genero = tk.Label(Ventana_Editar_Estudiante, text="Género:")
                etiqueta_genero.pack()
                campo_genero = tk.Entry(Ventana_Editar_Estudiante)
                campo_genero.insert(0, registro[4])
                campo_genero.pack()

                etiqueta_noControl = tk.Label(Ventana_Editar_Estudiante, text="No. Control:")
                etiqueta_noControl.pack()
                campo_noControl = tk.Entry(Ventana_Editar_Estudiante)
                campo_noControl.insert(0, registro[5])
                campo_noControl.pack()

                etiqueta_CURP = tk.Label(Ventana_Editar_Estudiante, text="CURP:")
                etiqueta_CURP.pack()
                campo_CURP = tk.Entry(Ventana_Editar_Estudiante)
                campo_CURP.insert(0, registro[6])
                campo_CURP.pack()

                boton_actualizar = tk.Button(Ventana_Editar_Estudiante, text="Actualizar", command=actualizar_estudiante)
                boton_actualizar.pack()

        Ventana_Editar = tk.Toplevel()
        Ventana_Editar.title("Editar estudiante")
        Ventana_Editar.geometry("400x400")

        scrollbar = tk.Scrollbar(Ventana_Editar)
        scrollbar.pack(side="right", fill="y")

        lista_estudiantes = tk.Listbox(Ventana_Editar, yscrollcommand=scrollbar.set)
        lista_estudiantes.pack(side="left", fill="both")

        scrollbar.config(command=lista_estudiantes.yview)

        with open("tareas.csv", "r", newline="") as file:
            contenido = csv.reader(file)
            for linea in contenido:
                lista_estudiantes.insert("end", linea)
        
        boton_seleccionar = tk.Button(Ventana_Editar, text="Seleccionar", command=seleccionar_estudiante)
        boton_seleccionar.pack()

        Ventana_Editar.mainloop()
        
        
        #11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        #crear_tarea
    def Crear_Contacto():
        def guardar():
            nombre = campo_nombre.get()
            apellidoP = campo_apellidoP.get()
            texto = campo_texto.get("1.0", "end-1c")  # Obtener el texto ingresado en el campo de texto
            
            with open("tareas.csv", mode="a", newline="") as file:
                escritor = csv.writer(file, delimiter=",")
                estudiante = [nombre, apellidoP, texto]  # Agregar el texto ingresado a la lista de estudiante
                
                escritor.writerow(estudiante)
            
            mensaje = messagebox.showinfo(message="Tarea guardada con exito", title="Información")
            Ventana_Crear.destroy()

        Ventana_Crear = tk.Toplevel()
        Ventana_Crear.config(bg='#008080')
        Ventana_Crear.geometry("400x400")

        etiqueta_nombre = tk.Label(Ventana_Crear, text="Titulo de la tarea:")
        etiqueta_nombre.pack()
        campo_nombre = tk.Entry(Ventana_Crear)
        campo_nombre.pack()

        etiqueta_apellidoP = tk.Label(Ventana_Crear, text="Fecha de entrega")
        etiqueta_apellidoP.pack()
        campo_apellidoP = tk.Entry(Ventana_Crear)
        campo_apellidoP.pack()

        etiqueta_texto = tk.Label(Ventana_Crear, text="Texto:")
        etiqueta_texto.pack()
        campo_texto = tk.Text(Ventana_Crear, height=5)
        campo_texto.pack()

        boton_guardar = tk.Button(Ventana_Crear, text="Guardar", command=guardar, bg='#008080', fg="white", font=("Arial", 12), width=10)
        boton_guardar.pack()

        Ventana_Crear.mainloop()
        Ventana_Crear.destroy()

        

        
        boton_guardar = tk.Button(Ventana_Crear, text="Guardar", command=guardar, bg='#008080', fg="white", font=("Arial", 12), width=10)
        boton_guardar.pack()
        Ventana_Crear.mainloop()
        Ventana_Crear.destroy()
        
        #11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        #2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        
        
        #Listar_Pendientes 
    def Listar_Contacto():
        ventana_listar = tk.Toplevel()
        ventana_listar.config(bg='#008080')
        ventana_listar.geometry("400x200")
        contacto=[]
        lista_estudiantes = tk.Listbox(ventana_listar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("tareas.csv","r",newline="")as file:
            lector = csv.reader(file)
            print(lector)
            contactos = list(lector)
            print(contactos)
            lista_estudiantes.insert(0,*contactos)
        ventana_listar.mainloop()
        #2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        #Eliminar_Tarea 
    def Eliminar_Contacto():

        def seleccionar_estudiante():
            print("Click en la tarea qur desea eliminar")
            indices = lista_estudiantes.curselection()
            contacto_seleccionado = list(lista_estudiantes.get(indices))
            no_control = contacto_seleccionado[3]
            ventana_eliminar.destroy()
            nuevo = []
            with open("tareas.csv","r",newline="") as file:
                contenido_archivo = csv.reader(file)
                for linea in contenido_archivo:
                    if no_control in linea:
                        print("Tarea encontrada")
                    else:
                        nuevo.append(linea)
            with open("tareas.csv", "w", newline="") as file:
                escritor = csv.writer(file)
                escritor.writerows(nuevo)
            print("Archivo Modificado")
            messagebox.showinfo(title="Tarea Eliminada", message=contacto_seleccionado)

        ventana_eliminar = tk.Toplevel()
        ventana_eliminar.config(bg='#008080')
        ventana_eliminar.geometry("400x200")
        lista_estudiantes = tk.Listbox(ventana_eliminar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("tarea.csv","r",newline="")as file:
            lector = csv.reader(file)
            print(lector)
            contactos = list(lector)
            print(contactos)
            lista_estudiantes.insert(0,*contactos)
        boton_seleccionar = tk.Button(ventana_eliminar, text="Seleccionar tarea", command=seleccionar_estudiante, bg='#800080', fg="white", font=("Arial", 12), width=20)
        boton_seleccionar.pack()
        ventana_eliminar.mainloop()
        
    def Salir():
        root.destroy()
        
    def Reporte():
        
        def Grafico():
            print("Reporte Gráfico")
            
            # Gráfica de Pastal (Género)
            # Leer el archivo CSV
            with open("estudiantes.csv", "r") as archivo:
                lector = csv.reader(archivo)
                # Saltar la primera línea que contiene los encabezados
                next(lector)
                masculinos = 0
                femeninos = 0
                for fila in lector:
                    # Si la columna de género es "Hombre", incrementar el contador de hombres.
                    if fila[4] == "Masculino":
                        masculinos += 1
                    # Si la columna de género es "Mujer", incrementar el contador de mujeres.
                    elif fila[4] == "Femenino":
                        femeninos += 1

            # Crear listas con los datos para el gráfico
            categorias = ["Masculinos", "Femeninos"]
            num_estudiantes = [masculinos, femeninos]

            # Crear una figura y un gráfico de pastel
            figura, ax = plt.subplots()
            ax.pie(num_estudiantes, labels=categorias, autopct="%1.1f%%")

            # Configurar el título del gráfico
            ax.set_title("Conteo de estudiantes por género")

            # Mostrar el gráfico
            plt.show()
            

            
        def Tabular():
            print("Reporte Tabular")
            ventana_reporte_tabular = tk.Toplevel()
            columnas = ["Nombre", "A.Paterno", "A.Materno", "Edad", "Sexo", "No.Control", "CURP"]            
            tree = ttk.Treeview(ventana_reporte_tabular, columns=columnas,
                                show="headings")
            
            tree.heading("Nombre", text= "Nombre Estudiante")
            tree.heading("A.Paterno", text= "Apellido Paterno")
            tree.heading("A.Materno", text= "Apellido Materno")
            tree.heading("Edad", text= "Edad")
            tree.heading("Sexo", text= "Sexo")
            tree.heading("No.Control", text= "No. de Control")
            tree.heading("CURP", text= "CURP")
            
            with open("estudiantes.csv", "r") as file:
                lector = csv.reader(file)
                contactos = list(lector)
                for contacto in contactos:
                    tree.insert("",tk.END,values=contacto)
            tree.pack()
                
            ventana_reporte_tabular.mainloop()
            
            
        def Jerarquica():
            print("Reporte Jerarquica")

            # Creación de la ventana del Reporte Jerarquico
            ventana_reporte_jerarquico = tk.Toplevel()
            ventana_reporte_jerarquico.title("Reporte de Estudiantes") 
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
                            
                    ventana_reporte_jerarquico.config(bg='#008080')
                    ventana_reporte_jerarquico.geometry("400x300")
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
    root.title("Gestor de Tareas")
    root.geometry("500x500")
    root.configure(bg='#ff8000')
    
    # Crear una etiqueta 
    text_label = tk.Label(root, text="Gestor de Treas ", font=("Arial", 20), bg='#ff8000')
    text_label.pack(pady=20)
    
    # Cargar la imagen
    image = Image.open("C:\\Users\\edgar\\OneDrive\\Imágenes\\Administrador-de-tareas-gratis-header.png")

    # Cambiar el tamaño de la imagen
    new_size = (500, 500)  # Especifica el nuevo tamaño deseado
    resized_image = image.resize(new_size)

    # Convertir la imagen redimensionada en PhotoImage
    photo = ImageTk.PhotoImage(resized_image)

    # Crear el widget de la imagen y mostrarlo
    imagen_widget = tk.Label(root, image=photo)
    imagen_widget.pack()
    
    #Menu
    menu_bar = tk.Menu(root)
    menu = tk.Menu(root,tearoff=0)
    menu_bar.add_cascade(label="Opciones", menu=menu)
    menu.add_command(label="Crear tarea",command=Crear_Contacto)
    menu.add_command(label="Editar tarea", command=Editar_Contacto)
    menu.add_command(label="Eliminar tarea", command=Eliminar_Contacto)
    menu.add_command(label="Listar pendientes", command=Listar_Contacto)
    menu.add_command(label="Reporte", command=Reporte)
    menu.add_command(label="Salir", command=Salir)
    root.config(menu=menu_bar)
    root.mainloop()

if __name__ == "__main__":
    main()