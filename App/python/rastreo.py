from scapy.all import *
from datetime import datetime
from colorama import Fore
from colorama import Style
import pyfiglet
def empezar(control,hay_filtro):
    #Empieza la configuracion del ratreo
    print("-" * 60)
    print(pyfiglet.figlet_format("CONFIGURACION DEL RASTREO"))
    if control==0:
        op_filtr=int(input('Desea filtros(Si=1 No=2):'))
        #Pedimos el tiempo que queremos que se este rastreando
        tiempo_ejecucion=input('Escriba el tiempo en segundos que desee que dure el rastreo(Por Defecto son 2 segundos):')
        if not tiempo_ejecucion: tiempo_ejecucion = 2 
    else:
        op_filtr=1
        tiempo_ejecucion = 3 
    #Si decimos que queremos filtros se nos preguntara que filtro queremos
    if(op_filtr==1):
        #Guardamos el filtro en una variable
        if hay_filtro is None:
            filtro=input('Escriba el filtro que desee que lleven:')
        else:
            filtro=hay_filtro
        print("-" * 60)
        
        #Hacemos uso de la funcion sniff de la libreria scapy para rastrear
        # los paquetes en nuestra red con el filtro que hemos introducido
        capture = sniff(filter=str(filtro),timeout=int(tiempo_ejecucion))
    #Si no queremos filtro solo se nos preguntara el tiempo que queremos que dure el rastreo
    elif(op_filtr==2):
        print("-" * 60)
        tiempo_ejecucion=input('Escriba el tiempo en segundos que desee que dure el rastreo(Por Defecto son 2 segundos):')
        if not tiempo_ejecucion: tiempo_ejecucion = 2 
        #Hacemos uso de la funcion sniff de la libreria scapy para rastrear
        capture = sniff(timeout=int(tiempo_ejecucion))
    #Imprimimos por pantalla el resultado del rastreo
    print(Fore.GREEN+"-" * 60)
    print("RASTREO COMPLETADO")
    print(capture.summary())
    print("-" * 60+Style.RESET_ALL)
    if control==0:
        #Preguntamos al usuario si quiere guardar en un fichero el resultado del ratreo
        nombre_archivo=input(Fore.YELLOW+"Si desea guardar el output en un fichero escriba el nombre con el que quiera guardarlo:"+Style.RESET_ALL)
        if not nombre_archivo: input("Introduzca una tecla para terminar")
        #En el caso que nos haya escrito un nombre
        else: 
            #Guardamos el resultado del ratreo en un fichero .cap con el que nos ha introducido el usuario
            wrpcap("App/rastreo_output/{}.cap".format(nombre_archivo),capture)
            input("Introduzca una tecla para terminar")
        
 