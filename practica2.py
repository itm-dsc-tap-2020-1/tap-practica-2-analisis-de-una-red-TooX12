#Antonio Juárez Castillo

import os

hostname = 'www.itmorelia.edu.mx'
respuesta= os.system('ping-c 1 '+hostname)
if respuesta == 0:
    print(hostname+": está en funcionamiento!")
else:
    print(hostname+": No funciona!")

red= '200.33.171.0/24'
os.system('nmap -sT '+red)

'''
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.00089s latency).
Not shown: 996 filtered ports
PORT     STATE SERVICE
2000/tcp open  cisco-sccp
5060/tcp open  sip
5432/tcp open  postgresql
6969/tcp open  acmsoda

Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.00086s latency).
Not shown: 999 filtered ports
PORT     STATE SERVICE
5060/tcp open  sip

Nmap scan report for 200.33.171.13
Host is up (0.72s latency).
Not shown: 660 closed ports, 335 filtered ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5060/tcp open  sip

Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.0011s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE
2000/tcp open  cisco-sccp
5060/tcp open  sip

Nmap scan report for 200.33.171.66
Host is up (0.00099s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE
119/tcp  open  nntp
2000/tcp open  cisco-sccp

Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.00091s latency).
Not shown: 997 filtered ports
PORT     STATE  SERVICE
53/tcp   closed domain
2000/tcp open   cisco-sccp
5060/tcp open   sip

Nmap scan report for 200.33.171.125
Host is up (0.0011s latency).
Not shown: 989 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
139/tcp   open  netbios-ssn
443/tcp   open  https
445/tcp   open  microsoft-ds
548/tcp   open  afp
2000/tcp  open  cisco-sccp
3306/tcp  open  mysql
5060/tcp  open  sip
8181/tcp  open  intermapper
49154/tcp open  unknown

Nmap scan report for 200.33.171.254
Host is up (0.0014s latency).
Not shown: 995 closed ports
PORT     STATE    SERVICE
2000/tcp open     cisco-sccp
2809/tcp filtered corbaloc
5060/tcp open     sip
6666/tcp filtered irc
7402/tcp filtered rtps-dd-mt'''