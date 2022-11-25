import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
import subprocess
import socket
import os
import threading
class App:
    def __init__(self, root):
        #setting title
        root.title("Escaneo de Vulnerabilidades")
        #setting window size
        width=1200
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        canvas = tk.Canvas(root,xscrollcommand="scrollbar")
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        canvas.configure(yscrollcommand=scrollbar.set,bg="black")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        GLabel_950=tk.Label(root)
        ft = tkFont.Font(family='Times New Roman',size=20)
        GLabel_950["font"] = ft
        GLabel_950["fg"] = "white"
        GLabel_950["bg"] = "black"
        GLabel_950["justify"] = "center"
        GLabel_950["text"] = "Escaneo de Vulnerabilidades"
        GLabel_950.place(x=480,y=20,width=321,height=35)

        self.target = tk.StringVar()
        GLineEdit_132=tk.Entry(root)
        GLineEdit_132["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_132["font"] = ft
        GLineEdit_132["fg"] = "black"
        GLineEdit_132["bg"] = "white"
        GLineEdit_132["justify"] = "center"
        GLineEdit_132["textvariable"] = self.target
        GLineEdit_132.place(x=330,y=80,width=128,height=30)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "white"
        GLabel_981["bg"] = "black"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Introduzca la URL que desea escanear:"
        GLabel_981.place(x=10,y=80,width=346,height=33)

        confileLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        confileLab["font"] = ft
        confileLab["fg"] = "white"
        confileLab["bg"] = "black"
        confileLab["justify"] = "center"
        confileLab["text"] = "Introduzca el archivo de configuracion que desea usar !opcional!:"
        confileLab.place(x=460,y=80,width=346,height=33)

        self.conf = tk.StringVar()
        confEntry = tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        confEntry["font"] = ft
        confEntry["fg"] = "black"
        confEntry["bg"] = "white"
        confEntry["justify"] = "center"
        confEntry["textvariable"] = self.conf
        confEntry.place(x=850,y=80,width=128,height=30)

        self.outputdes=False
        outputDis = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        outputDis["font"] = ft
        outputDis["fg"] = "grey"
        outputDis["bg"] = "black"
        outputDis["justify"] = "center"
        outputDis["text"] = "Desplegar output (por terminal) !opcional!"
        outputDis.place(x=10,y=120,width=346,height=33)
        outputDis["offvalue"] = "0"
        outputDis["onvalue"] = "1"
        outputDis["command"] = self.outputDis_command

        listaLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        listaLab["font"] = ft
        listaLab["fg"] = "white"
        listaLab["bg"] = "black"
        listaLab["justify"] = "center"
        listaLab["text"] = "Selecciona el formato del fichero !opcional!:"
        listaLab.place(x=360,y=120,width=346,height=33)

        vlista = ('csv','html','txt','xml','json','csv','sql','nbe')
        lista = tk.Variable(value=vlista)
        self.formatoEntry = tk.Listbox(root)
        ft = tkFont.Font(family='Times',size=10)
        self.formatoEntry["font"] = ft
        self.formatoEntry["bg"] = "white"
        self.formatoEntry["fg"] = "black"
        self.formatoEntry["justify"] = "center"
        self.formatoEntry["listvariable"] = lista
        self.formatoEntry["selectmode"] = tk.EXTENDED
        self.formatoEntry.place(x=700,y=120,width=100,height=65)
        

        authLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        authLab["font"] = ft
        authLab["fg"] = "white"
        authLab["bg"] = "black"
        authLab["justify"] = "center"
        authLab["text"] = "Introduzca la autenticacion a usar (id:pass) !opcional!:"
        authLab.place(x=10,y=160,width=346,height=33)

        self.authVar = tk.StringVar()
        authEntry = tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        authEntry["font"] = ft
        authEntry["fg"] = "black"
        authEntry["bg"] = "white"
        authEntry["justify"] = "center"
        authEntry["textvariable"] = self.authVar
        authEntry.place(x=360,y=160,width=128,height=30)

        fichLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        fichLab["font"] = ft
        fichLab["fg"] = "white"
        fichLab["bg"] = "black"
        fichLab["justify"] = "center"
        fichLab["text"] = "Introduzca el nombre del archivo del output !opcional!:"
        fichLab.place(x=10,y=200,width=346,height=33)

        self.fichero = tk.StringVar()
        fichEntry = tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        fichEntry["font"] = ft
        fichEntry["fg"] = "black"
        fichEntry["bg"] = "white"
        fichEntry["justify"] = "center"
        fichEntry["textvariable"] = self.fichero
        fichEntry.place(x=360,y=200,width=128,height=30)
        
        self.sslen = False
        sslDis = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        sslDis["font"] = ft
        sslDis["fg"] = "grey"
        sslDis["bg"] = "black"
        sslDis["justify"] = "center"
        sslDis["text"] = "Deshabilita el uso de SSL !opcional!"
        sslDis.place(x=500,y=200,width=346,height=33)
        sslDis["offvalue"] = "0"
        sslDis["onvalue"] = "1"
        sslDis["command"] = self.sslDis_command

        self.no404 = False
        no404Dis = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        no404Dis["font"] = ft
        no404Dis["fg"] = "grey"
        no404Dis["bg"] = "black"
        no404Dis["justify"] = "center"
        no404Dis["text"] = "Deshabilita 404 checks !opcional!"
        no404Dis.place(x=850,y=200,width=300,height=33)
        no404Dis["offvalue"] = "0"
        no404Dis["onvalue"] = "1"
        no404Dis["command"] = self.no404Dis_command
        
        portLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        portLab["font"] = ft
        portLab["fg"] = "white"
        portLab["bg"] = "black"
        portLab["justify"] = "center"
        portLab["text"] = "Introduzca el puerto a usar !opcional!:"
        portLab.place(x=10,y=240,width=300,height=33)
        
        self.puerto=tk.IntVar(value=80)
        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "black"
        GLineEdit_334["bg"] = "white"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["textvariable"] = self.puerto
        GLineEdit_334.place(x=310,y=240,width=85,height=30)

        portLab = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        portLab["font"] = ft
        portLab["fg"] = "white"
        portLab["bg"] = "black"
        portLab["justify"] = "center"
        portLab["text"] = "Introduzca el limite de tiempo en segundos para las request !opcional!:"
        portLab.place(x=410,y=240,width=380,height=33)
        
        self.timeout=tk.IntVar(value=10)
        GLineEdit_335=tk.Entry(root)
        GLineEdit_335["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_335["font"] = ft
        GLineEdit_335["fg"] = "black"
        GLineEdit_335["bg"] = "white"
        GLineEdit_335["justify"] = "center"
        GLineEdit_335["textvariable"] = self.timeout
        GLineEdit_335.place(x=800,y=240,width=85,height=30)

        GButton_797=tk.Button(root)
        GButton_797["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=578,y=280,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command
        self.cont=160

    def GButton_797_command(self):
        target = self.target.get()
        filtro = " -h "+target
        #index = self.formatoEntry.curselection()
        #puerto = str(self.puerto.get())
        if self.authVar.get() is not None: 
            filtro = filtro + " -id "+ self.authVar.get()
        if self.conf.get() is not None: 
            filtro = filtro + " -config "+ self.conf.get()
        if self.formatoEntry.curselection() is not None: 
            index = self.formatoEntry.curselection()
            filtro = filtro + " -Format "+ self.formatoEntry.get(index[0])
        if self.fichero.get() is not None: 
            filtro = filtro + " -output App/nikto_output/"+self.fichero.get()
        if self.outputdes is True: 
            filtro = filtro + " -Display on"
        if self.sslen is True: 
            filtro = filtro + " -nossl"
        if self.no404 is True: 
            filtro = filtro + " -no404"
        if self.puerto.get() != "":
            puerto = str(self.puerto.get()) 
            filtro = filtro + " -port "+ puerto
        if self.timeout.get() != "":filtro = filtro + " -timeout "+str(self.timeout.get())
        #print("perl App/nikto/program/nikto.pl "+ filtro)
        os.system("perl App/nikto/program/nikto.pl "+ filtro + "-C all")

    def outputDis_command(self):
        self.outputdes = True
    def sslDis_command(self):
        self.sslen = True
    def no404Dis_command(self):
        self.no404 = True

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()