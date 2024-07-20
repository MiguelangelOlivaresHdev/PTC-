import tkinter
from tkinter import messagebox

def calcular_produccion():
    messagebox.showinfo("Opción Seleccionada", "Calcular Producción")

def registrar_lote():
    messagebox.showinfo("Opción Seleccionada", "Registrar Lote")

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Formulario de Datos")

# Crear la etiqueta superior
etiqueta = tkinter.Label(ventana, text="INGRESE DATOS", bg="white")
etiqueta.pack(side=tkinter.TOP, fill=tkinter.X)

# Crear un marco para los campos de entrada
marco = tkinter.Frame(ventana)
marco.pack(pady=10, padx=10)

# Crear las etiquetas y campos de entrada
tkinter.Label(marco, text="Pieza:").grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.E)
pieza_entry = tkinter.Entry(marco)
pieza_entry.grid(row=0, column=1, padx=5, pady=5)

tkinter.Label(marco, text="Dimensiones:").grid(row=1, column=0, padx=5, pady=5, sticky=tkinter.E)
dimensiones_entry = tkinter.Entry(marco)
dimensiones_entry.grid(row=1, column=1, padx=5, pady=5)

tkinter.Label(marco, text="Volumen:").grid(row=2, column=0, padx=5, pady=5, sticky=tkinter.E)
volumen_entry = tkinter.Entry(marco)
volumen_entry.grid(row=2, column=1, padx=5, pady=5)

tkinter.Label(marco, text="Cantidad de Clavos:").grid(row=3, column=0, padx=5, pady=5, sticky=tkinter.E)
clavos_entry = tkinter.Entry(marco)
clavos_entry.grid(row=3, column=1, padx=5, pady=5)

# Crear el menú
menu_bar = tkinter.Menu(ventana)
ventana.config(menu=menu_bar)

# Añadir opciones al menú
archivo_menu = tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opciones", menu=archivo_menu)
archivo_menu.add_command(label="Calcular Producción", command=calcular_produccion)
archivo_menu.add_command(label="Registrar Lote", command=registrar_lote)

# Iniciar el bucle principal
ventana.mainloop()
