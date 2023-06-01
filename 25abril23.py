def Listar_Contacto():
        ventana_listar = tk.Toplevel()
        contacto=[]
        lista_estudiantes = tk.Listbox(ventana_listar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("estudiantes.csv","r",newline="")as file:
            lector = csv.reader(file)
            print(lector)
            contactos = list(lector)
            print(contactos)
            lista_estudiantes.insert(0,*contactos)
        ventana_listar.mainloop()

    
def Eliminar_Contacto():
    
    def Eliminar():
        indice = lista_estudiantes.curselection()
        contacto_seleccionado = list(lista_estudiantes.get(indice))
        no_control = contacto_seleccionado[3]
        ventana_eliminar.destroy()
        nuevo = []
        whith open ( "estudiantes.csv",r ,newline = "") as file: 
            contenido_del archivo = csv.reader(file)
            for linea in contenido_archivo:
                if no_control in linea:
                    print("estudiante encontrado")
                else:
                    nuevo.append(linea)
        whith open ( "estudiantes.csv", w ,newline = "") as file: 
            escritor = csv.writher(file)
            escritor.writerows(nuevo)
            print("archivo modificado")
            messagebox.showinfo(title="contacto eliminado", message=contacto seleccionado) 
        
        ventana eliminar = tk.Toplevel()
        contactos=csv
        lista estudiantes = tk.Listbox(ventana eliminar)
        
    
    
    '''

        def seleccionar_estudiante():
            print("Click en el estudiante que desea seleccionar")
            indices = lista_estudiantes.curselection()
            bandera = False
            for i in indices:
                contacto_seleccionado = list(lista_estudiantes.get(i))
                print(contacto_seleccionado)
                bandera = True
                
                
            
            no_control = contacto_seleccionado[3]
            messagebox.showinfo(title="Items seleccionados",
                # Obtener eñ texto de cada item seleccionado
                # y mostrarlos separados por comas
                message=contacto_seleccionado)
            
            ventana_eliminar.destroy()
            if bandera == True:
                with open("estudiantes.csv","r",newline="") as file:
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
                    print (contador)

        ventana_eliminar = tk.Toplevel()
        lista_estudiantes = tk.Listbox(ventana_eliminar)
        lista_estudiantes.config(width=60)
        lista_estudiantes.pack()
        with open("estudiantes.csv","r",newline="")as file:
            lector = csv.reader(file)
            print(lector)
            contactos = list(lector)
            print(contactos)
            lista_estudiantes.insert(0,*contactos)
        boton_seleccionar = tk.Button(ventana_eliminar, text="Seleccionar contacto", command=seleccionar_estudiante)
        boton_seleccionar.pack()
        ventana_eliminar.mainloop()
        
        '''