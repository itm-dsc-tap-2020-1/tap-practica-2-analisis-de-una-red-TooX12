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
 sss'''