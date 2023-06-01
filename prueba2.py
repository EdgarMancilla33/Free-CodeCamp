import tkinter as tk


def main():
    def crear_contacto():
        def guardar()
        nombre= campo_nombre.get()
        apellidoP = campo_apellidoP.get()
        apellidoM = campo_apellidoM.get()
        noControl = 
        ventana_crear = tk.Toplevel()
        #agregar el contenido
        # para creaer el contacto)
        etiqueta_nombre = tk.Label(ventana_crear, text="nombre contacto ")
        etiqueta_nombre.pack()
        campo_nombre = tk.Entry(ventana_crear)
        campo_nombre.pack()
        
        
        etiqueta_appellidoP = tk.Label(v)
        
        boton_guardar = tk.Button(ventana_crear, text="guardar",command=guardar)
        boton_guardar.pack()
        ventana_crear.mainloop()
        
    def Editar_Contacto():
        ventana_editar = tk.Toplevel()
        lista_estudiantes = tk.Listbox(ventana_editar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        boton_seleccionar = tk.Button(ventana_editar,text="seleccionar ocntactos ")
        
    
    print("funcion principal")
    root = tk.Tk()
    root.title("agenda de contacto")
    root.geometry("500x500")
    
    #menu
    menu_bar = tk.Menu(root)
    menu = tk.Menu(root,tearoff=0)
    menu_bar.add_cascade(label="opciones", menu=menu)
    menu.add_command(label="crear contacto",command = crear_contacto)
    menu.add_command(label="editar contacto ")
    menu.add_command(label="listar contacto ")
    menu.add_command(label="salir")
    root.config(menu=menu_bar)
    root.mainloop()
    
    
    

    
if __name__ == "__main__":
    main()