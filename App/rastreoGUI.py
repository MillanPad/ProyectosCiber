import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
from scapy.all import *
import socket
import sys
import threading
import requests


class App:
    def __init__(self, root):
        #setting title
        root.title("Rastreo de Paquetes")
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
        GLabel_950["fg"] = "#856ff8"
        GLabel_950["bg"] = "black"
        GLabel_950["justify"] = "center"
        GLabel_950["text"] = "Ratreo de Paquetes"
        GLabel_950.place(x=70,y=20,width=411,height=35)

        self.filtro = tk.StringVar()
        GLineEdit_132=tk.Entry(root)
        GLineEdit_132["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_132["font"] = ft
        GLineEdit_132["fg"] = "black"
        GLineEdit_132["bg"] = "#856ff8"
        GLineEdit_132["justify"] = "center"
        GLineEdit_132["textvariable"] = self.filtro
        GLineEdit_132.place(x=330,y=80,width=128,height=30)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "#856ff8"
        GLabel_981["bg"] = "black"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Introduzca el filtro que desea usar:"
        GLabel_981.place(x=10,y=80,width=260,height=33)

        GLabel_622=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#856ff8"
        GLabel_622["bg"] = "black"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "Introduzca el tiempo que quiere que dure el rastreo:"
        GLabel_622.place(x=10,y=120,width=346,height=33)

        self.duracion=tk.IntVar(value="2")
        GLineEdit_334=tk.Entry(root)
        GLineEdit_334["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_334["font"] = ft
        GLineEdit_334["fg"] = "black"
        GLineEdit_334["bg"] = "#856ff8"
        GLineEdit_334["justify"] = "center"
        GLineEdit_334["textvariable"] = self.duracion
        GLineEdit_334.place(x=356,y=120,width=125,height=30)

        archivoL=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        archivoL["font"] = ft
        archivoL["fg"] = "#856ff8"
        archivoL["bg"] = "black"
        archivoL["justify"] = "center"
        archivoL["text"] = "Introduzca el nombre del archivo del output:"
        archivoL.place(x=10,y=170,width=310,height=33)
        
        self.output=tk.StringVar()
        GLineEdit_335=tk.Entry(root)
        GLineEdit_335["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_335["font"] = ft
        GLineEdit_335["fg"] = "black"
        GLineEdit_335["bg"] = "#856ff8"
        GLineEdit_335["justify"] = "center"
        GLineEdit_335["textvariable"] = self.output
        GLineEdit_335.place(x=356,y=170,width=125,height=30)
                
        GButton_797=tk.Button(root)
        GButton_797["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=230,y=240,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command

    def GButton_797_command(self):
        filtro=self.filtro.get()
        duracion=self.duracion.get()
        output = self.output.get()
        self.cont=280
        if filtro is None:
            capture = sniff(filter=str(filtro),timeout=int(duracion))
        else:
            capture = sniff(timeout=int(duracion))
        wrpcap("App/rastreo_output/{}.cap".format(output),str(capture))
        self.printeo(str(capture))
    def printeo(self,lista):
        label = tk.Label(root,text=lista,fg="green",bg="black",justify="center")
        label.place(x=30,y=self.cont,width=530,height=20)
        self.cont=self.cont+20
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()