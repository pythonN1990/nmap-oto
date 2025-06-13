# NMAP OTO

## Amacımız Ne?

Nmap bazen karışık olabilir, komutlar akılda kalmayabilir. Biz bu durumu kolaylaştırmak için **nmap-oto**'yu geliştirdik ve geliştirmeye devam ediyoruz. Amacımız, **Nmap**'in güçlü özelliklerini herkesin kolayca kullanabileceği bir arayüzle sunmak.

## Nasıl Kullanılır?

**nmap-oto**'yu kullanmak çok basit:

1. Komut satırını aç.
2. **nmap-oto**'nun olduğu dizine git.
3. **nmap-oto** yaz ve çalıştır!

Hepsi bu kadar!

## Nmap-oto ile Neler Yapabilirim?

Neler yapamazsın ki? **Nmap**'in sahip olduğu birçok komutu kullanabilirsin. Tabii ki **nmap-oto**, **Nmap**'in tüm komutlarını içermiyor ancak ihtiyacın olan en önemli komutları ekledik:

- **Ağ keşfi**: İnternet ağındaki cihazları tespit edebilirsin.
- **İşletim sistemi tespiti**: Hedef sistemin hangi işletim sistemini çalıştırdığını belirleyebilirsin.
- **Port taraması**: Açık ve kapalı portları analiz edebilirsin.
- **Servis ve versiyon tespiti**: Açık servisleri inceleyebilir ve güvenlik testleri yapabilirsin.
- **NSE scriptleri çalıştırma**: Güvenlik kontrolleri için **NSE** scriptlerini kullanabilirsin.

## Önemli Uyarı

⚠️ **nmap-oto** yalnızca eğitim ve siber güvenlik amaçlıdır. Sahip olmadığınız ya da izniniz olmayan cihazlarda/sunucularda tarama yapmayın!  

## nmap-oto DEJI Projesine Bağlıdır

🔗 **DEJI Web Sitesi**: [DEJI](https://deji.rf.gd)

## Sık Sorulanlar

**Hangi sistemlerde çalışır?**  
Bu araç, Python 3 ve Nmap yüklü olduğu sürece Windows 7 ve üzeri, Linux (Ubuntu, Debian, vb.) ile macOS’ta çalışır.

**nmap-oto ücretsiz mi?**  
Evet, tamamen ücretsizdir!

**nmap-oto'yu kimler kullanabilir?**  
Siber güvenliğe ilgi duyan herkes! Ancak etik kullanımı unutmayın.

**nmap-oto yasal mı?**  
Evet, ancak **sadece izinli testlerde kullanılması gerektiğini** unutmayın.

**Yeni özellikler eklenebilir mi?**  
Tabii ki! Geri bildirimlerinizi ve önerilerinizi bizimle paylaşabilirsiniz.

**nmap-oto ile Hangi Komutları Kullanabilirim?**

Başlangıçta ihtiyacın olan her komutu kullanabilirsin!
**Komutlar:**

* `-Pn`
* `-sS`
* `-sT`
* `-sS`
* `-sV`
* `-sn`
* `-T`
* `-F`
* `-p`
* `-open`
* `--script=`
* `-sS`
* `-O`

**Scriptler:**


HTTP
- `http-vuln-cve2006-3392`
- `http-enum`
- `http-slowloris`
- `http-phpmyadmin-dir-traversal`
- `http-aspnet-debug`
- `http-csrf`
- `http-dombased-xss`
- `http-shellshock`
- `http-fileupload-exploiter`
- `http-backup-finder`
- `http-headers`
- `http-internal-ip-disclosure`
- `http-trace`
- `http-userdir-enum`
- `http-iis-webdav-vuln`
- `http-cakephp-debug`
- `http-vhosts`
- `http-stored-xss`
- `http-wordpress-enum`
- `http-sitemap-generator`
- `http-xssed`
- `http-lfi`
- `http-sql-injection`
- `http-xxe`
- `http-cookie-flags`

FTP
- `ftp-anon`
- `ftp-vsftpd-backdoor`
- `ftp-proftpd-backdoor`
- `ftp-bounce`

Microsoft-DS
- `smb-vuln-ms08-067`
- `smb-vuln-ms17-010`
- `smb-vuln-ms10-061`
- `smb-vuln-cve2009-3103`
- `smb-double-pulsar-backdoor`

Samba
- `smb-vuln-cve-2017-7494`
- `smb-protocols`

SMB
- `smb-vuln-ms10-061`
- `smb-vuln-cve2009-3103`
- `smb-enum-users`
- `smb-enum-shares`
- `smb-security-mode`
- `smbv2-enabled`

SNMP
- `snmp-brute`
- `snmp-info`
- `snmp-processes`
- `snmp-win32-services`

DNS
- `dns-zone-transfer`
- `dns-nsid`
- `dns-recursion`
- `dns-cache-snoop`

MySQL
- `mysql-empty-password`
- `mysql-brute`
- `mysql-users`
- `mysql-databases`

PostgreSQL
- `pgsql-brute`
- `pgsql-empty-password`

MSSQL
- `ms-sql-brute`
- `ms-sql-empty-password`
- `ms-sql-config`
- `ms-sql-info`

Telnet
- `telnet-encryption`
- `telnet-brute`

SMTP
- `smtp-open-relay`
- `smtp-brute`
- `smtp-vuln-cve2010-4344`

SSH
- `sshv1`
- `ssh-brute`
- `ssh-auth-methods`
- `ssh-hostkey`
- `ssh-run`

RDP
- `rdp-vuln-ms12-020`
- `rdp-enum-encryption`

VNC
- `vnc-brute`
- `vnc-info`
- `vnc-title`

LDAP
- `ldap-rootdse`
- `ldap-search`
- `ldap-brute`

NTP
- `ntp-monlist`
- `ntp-info`

RPCBind
- `rpc-grind`
- `rpcinfo`

MongoDB
- `mongodb-brute`
- `mongodb-info`
- `mongodb-databases`

Redis
- `redis-brute`
- `redis-info`

Elasticsearch
- `elasticsearch-info`
- `elasticsearch-users`

NFS
- `nfs-showmount`
- `nfs-ls`
- `nfs-statfs`
- `nfs-export`

WinRM
- `winrm-brute`
- `winrm-enum`

Docker
- `docker-version`
- `docker-container-enum`

Rsync
- `rsync-list-modules`

NetBIOS-SSN
- `nbstat`

POP3
- `pop3-brute`
- `pop3-capabilities`

IMAP
- `imap-brute`
- `imap-capabilities`

TFTP
- `tftp-enum`
- `tftp-vuln`

IPP
- `cups-info`
- `cups-enum-printers`

