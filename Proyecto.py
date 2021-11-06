from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
import sys

class Manejodeficheros:
    def __init__(self):
        self.ventanaprincipal=tk.Tk()
        self.opciones()
        self.scrolledtext=st.ScrolledText(self.ventanaprincipal, width=90, height=30)
        self.scrolledtext.grid(column=0,row=0, padx=15, pady=15)   
        self.ventanaprincipal.title("Proyecto final algoritmos")   
        self.ventanaprincipal.mainloop()

    def opciones(self):
        self.labelframe1=ttk.LabelFrame(self.ventanaprincipal, text="opciones")
        self.labelframe1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        self.boton1=ttk.Button(self.labelframe1, text="Guardar", command=self.guardarfichero)
        self.boton1.grid(column=2, row=4, padx=10, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Abrir", command=self.abrirfichero)
        self.boton1.grid(column=1, row=4, padx=10, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Salir", command=self.salir)
        self.boton1.grid(column=3, row=4, padx=10, pady=10)

    def salir(self):
        sys.exit()

    def guardarfichero(self):
        archivo=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if archivo!='':
            doc1=open(archivo, "w", encoding="utf-8")
            doc1.write(self.scrolledtext.get("1.0", tk.END))
            doc1.close()
            mb.showinfo("Confirmacion", "se han guardado los datos sin problamas.")

    def abrirfichero(self):
        archivo=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if archivo!='':
            doc1=open(archivo, "r", encoding="utf-8")
            texto=doc1.read()
            doc1.close()
            self.scrolledtext.delete("1.0", tk.END) 
            self.scrolledtext.insert("1.0", texto)
    

proyecto= Manejodeficheros() 

