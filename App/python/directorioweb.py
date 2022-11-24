from asyncio.windows_events import NULL
import datetime
import requests
import socket
import sys
import threading
import colorama
from colorama import Fore
from colorama import Style
#Inicializa la libreria que nos permita editar el estilo de los print
colorama.init()
#Recibimos por teclado la direccion de el servidor web del que queremos realizar un escaneo de directorio
host=input("Introduzca el servidor web del que quiere escanear el directorio:")
#Recibimos por teclado el nombre del .txt que hara de diccionario antes etse debe de estar en la carpeta wordlists
libreria=input("Introduzca el nombre de la wordlist que desea usar(Por defecto se usara el comun.txt en la carpeta wordlists):")
#Si no se recibe ningun nombre de diccionario se usara el que hay por defecto
if not libreria:
    libreria="comun"
try:
    #Mediante socket estableceremos conexion mediante el puerto 80 a el servidor web que hemos especificado
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    estado=sock.connect_ex((host,80))
    sock.close()
    #Comprueba si ha habido conexion o no
    if estado==0:
        print(Fore.BLUE+"Conexion probada=OK"+Style.RESET_ALL)
        pass
    else:
        print(Fore.RED+"Error - No se pudo conectar al host."+Style.RESET_ALL)
        sys.exit()
except socket.error:
    print(Fore.RED+"Error - No se pudo conectar al servidor"+Style.RESET_ALL)
    sys.exit()
#Empezamos el "cronometro" para ver luego el tiempo que tarda en hacer el escaneo completo 
startTime = datetime.datetime.now()
print(Fore.YELLOW+"-" * 60)
print("Importando el diccionario...esta accion podria tardar un poco")
print("Escaneo empezado a: " + startTime.strftime("%x %X"))
print("-" * 60 + Style.RESET_ALL)
#Abrimos el archivo .txt que va a hacer de diccionario y si este falla nos dara error
try:
    with open("App/wordlists/{}.txt".format(libreria)) as file:
        lista=file.read().strip().split('\n')
except IOError:
    print(Fore.RED+"Error - No se pudo importar la libreria: Comprueba que esta este en la carpeta de wordlists"+Style.RESET_ALL)
    sys.exit()
#Esta funcion se encarga de la enumeracion de directorio probando palabra a palabra y imprimiendo aquellos directorios que coinciden con las palabras
# del diccionario
def enumeracion(lista_importada):
    for i in range(len(lista_importada)):
        try:
            respuesta = requests.get('http://' + host + '/' + lista_importada[i]).status_code
            if respuesta == 200 :
                print(Fore.GREEN+'http://'+host+'/'+lista_importada[i]+': FOUND'+Style.RESET_ALL)
        except Exception:
            sys.exit()
#Hacemos uso de thread para optimizar el tiempo de ejecucion
t1 = threading.Thread(target=enumeracion(lista))
t1.start()
t1.join()
#Paramos el cronometro
endTime = datetime.datetime.now()
runTime = endTime - startTime
runTime_in_s =  runTime.total_seconds()
#Calculamos el tiempo que ha tardado en horas, minutos y segundos
runtimeDays    = divmod(runTime_in_s, 86400)        
runtimeHours   = divmod(runtimeDays[1], 3600)               
runtimeMinutes = divmod(runtimeHours[1], 60)                
runtimeSeconds = divmod(runtimeMinutes[1], 1)  
#Informa de que el escaneo se ha completado y del tiempo que este ha tardado
print(Fore.YELLOW+"-" * 60)
print("Escaneo completo")
print(" Duracion:  %d horas %d minutos and %d segundos" % ( runtimeHours[0],runtimeMinutes[0], runtimeSeconds[0]))
print("-" * 60)
#Esperamos a que el usuario pulse una tecla para poder terminar del todo el programa
input("Introduzca una tecla para terminar"+Style.RESET_ALL)

