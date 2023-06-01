import tkinter as tk
import csv

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = entrada_tarea.get()
    fecha_entrega = entrada_fecha_entrega.get()
    descripcion = entrada_descripcion.get()
    estado = var_estado.get()
    if tarea and fecha_entrega and descripcion and estado:
        nueva_tarea = {'Tarea': tarea, 'Fecha de Entrega': fecha_entrega, 'Descripción': descripcion, 'Estado': estado}
        lista_tareas.append(nueva_tarea)
        actualizar_lista_tareas()
        entrada_tarea.delete(0, tk.END)
        entrada_fecha_entrega.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
        guardar_tareas()

# Función para actualizar la lista de tareas en la interfaz gráfica
def actualizar_lista_tareas():
    lista_tareas_widget.delete(0, tk.END)
    for tarea in lista_tareas:
        lista_tareas_widget.insert(tk.END, tarea['Tarea'])

# Función para seleccionar una tarea de la lista
def seleccionar_tarea(event):
    indice = lista_tareas_widget.curselection()[0]
    tarea_seleccionada = lista_tareas[indice]
    entrada_tarea.delete(0, tk.END)
    entrada_tarea.insert(tk.END, tarea_seleccionada['Tarea'])
    entrada_fecha_entrega.delete(0, tk.END)
    entrada_fecha_entrega.insert(tk.END, tarea_seleccionada['Fecha de Entrega'])
    entrada_descripcion.delete(0, tk.END)
    entrada_descripcion.insert(tk.END, tarea_seleccionada['Descripción'])
    var_estado.set(tarea_seleccionada['Estado'])

# Función para actualizar una tarea existente
def actualizar_tarea():
    tarea_actualizada = entrada_tarea.get()
    fecha_entrega_actualizada = entrada_fecha_entrega.get()
    descripcion_actualizada = entrada_descripcion.get()
    estado_actualizado = var_estado.get()
    if tarea_actualizada and fecha_entrega_actualizada and descripcion_actualizada and estado_actualizado:
        indice = lista_tareas_widget.curselection()[0]
        lista_tareas[indice]['Tarea'] = tarea_actualizada
        lista_tareas[indice]['Fecha de Entrega'] = fecha_entrega_actualizada
        lista_tareas[indice]['Descripción'] = descripcion_actualizada
        lista_tareas[indice]['Estado'] = estado_actualizado
        actualizar_lista_tareas()
        entrada_tarea.delete(0, tk.END)
        entrada_fecha_entrega.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
        guardar_tareas()

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    indice = lista_tareas_widget.curselection()[0]
    lista_tareas.pop(indice)
    actualizar_lista_tareas()
    entrada_tarea.delete(0, tk.END)
    entrada_fecha_entrega.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)
    guardar_tareas()

# Función para guardar las tareas en un archivo CSV
def guardar_tareas():
    with open('tareas.csv', 'w', newline='') as archivo_csv:
        nombres_columnas = ['Tarea', 'Fecha de Entrega', 'Descripción', 'Estado']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)
        escritor_csv.writeheader()
        for tarea in lista_tareas:
            escritor_csv.writerow(tarea)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Gestión de Tareas')

# Crear el marco principal
marco_principal = tk.Frame(ventana)
marco_principal.pack(padx=20, pady=20)

# Crear la lista de tareas
lista_tareas_widget = tk.Listbox(marco_principal, width=50)
lista_tareas_widget.pack(side=tk.LEFT, fill=tk.Y)

# Crear el scrollbar para la lista de tareas
scrollbar = tk.Scrollbar(marco_principal)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Asociar el scrollbar con la lista de tareas
lista_tareas_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas_widget.yview)

# Crear el campo de entrada para la tarea
etiqueta_tarea = tk.Label(ventana, text='Tarea:')
etiqueta_tarea.pack()
entrada_tarea = tk.Entry(ventana, width=50)
entrada_tarea.pack(pady=5)

# Crear el campo de entrada para la fecha de entrega
etiqueta_fecha_entrega = tk.Label(ventana, text='Fecha de Entrega:')
etiqueta_fecha_entrega.pack()
entrada_fecha_entrega = tk.Entry(ventana, width=50)
entrada_fecha_entrega.pack(pady=5)

# Crear el campo de entrada para la descripción
etiqueta_descripcion = tk.Label(ventana, text='Descripción:')
etiqueta_descripcion.pack()
entrada_descripcion = tk.Entry(ventana, width=50)
entrada_descripcion.pack(pady=5)

# Crear el campo de selección para el estado de la tarea
etiqueta_estado = tk.Label(ventana, text='Estado:')
etiqueta_estado.pack()
var_estado = tk.StringVar(ventana)
opciones_estado = ['Terminada', 'Pendiente']
opciones_estado_menu = tk.OptionMenu(ventana, var_estado, *opciones_estado)
opciones_estado_menu.pack(pady=5)

# Crear los botones
boton_agregar = tk.Button(ventana, text='Agregar Tarea', command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT, padx=5)
boton_actualizar = tk.Button(ventana, text='Actualizar Tarea', command=actualizar_tarea)
boton_actualizar.pack(side=tk.LEFT, padx=5)
boton_eliminar = tk.Button(ventana, text='Eliminar Tarea', command=eliminar_tarea)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Asociar la función de selección de tarea con el evento de selección en la lista
lista_tareas_widget.bind('<<ListboxSelect>>', seleccionar_tarea)

# Cargar las tareas desde el archivo CSV
try:
    with open('tareas.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        lista_tareas = [row for row in lector_csv]
        actualizar_lista_tareas()
except FileNotFoundError:
    lista_tareas = []

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
