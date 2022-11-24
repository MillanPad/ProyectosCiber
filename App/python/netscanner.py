import socket
import sys
import os
import datetime
import threading
import colorama
from colorama import Fore
from colorama import Style
#Inicializa la libreria que nos permita editar el estilo de los print
colorama.init()
#Se pide al usuario que introduzca la direccion IP o el nombre del host que quiere escanear
remoteServer = input("Introduzca el nombre del host o la direccion IP que desea escanear: ")
#En caso de que sea introducido el nombre del host se sacar su direccion IP
remoteServerIP = socket.gethostbyname(remoteServer)
#Se abre el archivo ports.txt de la carpeta netscanner_files (que se podria editar) que carga los puertos mas comunes
ports_fich=open("App/netscanner_files/ports.txt","r")
ports_p=ports_fich.read()
ports_p=ports_p.split(':')
principial_ports=list(map(int, ports_p))
#Comprueba si se ha introducido un objetivo en caso de que no se sale del programa
if len(remoteServerIP) == 0:
    print("Un nombre de host o direccion IP es necesaria")
    sys.exit()
#Se imprimen avisos de como funciona el casteo de puertos 
print(Fore.YELLOW + "!Si se dejan las dos siguientes opciones por defecto solo se escanearan los puertos mas comunes!"+ Style.RESET_ALL)
print(Fore.YELLOW +"!Si se deja uno de los dos vacios cogeran los siguientes valores:\n!!!Si startPort vacio--> se empieza por el 0!!!\n!!!Si endPort vacio acaban en el puerto 1025!!!"+ Style.RESET_ALL)
#Si el usuario lo desea puede especificar porque puerto empezar y acabar el escaneo
startPort = input("Empezar por el puerto: ")
endPort = input("Terminar en el puerto: ")
#Empezamos el "cronometro" para ver luego el tiempo que tarda en hacer el escaneo completo 
openPortCount = 0
startTime = datetime.datetime.now()
    
print(Fore.YELLOW+"=" * 60)
print("Por favor espere, escaneando host remoto", remoteServerIP)
print("Escaneo empezado a: " + startTime.strftime("%x %X"))
print("=" * 60)
print("Puertos Abiertos:"+Style.RESET_ALL)
    
#Funcion que se encarga de escanear los puertos

try:
        #En caso de no haberse introducido porque puertos empezar y acabar, se usan los del archivo ports.txt
        if not startPort and not endPort:
            for port in principial_ports:  
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print(Fore.GREEN +" Puerto {}:     Abierto".format(port) + Style.RESET_ALL)
                    openPortCount += 1
                sock.close()
        else:
            #Si no se ha introducido solamente porque puerto empezar este cogera el valor de 0
            if not startPort:
                startPort=0
            #Si no se ha introducido solamente porque puerto terminar este cogera el valor de 1025
            if not endPort:
                endPort=1025
            for port in range(int(startPort),int(endPort)):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    print(Fore.GREEN +" Puerto {}:     Abierto".format(port) + Style.RESET_ALL)
                    openPortCount += 1
                sock.close()

    #En caso de que se presione Crtl+C que se muestre este mensaje
except KeyboardInterrupt:
        print(Fore.RED+"Se presiono Ctrl+C"+Style.RESET_ALL)
        sys.exit()
    #En caso de que no se resuelva el nombre del host  
except socket.gaierror:
        print(Fore.RED+"Error - No se pudo resolver el nombre de host."+Style.RESET_ALL)
        sys.exit()
    #En caso de que no se pueda conectar al servidor  
except socket.error:
        print(Fore.RED+"Error - No se pudo conectar al servidor"+Style.RESET_ALL)
        sys.exit()
  
#Paramos el cronometro 
endTime = datetime.datetime.now()
#Calculamos el tiempo que ha tardado en horas, minutos y segundos
runTime = endTime - startTime
runTime_in_s =  runTime.total_seconds()
runtimeDays    = divmod(runTime_in_s, 86400)        
runtimeHours   = divmod(runtimeDays[1], 3600)               
runtimeMinutes = divmod(runtimeHours[1], 60)                
runtimeSeconds = divmod(runtimeMinutes[1], 1)              
    
#Informa de que el escaneo se ha completado y del tiempo que este ha tardado
print(Fore.CYAN+"-" * 60)
print("Escaneo completo")
print(" Duracion:  %d horas %d minutos and %d segundos" % ( runtimeHours[0],runtimeMinutes[0], runtimeSeconds[0]))
print(" Puertos escaneados desde " + str(startPort) + " hasta " + str(endPort))
print(" " + str(openPortCount) + " puertos abiertos encontrados")
print("-" * 60+Style.RESET_ALL)
ports_fich.close()
#Esperamos a que el usuario pulse una tecla para poder terminar del todo el programa
print(Fore.YELLOW+"Si desea añadir puertos al escaneo por defecto o consultar estos mismos vea el documento ports.txt dentro de la carpeta netscanner_files"+Style.RESET_ALL)
input("Introduzca una tecla para terminar")