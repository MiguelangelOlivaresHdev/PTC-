import tkinter

 
ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Formulario de Datos")
 
etiqueta = tkinter.Label(ventana, text="INGRESE DATOS", bg="white")
etiqueta.pack(side=tkinter.TOP, fill=tkinter.X)

 
marco = tkinter.Frame(ventana)
marco.pack(pady=10, padx=10)


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
 
ventana.mainloop()
