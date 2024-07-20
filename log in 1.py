import tkinter as tk
from PIL import Image, ImageTk
 
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Sistema de Control PTC Tarimas")

 
ruta_imagen = "images/logo.png"  
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((400, 100), Image.LANCZOS)  
imagen_tk = ImageTk.PhotoImage(imagen)

 
header = tk.Label(ventana, image=imagen_tk)
header.pack(side="top", fill=tk.BOTH, expand=True)

 
etiqueta = tk.Label(ventana, text="BIENVENIDO AL SISTEMA DE CONTROL PTC TARIMAS", bg="white")
etiqueta.pack(fill=tk.BOTH, expand=True)

 
header.image = imagen_tk

 
ventana.mainloop()
