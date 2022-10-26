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
def menu(opcion):
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
                print("1.Denegacion de Servicio")
                print("2.ARP spoofing")
                print("3.SQL")
                print("4.XSS")
                print("5.Salir")
                op_ataque=int(input('Introduce su opcion:'))
                if(op_ataque==1):
                    op_deneg=0
                    while not(op_deneg==3):
                        clearConsole()
                        print(pyfiglet.figlet_format("DENEGACION"))
                        print("1.DDoS")
                        print("2.DoS")
                        print("3.Salir")
                        op_deneg=int(input('Introduce su opcion:'))
                        if(op_deneg==1):
                            print("Invocar funcion de DDoS")
                        elif(op_deneg==2):
                            print("Invocar funcion DoS")
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
                            
                            clearConsole()
                            print("-" * 60)
                            print(pyfiglet.figlet_format("CONFIGURACION DEL RASTREO"))
                            op_filtr=int(input('Desea filtros(Si=1 No=2):'))
                            if(op_filtr==1):
                                filtro=input('Escriba el filtro que desee que lleven:')
                                print("-" * 60)
                                tiempo_ejecucion=input('Escriba el tiempo en segundos que desee que dure el rastreo(Por Defecto son 2 segundos):')
                                if not tiempo_ejecucion: tiempo_ejecucion = 2 
                                capture = sniff(filter=filtro,timeout=int(tiempo_ejecucion))
                            elif(op_filtr==2):
                                print("-" * 60)
                                tiempo_ejecucion=input('Escriba el tiempo en segundos que desee que dure el rastreo(Por Defecto son 2 segundos):')
                                if not tiempo_ejecucion: tiempo_ejecucion = 2 
                                capture = sniff(timeout=int(tiempo_ejecucion))
                            print(Fore.GREEN+"-" * 60)
                            print("RASTREO COMPLETADO")
                            print(capture.summary())
                            print("-" * 60+Style.RESET_ALL)
                            nombre_archivo=input(Fore.YELLOW+"Si desea guardar el output en un fichero escriba el nombre con el que quiera guardarlo:"+Style.RESET_ALL)
                            if not nombre_archivo: input("Introduzca una tecla para terminar")
                            else: 
                                #fichero= open("App/rastreo_output/{}.txt".format(nombre_archivo),"a")
                                #fichero.write(str(capture.summary()))
                                wrpcap("App/rastreo_output/{}.cap".format(nombre_archivo),capture.summary())
                                input("Introduzca una tecla para terminar")
                                #fichero.close()

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
t1 = threading.Thread(target=menu(opcion))
t1.start()
t1.join() 