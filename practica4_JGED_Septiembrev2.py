import tkinter as tk
from tkinter import messagebox

Ventana = tk.Tk()
Ventana.geometry("350x500")
Ventana.config(bg="pink")
Ventana.title("Actividad 04 - Formulario de registro Vr.001")


# Definición de funciones
def LimpiarFormulario():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    varGenero.set(0)
    messagebox.showinfo("Información", "Los campos se han limpiado correctamente.")


def GuardarRegistro():
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    estatura = tbEstatura.get().strip()
    telefono = tbTelefono.get().strip()
    genero = ""

    if varGenero.get() == 1:
        genero = "Hombre"
    elif varGenero.get() == 2:
        genero = "Mujer"
    elif varGenero.get() == 3:
        genero = "Otro"

    datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nEstatura: {estatura}\nTelefono: {telefono}\nGenero: {genero}\n"

    try:
        with open("registro.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n")

        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)
        LimpiarFormulario()

    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error al guardar el archivo: {ex}")


varGenero = tk.IntVar()

lbNombre = tk.Label(Ventana, text="Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry(Ventana)
tbNombre.pack()

lbApellidos = tk.Label(Ventana, text="Apellido: ")
lbApellidos.pack()
tbApellidos = tk.Entry(Ventana)
tbApellidos.pack()

lbTelefono = tk.Label(Ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(Ventana)
tbTelefono.pack()

lbEdad = tk.Label(Ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(Ventana)
tbEdad.pack()

lbEstatura = tk.Label(Ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(Ventana)
tbEstatura.pack()

groupBox = tk.LabelFrame(Ventana, text="Género:", padx=12, pady=12)
groupBox.pack()

rbMasculino = tk.Radiobutton(groupBox, text="Masculino", variable=varGenero, value=1)
rbMasculino.grid(row=0, column=0)

rbFemenino = tk.Radiobutton(groupBox, text="Femenino", variable=varGenero, value=2)
rbFemenino.grid(row=0, column=1)

rbOtro = tk.Radiobutton(groupBox, text="Otro", variable=varGenero, value=3)
rbOtro.grid(row=0, column=2)

btnGuardar = tk.Button(Ventana, text="Guardar", command=GuardarRegistro)
btnGuardar.pack()

btnLimpiar = tk.Button(Ventana, text="Limpiar", command=LimpiarFormulario)
btnLimpiar.pack()

Ventana.mainloop()