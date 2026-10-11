import tkinter as tk
from tkinter import messagebox
import re

Ventana = tk.Tk()
Ventana.geometry("350x500")
Ventana.config(bg="pink")
Ventana.title("Actividad 05 - Formulario de registro Vr.002")

#Definición de pseudo delegados (no se implementan en tiempo real)

def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

# Definición de funciones
def LimpiarFormulario():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    varGenero.set(0)

def BorrarFun():
    LimpiarFormulario()

def GuardarRegistro():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""
    if varGenero.get() == 1:
        genero = "Hombre"
    elif varGenero.get() == 2:
        genero = "Mujer"
    elif varGenero.get() == 3:
        genero = "Otro"
    
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos)):
        # Generar la cadena de caracteres para la impresión en archivo
        datos = "Nombres: " + nombres + "\n" + "Apellidos: " + apellidos + "\n" + "Edad: " + edad + "\n" + "Estatura: " + estatura + "\n" + "Telefono: " + telefono + "\n" + "Genero: " + genero + "\n"
    
        # Guardar registros
        with open("registro.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
        
        # Mostrar mensaje de confirmación
        messagebox.showinfo("Información", "Datos guardados con éxito: \n\n" + datos)
        LimpiarFormulario();
    else:
        # Mostrar mensaje de error si no se cumplen las validaciones
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")

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