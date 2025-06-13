import psutil
import socket
import pyfiglet
from colorama import Fore
import time
import os
import ipaddress
import re
import platform



keywords = [
    "Windows", "Linux", "Ubuntu", "Debian", "OpenWrt", "macOS", "Darwin",
    "Android", "iOS", "OpenBSD", "FreeBSD", "VxWorks", "RouterOS", "Tizen",
    "webOS"
]

service_scripts = {
    "http": "http-vuln-cve2006-3392,http-enum,http-slowloris,http-phpmyadmin-dir-traversal,http-aspnet-debug,http-csrf,http-dombased-xss,http-shellshock,http-fileupload-exploiter,http-backup-finder,http-headers,http-internal-ip-disclosure,http-trace,http-userdir-enum,http-iis-webdav-vuln,http-cakephp-debug,http-vhosts,http-stored-xss,http-wordpress-enum,http-sitemap-generator,http-xssed,http-lfi,http-sql-injection,http-xxe,http-cookie-flags",
    "ftp": "ftp-anon,ftp-vsftpd-backdoor,ftp-proftpd-backdoor,ftp-bounce",
    "microsoft-ds": "smb-vuln-ms08-067,smb-vuln-ms17-010,smb-vuln-ms10-061,smb-vuln-cve2009-3103,smb-double-pulsar-backdoor",
    "samba": "smb-vuln-cve-2017-7494,smb-protocols",
    "smb": "smb-vuln-ms10-061,smb-vuln-cve2009-3103,smb-enum-users,smb-enum-shares,smb-security-mode,smbv2-enabled",
    "snmp": "snmp-brute,snmp-info,snmp-processes,snmp-win32-services",
    "dns": "dns-zone-transfer,dns-nsid,dns-recursion,dns-cache-snoop",
    "mysql": "mysql-empty-password,mysql-brute,mysql-users,mysql-databases",
    "postgresql": "pgsql-brute,pgsql-empty-password",
    "mssql": "ms-sql-brute,ms-sql-empty-password,ms-sql-config,ms-sql-info",
    "telnet": "telnet-encryption,telnet-brute",
    "smtp": "smtp-open-relay,smtp-brute,smtp-vuln-cve2010-4344",
    "ssh": "sshv1,ssh-brute,ssh-auth-methods,ssh-hostkey,ssh-run",
    "rdp": "rdp-vuln-ms12-020,rdp-enum-encryption",
    "vnc": "vnc-brute,vnc-info,vnc-title",
    "ldap": "ldap-rootdse,ldap-search,ldap-brute",
    "ntp": "ntp-monlist,ntp-info",
    "rpcbind": "rpc-grind,rpcinfo",
    "mongodb": "mongodb-brute,mongodb-info,mongodb-databases",
    "redis": "redis-brute,redis-info",
    "elasticsearch": "elasticsearch-info,elasticsearch-users",
    "nfs": "nfs-showmount,nfs-ls,nfs-statfs,nfs-export",
    "winrm": "winrm-brute,winrm-enum",
    "docker": "docker-version,docker-container-enum",
    "rsync": "rsync-list-modules",
    "netbios-ssn": "nbstat",
    "pop3": "pop3-brute,pop3-capabilities",
    "imap": "imap-brute,imap-capabilities",
    "tftp": "tftp-enum,tftp-vuln",
    "ipp": "cups-info,cups-enum-printers"
}

safe_service_scripts = {
    "http": "http-headers,http-title,http-enum,http-robots,http-methods,http-trace,http-cookie-flags",
    "ftp": "ftp-anon,ftp-bounce",
    "smb": "smb-enum-users,smb-enum-shares,smb-os-discovery",
    "snmp": "snmp-info,snmp-processes",
    "dns": "dns-nsid,dns-service-discovery",
    "mysql": "mysql-info,mysql-users,mysql-databases",
    "postgresql": "pgsql-info",
    "mssql": "ms-sql-info",
    "telnet": "telnet-encryption",
    "smtp": "smtp-commands,smtp-enum-users",
    "ssh": "ssh-auth-methods,ssh-hostkey",
    "rdp": "rdp-enum-encryption",
    "ldap": "ldap-search",
    "rpcbind": "rpcinfo",
    "nfs": "nfs-showmount,nfs-statfs",
    "winrm": "winrm-enum",
    "docker": "docker-version",
    "rsync": "rsync-list-modules",
    "pop3": "pop3-capabilities",
    "imap": "imap-capabilities",
    "tftp": "tftp-enum",
    "ipp": "cups-info"
}

def nse(open_port):
    if safe_or_aggressive == "1":
        scriptlist=safe_service_scripts
    elif safe_or_aggressive == "2":
        scriptlist=service_scripts

    for service in open_port.splitlines():
        if not re.match(r'^\d+/[a-z]+\s+open\s+', service):
            continue

        for keyword in scriptlist:
            if keyword in service:
                print(Fore.RED + f"{keyword.upper()} scriptleri çalıştırılıyor.")
                print(Fore.RESET)
                time.sleep(0.4)
                port = re.match(r'^(\d+)', service)
                if not port:
                    break
                port = port.group(1)
                script = scriptlist[keyword]

                if os_info3 == "Windows":
                    
                    script_outpot=os.popen(f"nmap -Pn -sT -p{port}  -T{speed} --script={script} {victim_local_ip}").read()
                    
                    print(script_outpot)
                    
                    break

                else:

                    script_outpot=os.popen(f"nmap -Pn -sS -p{port}  -T{speed} --script={script} {victim_local_ip}").read()
                
                    print(script_outpot)
                    break



def list_all_interfaces_with_subnet():
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for iface_name, iface_addrs in addrs.items():
        if stats[iface_name].isup:
            for addr in iface_addrs:
                if addr.family == socket.AF_INET:
                    print(Fore.GREEN + "")
                    print(f"Adaptör Adı: {iface_name}")
                    print(f"  IP: {addr.address}")
                    print(f"  Subnet Mask: {addr.netmask}")
                    print()


def clear_terminal():
    if os_info3 == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_os(localip):
    global guess
    global os_info2


    print(Fore.GREEN + "İşletim Sistemi")
    print(Fore.RESET)

    if os_info3 == "Windows":
        
        os_info = os.popen(f'nmap -Pn -T{speed} -sT -O --osscan-guess {localip}').read()
    else:
        os_info = os.popen(f'nmap -Pn -T{speed} -sS -O --osscan-guess {localip}').read()




    guess=False
    os1=False


    if "Running" not in os_info:

    
        for line in os_info.splitlines():
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    print(Fore.RED + "Kesin olarak işletim sistemi bulunamadı.")
                    os_info2=keyword
                    guess = True
                    os1=True
                    break
                
                if guess == True:
                    break
            

        if guess == False:
            print(Fore.RED + "Tespit edilemedi.")
            

            


    else:
        for line in os_info.splitlines():
            if "Running" in line:
                os_info2=line

                for osn in keywords:
                    
                    if osn.lower() in os_info2.lower():
                        os_info2=osn
                        os1=True
                        break
    
    if os1 == True:
        print(Fore.WHITE, os_info2)
    else:
        pass

def port_scan():
    global portscan


    if choose == "1":
        print(Fore.WHITE + "")
        print(Fore.GREEN + "Açık Portlar")
        print(Fore.RESET)
        if os_info3 == "Windows":
            portscan=os.popen(f"nmap -Pn -T{speed} -sT -p- -sV --open {victim_local_ip}").read()

            print(portscan)
        else:
            portscan=os.popen(f"nmap -Pn -T{speed} -sS -f -p- -sV --open {victim_local_ip}").read()

            print(portscan)


    else:
        print(Fore.WHITE + "")
        print(Fore.GREEN + "Açık Portlar")
        print(Fore.RESET)

        if os_info3 == "Windows":

            portscan=os.popen(f"nmap -Pn -T{speed} -sT -F --open {victim_local_ip}").read()
        else:
            portscan=os.popen(f"nmap -Pn -T{speed} -sS -F --open {victim_local_ip}").read()

        print(portscan)


os_info3 = platform.system()
figlet=pyfiglet.figlet_format("NMAP OTO")
time.sleep(0.2)

clear_terminal()
time.sleep(0.3)

print(Fore.RED, figlet)
time.sleep(0.2)
print(Fore.GREEN + "By: Fatih")
time.sleep(0.4)

print("İşletim Sistemi:", os_info3)
time.sleep(0.6)

clear_terminal()
print(Fore.RED, figlet)
time.sleep(0.5)
print(Fore.GREEN + "Yerel ağda[1] mı tarama yapacaksın yoksa dış ağda[2] mı tarama yapacaksın?")
time.sleep(0.4)
local_or_public=input(Fore.RED + "->")
time.sleep(0.6)

clear_terminal()
print(Fore.RED, figlet)

if local_or_public == "1":

    list_all_interfaces_with_subnet()
    time.sleep(0.2)
    print(Fore.WHITE + "Kullanılacak local IP adresini ve subnet mask adresini gir.")
    time.sleep(0.4)
    local_ip=input(Fore.RED + "IP ->")
    subnet_mask=input(Fore.RED + "Subnet mask ->")
    time.sleep(0.4)
    clear_terminal()

    print(Fore.RED, figlet)
    print(Fore.WHITE + "")

    network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)

    print("Denenecek IP adresleri: ", Fore.GREEN, network)
    time.sleep(0.5)
    print(Fore.WHITE + "")
    os.system(f"nmap -sn {network} -oG -")
    time.sleep(0.5)
    print("")
    print(Fore.RED + "Hangi cihazda tarama yapmak istersin?")
    time.sleep(0.2)

elif local_or_public == "2":
    print(Fore.WHITE + "IP veya URL girin.")
    time.sleep(0.2)

if local_or_public == "1":
    victim_local_ip=input(Fore.GREEN + "IP ->")
elif local_or_public == "2":
    victim_local_ip=input(Fore.GREEN + "IP/URL ->")

time.sleep(0.2)
print(Fore.RED + "Derin[1] mi yüzeysel[2] mi tarama yapmak istersin? (1/2)")
time.sleep(0.2)
choose=input(Fore.GREEN + "->")
time.sleep(0.5)
print(Fore.RED + "Hangi hızda tarama yapmak istersin? Sayı büyüdükçe tarama hızlanır.(0-5, 3 normal kabul edilir.)")
time.sleep(0.2)
speed=input(Fore.GREEN + "->")
time.sleep(0.5)

clear_terminal()

print(Fore.RED, figlet)
time.sleep(0.2)

if choose == "1":
    get_os(victim_local_ip)


time.sleep(0.7)


port_scan()


time.sleep(0.7)

print(Fore.WHITE + "")
print(Fore.GREEN + "NSE Çalıştırma")
time.sleep(0.4)
print(Fore.WHITE + "Güvenli Mod[1] Agresif Mod[2]")
time.sleep(0.2)
safe_or_aggressive=input(Fore.GREEN + "->")
time.sleep(0.3)

nse(portscan)