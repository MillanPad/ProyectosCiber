import os
import platform
import socket
import threading
from scapy.all import *
from datetime import datetime
from colorama import Fore
from colorama import Style
import pyfiglet
ascii_banner = pyfiglet.figlet_format("PROYECTOS FRAMEWORK")
opcion=0
#Funcion para limpiar la consola de texto
clearConsole = lambda: os.system('cls' if os.name=='nt' else 'clear')
#Funcion que despliega el menu con las funciones del framework

while (opcion!=3):
        clearConsole() 
        print(ascii_banner)
        print("1.Ataque")
        print("2.Escaneo")
        print("3.Salir")
        opcion= int(input('Introduce su opcion:'))

        if(opcion==1):
            op_ataque=0
            while not(op_ataque==5):
                clearConsole()
                print(pyfiglet.figlet_format("ATAQUES"))
                print("1.DoS")
                print("2.ARP spoofing")
                print("3.SQL")
                print("4.XSS")
                print("5.Salir")
                op_ataque=int(input('Introduce su opcion:'))
                if(op_ataque==1):
                    
                    clearConsole()
                        
                elif(op_ataque==2):
                    print("Invocar ataque ARP")
                elif(op_ataque==3):
                    print("Invocar funcion ataque SQL")
                elif(op_ataque==4):
                    print("Invocar funcion ataque XSS")
        elif(opcion==2):
            op_escaneo=0
            while not(op_escaneo==3):
                clearConsole()
                print(pyfiglet.figlet_format("ESCANEO"))
                print("1.Vulnerabilidades")
                print("2.De Red")
                print("3.Salir")
                op_escaneo= int(input('Introduce su opcion:'))
                if(op_escaneo==1):
                    #Llamar a la funcion que usara nikto#
                    print("Nikto")
                elif (op_escaneo==2):
                    op_red=0
                    while not(op_red==4):
                        clearConsole()
                        print(pyfiglet.figlet_format("ESCANEO DE RED"))
                        print("1.Rastreo de Paquetes")
                        print("2.Escaneo de puertos")
                        print("3.Escaneo de directorio web")
                        print("4.Salir")
                        op_red=int(input('Introduce su opcion:'))
                        if(op_red==1):
                            #Limpia la salida de la consola 
                            import rastreo
                            clearConsole()
                            rastreo.empezar(0,None)
                        elif (op_red==2):
                            #print("Invocar funcion Escaneo de puertos")
                            import netscanner
                            clearConsole()
                            netscanner
                        elif (op_red==3):
                            clearConsole()
                            import directorioweb
                            directorioweb
#Hacemos uso de thread para optimizar el tiempo de ejecucion
