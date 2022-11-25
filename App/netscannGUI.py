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
        root.title("Escaneo de Puertos")
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
        GLabel_950["text"] = "Escaneo de Puertos"
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
        GLabel_622["text"] = "Empezar por Puerto:"
        GLabel_622.place(x=10,y=120,width=200,height=30)

        self.puertoin=tk.IntVar()
        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "black"
        GLineEdit_334["bg"] = "white"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["textvariable"] = self.puertoin
        GLineEdit_334.place(x=220,y=120,width=85,height=30)

        GLabel_470=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_470["font"] = ft
        GLabel_470["fg"] = "white"
        GLabel_470["bg"] = "black"
        GLabel_470["justify"] = "center"
        GLabel_470["text"] = "Terminar por Puerto:"
        GLabel_470.place(x=10,y=160,width=201,height=30)

        self.puertofin=tk.IntVar()
        GLineEdit_430=tk.Entry(root)
        GLineEdit_430["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_430["font"] = ft
        GLineEdit_430["fg"] = "black"
        GLineEdit_430["bg"] = "white"
        GLineEdit_430["justify"] = "center"
        GLineEdit_430["textvariable"] = self.puertofin
        GLineEdit_430.place(x=220,y=160,width=87,height=30)
        
        
        GCheckBox_629=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_629["font"] = ft
        GCheckBox_629["fg"] = "grey"
        GCheckBox_629["bg"] = "black"
        GCheckBox_629["justify"] = "center"
        GCheckBox_629["text"] = "Escanear puertos por defecto guardados en el documento ports.txt en la carpeta netscanner_files "
        GCheckBox_629.place(x=10,y=200,width=570,height=53)
        GCheckBox_629["offvalue"] = "0"
        GCheckBox_629["onvalue"] = "1"
        GCheckBox_629["command"] = self.GCheckBox_629_command

        self.control = False

        GButton_797=tk.Button(root)
        GButton_797["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=230,y=250,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command

        

    def GCheckBox_629_command(self):
        self.control = True
        
        


    def GButton_797_command(self):
        target=self.targetip.get()
        inicio=self.puertoin.get()
        fin=self.puertofin.get()
        self.cont = 280
        if self.control is True:
            ports_fich=open("App/netscanner_files/ports.txt","r")
            ports_p=ports_fich.read()
            ports_p=ports_p.split(':')
            ports_fich.close()
            principial_ports=list(map(int, ports_p))
                
            for port in principial_ports:  
                
                thread = threading.Thread(target=self.connection(target,port))
                thread.start()
                    
        else:
            for port in range(inicio,fin+1):
                
                thread = threading.Thread(target=self.connection(target,port))
                thread.start()
        label = tk.Label(root,text="Escaneo Completado",fg="yellow",bg="black",justify="center")
        label.place(x=30,y=self.cont,width=530,height=20)
    def connection(self,ip,prt):
        try:
            print("Probando con ip: {} y puerto: {}".format(ip,prt))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, prt))
            if result == 0:
                label = tk.Label(root,text=" Puerto {}:     Abierto".format(prt),fg="green",bg="black",justify="center")
                label.place(x=30,y=self.cont,width=530,height=20)
                self.cont=self.cont+20
            sock.close()
            #En caso de que se presione Crtl+C que se muestre este mensaje
        except KeyboardInterrupt:
            print("Se presiono Ctrl+C")
            sys.exit()
                #En caso de que no se resuelva el nombre del host  
        except socket.gaierror:
            print("Error - No se pudo resolver el nombre de host.")
            sys.exit()
                #En caso de que no se pueda conectar al servidor  
        except socket.error:
            print("Error - No se pudo conectar al servidor")
            sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
