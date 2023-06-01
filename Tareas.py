import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk
import csv
from PIL import Image, ImageTk

def main():
    def Editar_Tarea():
        def seleccionar_tarea():
            def actualizar_tarea():
                print("Click en el botón para actualizar la tarea")
                titulo_nuevo = tarea_seleccionada[0]
                descripcion_nueva = tarea_seleccionada[1]
                estado_nuevo = tarea_seleccionada[2]
                tarea_nueva = [titulo_nuevo, descripcion_nueva, estado_nuevo]
                tareas[contador] = tarea_nueva
                with open("tareas.csv", "w", newline="") as file:
                    escritor = csv.writer(file)
                    escritor.writerows(tareas)
                print("Tarea actualizada")
                Ventana_Editar_Tarea.destroy()

            print("Click en la tarea que desea seleccionar")
            indices = lista_tareas.curselection()
            for i in indices:
                tarea_seleccionada = list(tareas[i])

            contador = indices[0]
            tarea = tareas[contador]

            Ventana_Editar.destroy()

            Ventana_Editar_Tarea = tk.Toplevel()
            Ventana_Editar_Tarea.config(bg='#008080')
            Ventana_Editar_Tarea.geometry("400x300")

            etiqueta_titulo = tk.Label(Ventana_Editar_Tarea, text="Título de la tarea:")
            etiqueta_titulo.pack()
            campo_titulo = tk.Entry(Ventana_Editar_Tarea)
            campo_titulo.insert(0, tarea[0])
            campo_titulo.pack()

            etiqueta_descripcion = tk.Label(Ventana_Editar_Tarea, text="Descripción de la tarea:")
            etiqueta_descripcion.pack()
            campo_descripcion = tk.Entry(Ventana_Editar_Tarea)
            campo_descripcion.insert(0, tarea[1])
            campo_descripcion.pack()

            etiqueta_estado = tk.Label(Ventana_Editar_Tarea, text="Estado de la tarea:")
            etiqueta_estado.pack()
            campo_estado = tk.Entry(Ventana_Editar_Tarea)
            campo_estado.insert(0, tarea[2])
            campo_estado.pack()

            boton_actualizar = tk.Button(Ventana_Editar_Tarea, text="Actualizar Tarea", command=actualizar_tarea, bg='#800080', fg="white", font=("Arial", 12), width=15)
            boton_actualizar.pack()

            Ventana_Editar_Tarea.mainloop()

        Ventana_Editar = tk.Toplevel()
        Ventana_Editar.config(bg='#008080')
        Ventana_Editar.geometry("400x300")

        lista_tareas = tk.Listbox(Ventana_Editar)
        lista_tareas.config(width=60)
        lista_tareas.pack()

        with open("tareas.csv", "r", newline="") as file:
            lector = csv.reader(file)
            tareas = list(lector)

        for tarea in tareas:
            lista_tareas.insert(tk.END, tarea[0])

        boton_seleccionar = tk.Button(Ventana_Editar, text="Seleccionar Tarea", command=seleccionar_tarea, bg='#008080', fg="white", font=("Arial", 12), width=20)
        boton_seleccionar.pack()

        Ventana_Editar.mainloop()

    def Crear_Tarea():
        def guardar():
            titulo = campo_titulo.get()
            descripcion = campo_descripcion.get()
            estado = campo_estado.get()
            tarea = [titulo, descripcion, estado]
            with open("tareas.csv", "a", newline="") as file:
                escritor = csv.writer(file)
                escritor.writerow(tarea)
            messagebox.showinfo("Tarea creada", "La tarea se ha creado exitosamente")
            Ventana_Crear_Tarea.destroy()

        Ventana_Crear_Tarea = tk.Toplevel()
        Ventana_Crear_Tarea.config(bg='#008080')
        Ventana_Crear_Tarea.geometry("400x300")

        etiqueta_titulo = tk.Label(Ventana_Crear_Tarea, text="Título de la tarea:")
        etiqueta_titulo.pack()
        campo_titulo = tk.Entry(Ventana_Crear_Tarea)
        campo_titulo.pack()

        etiqueta_descripcion = tk.Label(Ventana_Crear_Tarea, text="Descripción de la tarea:")
        etiqueta_descripcion.pack()
        campo_descripcion = tk.Entry(Ventana_Crear_Tarea)
        campo_descripcion.pack()

        etiqueta_estado = tk.Label(Ventana_Crear_Tarea, text="Estado de la tarea:")
        etiqueta_estado.pack()
        campo_estado = tk.Entry(Ventana_Crear_Tarea)
        campo_estado.pack()

        boton_guardar = tk.Button(Ventana_Crear_Tarea, text="Guardar Tarea", command=guardar, bg='#800080', fg="white", font=("Arial", 12), width=15)
        boton_guardar.pack()

        Ventana_Crear_Tarea.mainloop()

    def Leer_Tareas():
        Ventana_Leer_Tareas = tk.Toplevel()
        Ventana_Leer_Tareas.config(bg='#008080')
        Ventana_Leer_Tareas.geometry("400x300")

        lista_tareas = tk.Listbox(Ventana_Leer_Tareas)
        lista_tareas.config(width=60)
        lista_tareas.pack()

        with open("tareas.csv", "r", newline="") as file:
            lector = csv.reader(file)
            tareas = list(lector)

        for tarea in tareas:
            lista_tareas.insert(tk.END, f"Título: {tarea[0]} - Descripción: {tarea[1]} - Estado: {tarea[2]}")

        Ventana_Leer_Tareas.mainloop()

    def Eliminar_Tarea():
        def seleccionar_tarea():
            print("Click en la tarea que desea seleccionar")
            indices = lista_tareas.curselection()
            for i in indices:
                tarea_seleccionada = lista_tareas.get(i)
                print(tarea_seleccionada)

            contador = indices[0]
            tarea = tareas[contador]

            tareas.remove(tarea)

            with open("tareas.csv", "w", newline="") as file:
                escritor = csv.writer(file)
                escritor.writerows(tareas)

            lista_tareas.delete(indices)

            messagebox.showinfo("Tarea eliminada", "La tarea se ha eliminado exitosamente")
            Ventana_Eliminar_Tarea.destroy()

        Ventana_Eliminar_Tarea = tk.Toplevel()
        Ventana_Eliminar_Tarea.config(bg='#008080')
        Ventana_Eliminar_Tarea.geometry("400x300")

        lista_tareas = tk.Listbox(Ventana_Eliminar_Tarea)
        lista_tareas.config(width=60)
        lista_tareas.pack()

        with open("tareas.csv", "r", newline="") as file:
            lector = csv.reader(file)
            tareas = list(lector)

        for tarea in tareas:
            lista_tareas.insert(tk.END, tarea[0])

        boton_seleccionar = tk.Button(Ventana_Eliminar_Tarea, text="Seleccionar Tarea", command=seleccionar_tarea, bg='#008080', fg="white", font=("Arial", 12), width=20)
        boton_seleccionar.pack()

        Ventana_Eliminar_Tarea.mainloop()

    def Generar_Reporte():
        def Generar_Reporte_Grafico():
            # Leer las tareas desde el archivo CSV
            with open("tareas.csv", "r", newline="") as file:
                lector = csv.reader(file)
                tareas = list(lector)
            
            # Contadores de avances
            contador_pendiente = 0
            contador_realizada = 0
            
            # Calcular conteo de avances
            for tarea in tareas:
                estado = tarea[2]
                if estado == "Pendiente":
                    contador_pendiente += 1
                elif estado == "Realizada":
                    contador_realizada += 1
            
            # Etiquetas y tamaños para la gráfica de pastel
            labels = ["Pendiente", "Realizada"]
            sizes = [contador_pendiente, contador_realizada]
            colors = ["orange", "green"]
            explode = (0.1, 0)  # Explode el primer sector (pendiente)
            
            # Generar la gráfica de pastel
            plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')  # Hace que el gráfico sea un círculo en lugar de una elipse
            plt.title("Avance de las tareas")
            plt.show()

        def Generar_Reporte_Jerarquico():
            print("Reporte Jerárquico")

        # Leer las tareas desde el archivo CSV
        with open("tareas.csv", "r", newline="") as file:
            reader = csv.reader(file)
            tareas = list(reader)

        # Creación de la ventana del Reporte Jerárquico
        ventana_reporte_jerarquico = tk.Toplevel()
        ventana_reporte_jerarquico.title("Reporte Jerárquico")

        # Creación del Treeview
        treeview = ttk.Treeview(ventana_reporte_jerarquico)
        treeview.pack()

        # Crear los encabezados de las columnas
        treeview["columns"] = ("Estado")

        # Establecer los nombres de las columnas
        treeview.heading("#0", text="Tarea")
        treeview.heading("Estado", text="Estado")

        # Separar las tareas en las listas correspondientes
        tareas_pendientes = []
        tareas_realizadas = []

        for tarea in tareas:
            if tarea[2] == "Pendiente":
                tareas_pendientes.append(tarea)
            elif tarea[2] == "Realizada":
                tareas_realizadas.append(tarea)

        # Agregar las tareas pendientes al Treeview
        if len(tareas_pendientes) > 0:
            pendientes = treeview.insert("", tk.END, text="Pendientes")
            for tarea in tareas_pendientes:
                treeview.insert(pendientes, tk.END, text=tarea[0], values=(tarea[2]))

        # Agregar las tareas realizadas al Treeview
        if len(tareas_realizadas) > 0:
            realizadas = treeview.insert("", tk.END, text="Realizadas")
            for tarea in tareas_realizadas:
                treeview.insert(realizadas, tk.END, text=tarea[0], values=(tarea[2]))

        ventana_reporte_jerarquico.mainloop()

        Ventana_Reportes = tk.Toplevel()
        Ventana_Reportes.title("Reportes")
        Ventana_Reportes.geometry("200x150")
        Ventana_Reportes.config(bg='#008080')

        boton_reporte_grafico = tk.Button(Ventana_Reportes, text="Reporte gráfico", command=Generar_Reporte_Grafico, bg='#800080', fg="white", font=("Arial", 12), width=15)
        boton_reporte_grafico.pack(pady=10)

        boton_reporte_jerarquico = tk.Button(Ventana_Reportes, text="Reporte jerárquico", command=Generar_Reporte_Jerarquico, bg='#800080', fg="white", font=("Arial", 12), width=15)
        boton_reporte_jerarquico.pack(pady=10)
        
        

    Ventana_Principal = tk.Tk()
    Ventana_Principal.title("Gestión de Tareas")
    Ventana_Principal.geometry("400x500")
    Ventana_Principal.config(bg='#008080')

    frame_superior = tk.Frame(Ventana_Principal, bg='#008080')
    frame_superior.pack(side='top', fill='y', pady=(150, 0))

    boton_crear = tk.Button(frame_superior, text="Crear Tarea", command=Crear_Tarea, bg='#800080', fg="white", font=("Arial", 12), width=15)
    boton_crear.pack(pady=10)

    boton_leer = tk.Button(frame_superior, text="Leer Tareas", command=Leer_Tareas, bg='#800080', fg="white", font=("Arial", 12), width=15)
    boton_leer.pack(pady=10)

    boton_editar = tk.Button(frame_superior, text="Editar Tarea", command=Editar_Tarea, bg='#800080', fg="white", font=("Arial", 12), width=15)
    boton_editar.pack(pady=10)

    boton_eliminar = tk.Button(frame_superior, text="Eliminar Tarea", command=Eliminar_Tarea, bg='#800080', fg="white", font=("Arial", 12), width=15)
    boton_eliminar.pack(pady=10)

    boton_reporte = tk.Button(frame_superior, text="Reporte", command=Generar_Reporte, bg='#800080', fg="white", font=("Arial", 12), width=15)
    boton_reporte.pack(pady=10)

    Ventana_Principal.mainloop()
    
    # Cargar la imagen
    image = Image.open("C:\\Users\\edgar\\OneDrive\\Imágenes\\383px-Oxford-University-Circlet.png")
    photo = ImageTk.PhotoImage(image)
    imagen_widget = tk.Label(root, image=photo)
    imagen_widget.pack()


if __name__ == "__main__":
    main()