# Python-Chat-App
Networking Class Project CS 364
This only usable for educatinoal porposes.
Project depends on lessons from İstanbul Şehir University.

#Server.Py
HOST = '192.168.1.79' #Server ip adress set yours by ipconfig and get your internet ip4 address.
PORT = 1234 #Server Port that is basic port you can use any if there is a collision just change it.

#Client.Py / Chat.py
#----Now comes the sockets part----
HOST = input('HOST: ') #Thats part will set and wait for input so if you give Server Host you can coonect. You cange it make it const.
PORT = input('PORT: ') #Same as HOST
if not PORT:#If there is none you can use basic port which i declared
    PORT = 1234

