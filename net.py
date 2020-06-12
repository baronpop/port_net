###########################
'''
Requirements

1- Machine Name    [+]
2- Local IP        [+]
3- facebook IP     [+]
4- Your Remote IP  [+]
'''
###########################
import time
import socket
from urllib.request import urlopen
import sys
###########################
def Machine_Name():
   name = socket.gethostname()
   return(name)

def Local_IP():
   ip = socket.gethostbyname(Machine_Name())
   return(ip)

def Facebook_IP():
   fr = socket.gethostbyname("www.facebook.com")
   return(fr)

def Your_Remote_IP():
   remote = urlopen("https://ident.me")
   return(remote.read().decode())
###########################
time.sleep(1)
print("--->> How to use tool !")
time.sleep(2)
print('==============================')
print("[+] Machine Name Enter   { 1 }")
print("[+] Local IP Enter       { 2 }")
print("[+] facebook IP Enter    { 3 }")
print("[+] Your Remote IP Enter { 4 }")
print('==============================')
time.sleep(3)
while True:
   user = input("Enter The Number: ")
   
   if user == '1':
      print("Your machine name = ",Machine_Name())
   elif user == '2':
      print("Your Local IP = ",Local_IP())
   elif user == '3':
      print("Your facebook IP = ",Facebook_IP())
   elif user == '4':
      print("Your Your Remote IP = ",Your_Remote_IP())
   else:
      print("[!] Check The Entry")
      sys.exit()
##########################

