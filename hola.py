import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import subprocess
from tkinter import filedialog
from Crypto.Cipher import CAST
import os
import shutil


class Aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("AleOsama -- Ccrypt")
        
        self.miframe1=tk.Frame(self.ventana1)
        self.miframe1.grid(row=0,column=0,padx=10,pady=10)
        
        
        #--------------------menu bar---------------------------------
        
        menubar=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar)
        opciones1=tk.Menu(menubar)
        
        
        opciones1.add_command(label="Abrir Archivo",command=self.abrirArchivo)
        opciones1.add_command(label="salir",command=self.salir)
        menubar.add_cascade(label="inicio",menu=opciones1)
    
        #---------------------label entry---------------------------
        
        self.labelArchivo = tk.Label(self.miframe1,text="Archivo")
        self.labelArchivo.grid(row=0,column=0,padx=5,pady=5,sticky=tk.E)
        self.entryArchivo = tk.Entry(self.miframe1)
        self.entryArchivo.grid(row=0,column=1,padx=5,pady=5) 
        
        self.labelClave=tk.Label(self.miframe1,text="clave")
        self.labelClave.grid(row=1,column=0,padx=5,pady=5)
        self.entryClave =tk.Entry(self.miframe1,show="*")    
        self.entryClave.grid(row=1,column=1,padx=5,pady=5)
           
        
       #------------------------botones------------------------------- 
        self.boton1=tk.Button(self.miframe1,text="encriptar",command=self.encriptar)
        self.boton1.grid(row=2,column=0,padx=5,pady=5)
        self.boton2=tk.Button(self.miframe1,text="desencriptar",command=self.desencriptar)
        self.boton2.grid(row=2,column=1,padx=5,pady=5)
        
        self.ventana1.grid_columnconfigure(0,weight=1)
        self.ventana1.grid_rowconfigure(0,weight=2)
                
        
        self.ventana1.mainloop()
    
    
    
    def abrirArchivo(self):
        nombreArchivo=filedialog.askopenfilename(title="abrir")
        self.entryArchivo.delete(0,tk.END)
        self.entryArchivo.insert(0,nombreArchivo)
        
    
    
    def encriptar(self):
        archivo = self.entryArchivo.get()
        clave = self.entryClave.get()

        if not clave:
            messagebox.showerror("Error", "Por favor, ingresa una clave.")
            return

        clave_bytes = clave.encode('utf-8')
        clave_ajustada = clave_bytes[:16]  # Utilizar los primeros 16 bytes como clave

        with open(archivo, 'rb') as file:
            contenido = file.read()

        cifrador = CAST.new(clave_ajustada, CAST.MODE_ECB)  # Utilizar el modo ECB

        contenido_encriptado = cifrador.encrypt(contenido)

        archivo_encriptado = archivo + ".encrypted"
        with open(archivo_encriptado, 'wb') as file:
            file.write(contenido_encriptado)
            
        
        carpeta_destino= os.path.join(os.getcwd(),("baulera"))
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        
        archivo_destino= os.path.join(carpeta_destino, os.path.basename(archivo_encriptado))
        shutil.copy(archivo_encriptado,archivo_destino)    
            

        messagebox.showinfo("Encriptado", "El archivo se ha encriptado correctamente.")
        
        

    def desencriptar(self):
        archivo = self.entryArchivo.get()
        clave = self.entryClave.get()

        if not clave:
            messagebox.showerror("Error", "Por favor, ingresa una clave.")
            return

        clave_bytes = clave.encode('utf-8')
        clave_ajustada = clave_bytes[:16]  # Utilizar los primeros 16 bytes como clave

        with open(archivo, 'rb') as file:
            contenido_encriptado = file.read()

        cifrador = CAST.new(clave_ajustada, CAST.MODE_ECB)  # Utilizar el modo ECB

        contenido_desencriptado = cifrador.decrypt(contenido_encriptado)

        archivo_desencriptado = archivo + ".decrypted"
        with open(archivo_desencriptado, 'wb') as file:
            file.write(contenido_desencriptado)

        messagebox.showinfo("Desencriptado", "El archivo se ha desencriptado correctamente.")
        
    def salir(self):
        self.ventana1.destroy()
        

Aplicacion1=Aplicacion()


