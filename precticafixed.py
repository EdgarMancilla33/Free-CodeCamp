import tkinter as tk
import csv
import matplotlib.pyplot as plt
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
                    contenido = csv.reader(file)
                    contenido = list(contenido)
                    for linea in contenido:
                        if registro in contenido:
                            contenido.pop(contador)
                            contenido.insert(contador, registro_nuevo)
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

            no_control = contacto_seleccionado[3]
            messagebox.showinfo(
                title="Items seleccionados", message=contacto_seleccionado
            )

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
            if bandera == True:
                Ventana_Editar_Estudiante = tk.Toplevel()
                etiqueta_nombre = tk.Label(
                    Ventana_Editar_Estudiante, text="Nombre Contacto:"
                )
                etiqueta_nombre.pack()
                campo_nombre = tk.Entry(Ventana_Editar_Estudiante)
                campo_nombre.insert(0, registro[0])
                campo_nombre.pack()

                etiqueta_apellidoP = tk.Label(
                    Ventana_Editar_Estudiante, text="Apellido Paterno:"
                )
                etiqueta_apellidoP.pack()
                campo_apellidoP = tk.Entry(Ventana_Editar_Estudiante)
                campo_apellidoP.insert(0, registro[1])
                campo_apellidoP.pack()

                etiqueta_apellidoM = tk.Label(
                    Ventana_Editar_Estudiante, text="Apellido Materno:"
                )
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

                etiqueta_noControl = tk.Label(
                    Ventana_Editar_Estudiante, text="Número de Control:"
                )
                etiqueta_noControl.pack()
                campo_noControl = tk.Entry(Ventana_Editar_Estudiante)
                campo_noControl.insert(0, registro[5])
                campo_noControl.pack()

                etiqueta_CURP = tk.Label(Ventana_Editar_Estudiante, text="CURP:")
                etiqueta_CURP.pack()
                campo_CURP = tk.Entry(Ventana_Editar_Estudiante)
                campo_CURP.insert(0, registro[6])
                campo_CURP.pack()

                boton_actualizar = tk.Button(
                    Ventana_Editar_Estudiante,
                    text="Actualizar",
                    command=actualizar_estudiante,
                )
                boton_actualizar.pack()

                Ventana_Editar_Estudiante.mainloop()

        Ventana_Editar = tk.Toplevel()
        lista_estudiantes = tk.Listbox(Ventana_Editar)
        lista_estudiantes.pack()

        with open("estudiantes.csv", "r") as file:
            contenido = csv.reader(file)
            for linea in contenido:
                lista_estudiantes.insert(tk.END, linea)

        boton_seleccionar = tk.Button(
            Ventana_Editar, text="Seleccionar", command=seleccionar_estudiante
        )
        boton_seleccionar.pack()

        Ventana_Editar.mainloop()

    ventana_principal = tk.Tk()

    boton_editar = tk.Button(
        ventana_principal, text="Editar Estudiante", command=Editar_Contacto
    )
    boton_editar.pack()

    ventana_principal.mainloop()


if __name__ == "__main__":
    main()