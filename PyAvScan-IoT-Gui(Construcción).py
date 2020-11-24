# -*- coding: utf-8 -*-
import time 
from tkinter import *
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
from tkinter import ttk

root    = Tk()
playimg = PhotoImage(file="img/play.png")

def ventana_escaneo2(archivo):  
    root1 = Tk() 
    root1.geometry("500x300")
    root1.configure(bg='white')
    root1.title("PyAvScann-IoT - Analisis en Busca de Amenazas")
    titulo1  = Label(root1, text="PyAvScann-IoT",  bg='white')
    titulo1.pack(side=TOP,padx=10,pady=10)
    archivo = "Escaneando:",archivo
    lbl1 = Label(root1, text=archivo,bg='white')
    lbl1.pack(side=TOP,padx=10,pady=10)
    progress = ttk.Progressbar(root1, orient = HORIZONTAL, 
                 length = 300, mode = 'determinate')
    progress.pack(pady = 10)
    progress['value'] = 20
    btnplay = Button(root1, text = 'Play',fg="black", activebackground = "white").place(x=100, y=130) 
    btnpause = Button(root1, text = 'Pause',fg="black", activebackground = "white").place(x=160, y=130)
    btnpause = Button(root1, text = 'Stop',fg="black", activebackground = "white").place(x=230, y=130) 
    root.update_idletasks() 
    time.sleep(1) 
    mainloop()

def ventana_escaneo(archivo):
    root2 = Tk() 
    root2.geometry("500x400")
    root2.configure(bg='white')
    root2.title("PyAvScann-IoT - Analisis en Busca de Amenazas")
    f1 = Frame(bg="white",height=499,width=399)
    f1.pack()
    titulo  = Label(f1, text="PyAvScann-IoT",  bg='white')
    titulo.pack(side=TOP,padx=10,pady=10)
    #logoimg = PhotoImage(file="img/Logo2.png")
    #lbl0 = Label(f1, image = logoimg, bg='white')
    #lbl0.pack(side=TOP,padx=10,pady=10)
    lbl1 = Label(f1, text="Seleccione la acción deseada:",bg='white')
    lbl1.pack(side=TOP,padx=10,pady=10)
    btn1 = Button(f1, text="Escaneo Completo", fg="black", activebackground = "white", command=responder)   
    btn1.pack(padx=10,pady=10) 
    btn2 = Button(f1, text="Escaneo Rapido", fg="black", activebackground = "white", command=buscarArchivo)  
    btn2.pack(padx=10,pady=10)  
    btn3 = Button(f1, text="Salir", fg="black", activebackground = "white", command=salir)  
    btn3.pack(padx=10,pady=10)
    progress = ttk.Progressbar(root2, orient = HORIZONTAL, 
                 length = 300, mode = 'determinate')
    progress.pack(pady = 10)
    progress['value'] = 20
    root2.update_idletasks() 
    root2.mainloop() 

def salir():
    root.destroy()

def buscarArchivo():
    name = fd.askopenfilename()
    ventana_escaneo(name) 

def responder():
    if mb.askyesno('PyAvScann-IoT', '¿Desea ejecutar el escaneo completo?'):
        mb.showwarning('Si', 'Esto tardará vaios minutos')	
    else:
        mb.showinfo('No', 'Regresar')

def main():
    
    root.geometry("500x400")
    root.configure(bg='white')
    root.title("PyAvScann-IoT - Analisis en Busca de Amenazas")
    f = Frame(bg="white",height=499,width=399)
    f.pack()
    titulo  = Label(f, text="PyAvScann-IoT",  bg='white')
    titulo.pack(side=TOP,padx=10,pady=10)
    logoimg = PhotoImage(file="img/Logo2.png")
    lbl0 = Label(f, image = logoimg, bg='white')
    lbl0.pack(side=TOP,padx=10,pady=10)
    lbl1 = Label(f, text="Seleccione la acción deseada:",bg='white')
    lbl1.pack(side=TOP,padx=10,pady=10)
    btn1 = Button(f, text="Escaneo Completo", fg="black", activebackground = "white", command=responder)   
    btn1.pack(padx=10,pady=10) 
    btn2 = Button(f, text="Escaneo Rapido", fg="black", activebackground = "white", command=buscarArchivo)  
    btn2.pack(padx=10,pady=10)  
    btn3 = Button(f, text="Salir", fg="black", activebackground = "white", command=salir)  
    btn3.pack(padx=10,pady=10)
    progress = ttk.Progressbar(root, orient = HORIZONTAL, 
                 length = 300, mode = 'determinate')
    progress.pack(pady = 10)
    progress['value'] = 20
    root.update_idletasks() 
    root.mainloop()

main()


 

