import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
import socket
import sys
import threading
import requests


class App:
    def __init__(self, root):
        #setting title
        root.title("Escaneo de Directorio Web")
        #setting window size
        width=600
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        canvas = tk.Canvas(root)
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
        GLabel_950["text"] = "Escaneo de Directorio Web"
        GLabel_950.place(x=70,y=20,width=411,height=35)

        self.targetip = tk.StringVar()
        GLineEdit_132=tk.Entry(root)
        GLineEdit_132["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_132["font"] = ft
        GLineEdit_132["fg"] = "black"
        GLineEdit_132["bg"] = "white"
        GLineEdit_132["justify"] = "center"
        GLineEdit_132["textvariable"] = self.targetip
        GLineEdit_132.place(x=330,y=80,width=128,height=30)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "white"
        GLabel_981["bg"] = "black"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Introduzca el nombre del host o la direccion IP:"
        GLabel_981.place(x=10,y=80,width=346,height=33)

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "white"
        GLabel_622["bg"] = "black"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "Introduzca el nombre de la wordlist que desea usar"
        GLabel_622.place(x=10,y=120,width=346,height=33)

        segundafrase=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        segundafrase["font"] = ft
        segundafrase["fg"] = "white"
        segundafrase["bg"] = "black"
        segundafrase["justify"] = "center"
        segundafrase["text"] = "(Por defecto se usara el comun.txt en la carpeta wordlists):"
        segundafrase.place(x=15,y=143,width=346,height=33)

        self.wordlists=tk.StringVar(value="comun")
        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "black"
        GLineEdit_334["bg"] = "white"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["textvariable"] = self.wordlists
        GLineEdit_334.place(x=356,y=130,width=125,height=30)
                
        GButton_797=tk.Button(root)
        GButton_797["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=230,y=200,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command

    def GButton_797_command(self):
        targetip=self.targetip.get()
        wordlist=self.wordlists.get()
        self.cont=240
        print(wordlist)
        print(self.cont)
        try:
            #Mediante socket estableceremos conexion mediante el puerto 80 a el servidor web que hemos especificado
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            estado=sock.connect_ex((targetip,80))
            sock.close()
            #Comprueba si ha habido conexion o no
            if estado==0:
                
                
                label = tk.Label(root,text="Conexion probada=OK",fg="blue",bg="black",justify="center")
                print("hecho")
                label.place(x=30,y=self.cont,width=530,height=20)
                self.cont=self.cont+20
                pass
            else:
                self.cont=self.cont+20
                label = tk.Label(root,text= "Error - No se pudo conectar al host.",fg="red",bg="black",justify="center")
                label.place(x=30,y=self.cont,width=530,height=20)
                ##sys.exit()
            try:
                with open("App/wordlists/{}.txt".format(wordlist)) as file:
                    lista=file.read().strip().split('\n')
                t1 = threading.Thread(target=self.enumeracion(lista,targetip))
                t1.start()
                t1.join()
                
                label = tk.Label(root,text="Escaneo Terminado",fg="yellow",bg="black",justify="center")
                label.place(x=30,y=self.cont,width=530,height=20)
            except IOError:
                self.cont=self.cont+20
                label = tk.Label(root,text="Error - No se pudo importar la libreria: Comprueba que esta este en la carpeta de wordlists",fg="red",bg="black",justify="center")
                label.place(x=30,y=self.cont,width=530,height=20)
                #sys.exit()
        except socket.error:
            self.cont=self.cont+20
            label = tk.Label(root,text= "Error - No se pudo conectar al servidor",fg="red",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            #sys.exit()
    def enumeracion(self,lista_importada,host):
        for i in range(len(lista_importada)):
            #try:
                print("Probando con {}".format(lista_importada[i]))
                respuesta = requests.get('http://' + host + '/' + lista_importada[i]).status_code
                if respuesta == 200 :
                    label = tk.Label(root,text= "http://"+host+"/"+lista_importada[i]+": FOUND",fg="green",bg="black",justify="center")
                    label.place(x=30,y=self.cont,width=530,height=20)
                    self.cont=self.cont+20
            #except Exception:
                #sys.exit()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()