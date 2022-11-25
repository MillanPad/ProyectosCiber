import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
import subprocess
import socket
import os
import threading
from urllib.parse import unquote
class App:
    def __init__(self, root):
        #setting title
        root.title("XSS Attack")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        

        GLabel_553=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_553["font"] = ft
        GLabel_553["fg"] = "white"
        GLabel_553["bg"] = "black"
        GLabel_553["justify"] = "center"
        GLabel_553["text"] = "XSS Attack"
        GLabel_553.place(x=220,y=10,width=162,height=30)

        GLabel_409=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_409["font"] = ft
        GLabel_409["fg"] = "white"
        GLabel_409["bg"] = "black"
        GLabel_409["justify"] = "center"
        GLabel_409["text"] = "Introduce la URL objetivo:"
        GLabel_409.place(x=0,y=60,width=229,height=30)

        self.target = tk.StringVar()
        GLineEdit_713=tk.Entry(root)
        GLineEdit_713["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_713["font"] = ft
        GLineEdit_713["fg"] = "#333333"
        GLineEdit_713["justify"] = "center"
        GLineEdit_713["textvariable"] = self.target
        GLineEdit_713.place(x=240,y=60,width=89,height=30)

        GLabel_961=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_961["font"] = ft
        GLabel_961["fg"] = "white"
        GLabel_961["bg"] = "black"
        GLabel_961["justify"] = "center"
        GLabel_961["text"] = "Escoge el metodo que quieres que se use:"
        GLabel_961.place(x=40,y=110,width=235,height=30)

        vlista = ('GET','POST','GET and POST')
        lista = tk.Variable(value=vlista)
        self.GListBox_146=tk.Listbox(root)
        self.GListBox_146["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GListBox_146["font"] = ft
        self.GListBox_146["fg"] = "#333333"
        self.GListBox_146["justify"] = "center"
        self.GListBox_146["listvariable"] = lista
        self.GListBox_146["selectmode"] = tk.EXTENDED
        self.GListBox_146.place(x=290,y=100,width=120,height=50)

        

        #self.GMessage_297=tk.Text(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.GMessage_297["font"] = ft
        #self.GMessage_297["fg"] = "#333333"
        #self.GMessage_297["justify"] = "center"
        #self.GMessage_297["text"] = "Message"
        #self.GMessage_297["yscrollcommand"] = scrollbar.set
        #self.GMessage_297.place(x=100,y=300,width=327,height=155)

        GLabel_345=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_345["font"] = ft
        GLabel_345["fg"] = "white"
        GLabel_345["bg"] = "black"
        GLabel_345["justify"] = "center"
        GLabel_345["text"] = "Introduce un payload que quieras probar:"
        GLabel_345.place(x=40,y=190,width=237,height=30)

        self.payload = tk.StringVar()
        GLineEdit_833=tk.Entry(root)
        GLineEdit_833["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_833["font"] = ft
        GLineEdit_833["fg"] = "#333333"
        GLineEdit_833["justify"] = "center"
        GLineEdit_833["textvariable"] = self.payload
        GLineEdit_833.place(x=290,y=190,width=85,height=30)

        GButton_553=tk.Button(root)
        GButton_553["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_553["font"] = ft
        GButton_553["fg"] = "#000000"
        GButton_553["justify"] = "center"
        GButton_553["text"] = "Iniciar"
        GButton_553.place(x=230,y=240,width=98,height=30)
        GButton_553["command"] = self.GButton_553_command
        self.cont=270
        
        container = ttk.Frame(root)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0,0), window=self.scrollable_frame)

        canvas.configure(yscrollcommand=scrollbar.set,bg="black")
        container.place(x=0,y=270,width=600,height=230)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def GButton_553_command(self):
        url = self.target.get()
        filtro = "-u " + url
        line1 =""
        os.remove("App/PwnXSS/xss.txt")
        if self.GListBox_146.curselection() is not None:
            index = self.GListBox_146.curselection()
            filtro = filtro + " --method "+str(index[0])
        if self.payload.get() != "":
            filtro = filtro + " --payload '"+ self.payload.get()+ "'"
        os.system("python App/PwnXSS/pwnxss.py "+filtro)
        
        
        with open('App/PwnXSS/xss.txt', 'r') as f:
            for line in f:
                line1 = unquote(line)
                ttk.Label(self.scrollable_frame,text=line1,foreground="green",background="black").pack()
                
                self.cont=self.cont+20
        
        #self.GMessage_297["textvariable"]= line1
        #self.GMessage_297.insert(chars=line1)
        


if __name__ == "__main__":
    root = tk.Tk()  
    app = App(root)
    root.config(bg="black")
    root.mainloop()
   
