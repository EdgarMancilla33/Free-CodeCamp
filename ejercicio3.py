import csv
import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = campo_tarea.get()
    fecha_entrega = campo_fecha_entrega.get()
    descripcion = campo_descripcion.get()
    estado = campo_estado.get()

    nueva_tarea = [tarea, fecha_entrega, descripcion, estado]

    with open("tarea.csv", "a", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerow(nueva_tarea)

    messagebox.showinfo("Tarea agregada", "La tarea se agregó correctamente.")
    limpiar_campos()

def limpiar_campos():
    campo_tarea.delete(0, tk.END)
    campo_fecha_entrega.delete(0, tk.END)
    campo_descripcion.delete(0, tk.END)
    campo_estado.delete(0, tk.END)

def editar_tarea():
    tarea_seleccionada = lista_tareas.get(lista_tareas.curselection())
    tarea_seleccionada = tarea_seleccionada.split(',')

    tarea = tarea_seleccionada[0]
    fecha_entrega = tarea_seleccionada[1]
    descripcion = tarea_seleccionada[2]
    estado = tarea_seleccionada[3]

    campo_tarea.delete(0, tk.END)
    campo_tarea.insert(tk.END, tarea)
    campo_fecha_entrega.delete(0, tk.END)
    campo_fecha_entrega.insert(tk.END, fecha_entrega)
    campo_descripcion.delete(0, tk.END)
    campo_descripcion.insert(tk.END, descripcion)
    campo_estado.delete(0, tk.END)
    campo_estado.insert(tk.END, estado)

    messagebox.showinfo("Tarea seleccionada", "La tarea seleccionada se cargó en los campos de edición.")

def guardar_cambios():
    tarea_actualizada = campo_tarea.get()
    fecha_entrega_actualizada = campo_fecha_entrega.get()
    descripcion_actualizada = campo_descripcion.get()
    estado_actualizado = campo_estado.get()

    tarea_seleccionada = lista_tareas.get(lista_tareas.curselection())
    tarea_seleccionada = tarea_seleccionada.split(',')

    tarea = tarea_seleccionada[0]
    fecha_entrega = tarea_seleccionada[1]
    descripcion = tarea_seleccionada[2]
    estado = tarea_seleccionada[3]

    tareas = []

    with open("tarea.csv", "r", newline="") as file:
        lector = csv.reader(file)
        for row in lector:
            if row == tarea_seleccionada:
                tareas.append([tarea_actualizada, fecha_entrega_actualizada, descripcion_actualizada, estado_actualizado])
            else:
                tareas.append(row)

    with open("tarea.csv", "w", newline="") as file:
        escritor = csv.writer(file)
        escritor.writerows(tareas)

    messagebox.showinfo("Cambios guardados", "Los cambios se guardaron correctamente.")
    limpiar_campos()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Tareas")

# Crear los campos de entrada
etiqueta_tarea = tk.Label(ventana, text="Tarea:")
etiqueta_tarea.pack()
campo_tarea = tk.Entry(ventana)
campo_tarea.pack()

etiqueta_fecha_entrega = tk.Label(ventana, text="Fecha de Entrega:")
etiqueta_fecha_entrega.pack()
campo_fecha_entrega = tk.Entry(ventana)
campo_fecha_entrega.pack()

etiqueta_descripcion = tk.Label(ventana, text="Descripción:")
etiqueta_descripcion.pack()
campo_descripcion = tk.Entry(ventana)
campo_descripcion.pack()

etiqueta_estado = tk.Label(ventana, text="Estado:")
etiqueta_estado.pack()
campo_estado = tk.Entry(ventana)
campo_estado.pack()

# Crear el botón de agregar tarea
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

# Crear la lista de tareas
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

# Crear el botón de editar tarea
boton_editar = tk.Button(ventana, text="Editar Tarea", command=editar_tarea)
boton_editar.pack()

# Crear el botón de guardar cambios
boton_guardar = tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios)
boton_guardar.pack()

# Cargar las tareas existentes en la lista
with open("tarea.csv", "r") as file:
    lector = csv.reader(file)
    for row in lector:
        tarea = row[0]
        fecha_entrega = row[1]
        descripcion = row[2]
        estado = row[3]
        lista_tareas.insert(tk.END, f"{tarea}, {fecha_entrega}, {descripcion}, {estado}")

ventana.mainloop()