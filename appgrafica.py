import tkinter

ventana= tkinter.Tk()
ventana.geometry("400x300")

etiqueta=tkinter.Label(ventana, text=" BIENVENIDO AL SISTEMA DE CONTEROL PTC TARIMAS", bg="white")
etiqueta.pack (fill=tkinter.BOTH,expand=True)

ventana.mainloop ()
