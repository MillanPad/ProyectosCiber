import tkinter as tk
import tkinter.font as tkFont
root = tk.Tk()
class App:
    def __init__(self, root):
        #setting title
        root.title("Framework")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(bg="black")
        root.resizable(width=True, height=True)

        GLabel_105=tk.Label(root)
        ft = tkFont.Font(family='Times New Roman',size=25)
        GLabel_105["font"] = ft
        GLabel_105["fg"] = "#856ff8"
        GLabel_105["bg"] = "black"
        GLabel_105["justify"] = "center"
        GLabel_105["text"] = "Menu de Proyectos"
        GLabel_105.place(x=80,y=0,width=412,height=37)

        encabezado1=tk.Label(root)
        ft = tkFont.Font(family="Times New Roman",size=15)
        encabezado1["font"] = ft
        encabezado1["fg"] = "#856ff8"
        encabezado1["bg"] = "black"
        encabezado1["justify"] = "center"
        encabezado1["text"] = "Posibles ataques a realizar:"
        encabezado1.place(x=80,y=50,width=412,height=37)

        GButton_302=tk.Button(root)
        GButton_302["anchor"] = "center"
        GButton_302["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_302["font"] = ft
        GButton_302["fg"] = "#000000"
        GButton_302["justify"] = "center"
        GButton_302["text"] = "ARP Spoofing"
        GButton_302.place(x=50,y=100,width=118,height=30)
        GButton_302["command"] = self.GButton_302_command

        GButton_317=tk.Button(root)
        GButton_317["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_317["font"] = ft
        GButton_317["fg"] = "#000000"
        GButton_317["justify"] = "center"
        GButton_317["text"] = "SQL Attack"
        GButton_317.place(x=169,y=100,width=118,height=30)
        GButton_317["command"] = self.GButton_317_command

        GButton_310=tk.Button(root)
        GButton_310["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_310["font"] = ft
        GButton_310["fg"] = "#000000"
        GButton_310["justify"] = "center"
        GButton_310["text"] = "XSS Attack"
        GButton_310.place(x=287,y=100,width=118,height=30)
        GButton_310["command"] = self.GButton_310_command

        GButton_37=tk.Button(root)
        GButton_37["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_37["font"] = ft
        GButton_37["fg"] = "#000000"
        GButton_37["justify"] = "center"
        GButton_37["text"] = "DoS"
        GButton_37.place(x=405,y=100,width=118,height=30)
        GButton_37["command"] = self.GButton_37_command

        encabezado2=tk.Label(root)
        ft = tkFont.Font(family="Times New Roman",size=15)
        encabezado2["font"] = ft
        encabezado2["fg"] = "#856ff8"
        encabezado2["bg"] = "black"
        encabezado2["justify"] = "center"
        encabezado2["text"] = "Posibles escaneos a realizar:"
        encabezado2.place(x=80,y=150,width=412,height=37)

        GButton_93=tk.Button(root)
        GButton_93["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_93["font"] = ft
        GButton_93["fg"] = "#000000"
        GButton_93["justify"] = "center"
        GButton_93["text"] = "Escaneo de Vulnerabilidades"
        GButton_93.place(x=50,y=200,width=174,height=36)
        GButton_93["command"] = self.GButton_93_command

        GButton_429=tk.Button(root)
        GButton_429["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_429["font"] = ft
        GButton_429["fg"] = "#000000"
        GButton_429["justify"] = "center"
        GButton_429["text"] = "Escaneo de Puertos"
        GButton_429.place(x=224,y=200,width=132,height=36)
        GButton_429["command"] = self.GButton_429_command

        encabezado3=tk.Label(root)
        ft = tkFont.Font(family="Times New Roman",size=15)
        encabezado3["font"] = ft
        encabezado3["fg"] = "#856ff8"
        encabezado3["bg"] = "black"
        encabezado3["justify"] = "center"
        encabezado3["text"] = "Posible sniff de red:"
        encabezado3.place(x=80,y=250,width=412,height=37)

        GButton_989=tk.Button(root)
        GButton_989["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_989["font"] = ft
        GButton_989["fg"] = "#000000"
        GButton_989["justify"] = "center"
        GButton_989["text"] = "Rastreo de Paquetes"
        GButton_989.place(x=224,y=300,width=132,height=36)
        GButton_989["command"] = self.GButton_989_command

        GButton_917=tk.Button(root)
        GButton_917["bg"] = "#856ff8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_917["font"] = ft
        GButton_917["fg"] = "#000000"
        GButton_917["justify"] = "center"
        GButton_917["text"] = "Escaneo de Directorio Web"
        GButton_917.place(x=356,y=200,width=169,height=36)
        GButton_917["command"] = self.GButton_917_command

    def GButton_302_command(self):
        import arpGUI
        root.destroy()
        arp = tk.Tk()
        app = arpGUI.App(arp)
        arp.mainloop()
        


    def GButton_317_command(self):
        import sqlGUI
        root.destroy()
        sql = tk.Tk()
        app = sqlGUI.App(sql)
        sql.mainloop()


    def GButton_310_command(self):
        print("command")



    def GButton_37_command(self):
        import dosGUI
        root.destroy()
        dos = tk.Tk()
        app = dosGUI.App(dos)
        dos.mainloop()


    def GButton_93_command(self):
        import nikGUI
        root.destroy()
        nik = tk.Tk()
        app = nikGUI.App(nik)
        nik.mainloop()


    def GButton_429_command(self):
        import netscannGUI
        root.destroy()
        nescan = tk.Tk()
        app = netscannGUI.App(nescan)
        nescan.mainloop()
        
        
        
        


    def GButton_989_command(self):
        import rastreoGUI
        root.destroy()
        rastreo = tk.Tk()
        app = rastreoGUI.App(rastreo)
        rastreo.mainloop()


    def GButton_917_command(self):
        import directoriowebGUI
        root.destroy()
        dirweb = tk.Tk()
        app = directoriowebGUI.App(dirweb)
        dirweb.mainloop()

#if __name__ == "__main__":

app = App(root)
root.mainloop()


