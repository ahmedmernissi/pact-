
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



A=[5,5,5] #chauffage, ventilo,vibreur

alphabet =[b'a',b'b',b'c',b'd',b'e',b'f',b'g',b'h',b'i',b'j',b'k',b'l',b'm',b'n',b'o',b'p',b'q',b'r']


CMB=[b'$']
for i in range(len(A)):
     A[i]+=i*6
for c in A:
     CMB.append(alphabet[c])
print (CMB)
     


CMD = [b'l',b'c',b'f']



for c in CMB:
   status = send_cmd(c)
   if not status:
      print("fail")
   else:
      print("ok")


ser.close() #on ferme le port serie
