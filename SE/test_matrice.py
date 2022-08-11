import serial
import time

ser=serial.Serial('COM5', 76800, timeout=2) #on ouvre un port serie sur le COM5 de vitesse 9600 bauds et de timeout 2 secondes
encoding = 'utf-8' #on initialise une variable avec le caractère utf-8 qui correspond à un format de données
ser.flush() #clean serial port


def send_cmd(x):
     ser.write(x)
     if ser.readline(2).decode(encoding)=="OK":
         return 1
     else:
         return 0

CMD = [[3,1],[2,2],[5,1],[0,1],[4,0],[0,1]]

for i in range (5):
    for j in range (1):
        CMD[i][j] = CMD[i][j] + i*10 + j*6


print (CMD)

for c in CMD:
   status = send_cmd(c)
   if not status:
      print("fail")
   else:
      print("ok")


ser.close() #on ferme le port serie
