import serial
import time

ser=serial.Serial('COM5', 76800, timeout=2) #on ouvre un port serie sur le COM5 de vitesse 9600 bauds et de timeout 2 secondes
encoding = 'utf-8' #on initialise une variable avec le caractère utf-8 qui correspond à un format de données
ser.flush() #clean serial port
import threading
# IMPORT BDD MODULE
import os
# Condition if we ar in dev branch
if 'BDD' in os.listdir('..'):
	# Import module
	import Library
	import AmbianceSonore
	# Set imported to True
	BDD = True
else:
	BDD = False


##### Important Vars #####
# ID OF THE WORK
work_id = 5
# Time duration for Atmosphere
duration = 10

def thread_sound_play(name):
	# Play sound with module Son package
	AmbianceSonore.MakeNoise(script.nameSoundAtmosphere, script.matrixSoundAtmosphere, duration)


# If BDD is imported
if BDD:
	# Get a Work
	work = Library.getWork(work_id)
	# If work exist
	if work:
		# Get Script of the Work
		script = work.getScript()
		# Convert the string into a list
		script.matrixES = script.matrixES.replace("{","").replace("}","").split(",")
		script.matrixSoundAtmosphere = script.matrixSoundAtmosphere.replace("{","").replace("}","").split(",")
		# Convert the list of string into list of int
		script.matrixES = [float(i) for i in script.matrixES]
		script.matrixES = [int(i) for i in script.matrixES]
		script.matrixSoundAtmosphere = [int(i) for i in script.matrixSoundAtmosphere]
		# Print the matrix
		print("[*] matrix ES:", script.matrixES)
		print("[*] matrix sound ambiance:", script.matrixSoundAtmosphere)
		print("[*] Atmosphere name", script.nameSoundAtmosphere)
		# If we run the code locally
		if os.getenv('HOST') == 'localhost':
			# Create a thread to play the sound
			# so we can continue the script
			sound = threading.Thread(target=thread_sound_play, args=(1,))
			sound.start()
			time.sleep(15)
			a=0
			A=script.matrixES
			A[0] = 5
			A[1] = 5
			A[2] = 5
			alphabet=[b'a',b'b',b'c',b'd',b'e',b'f',b'g',b'h',b'i',b'j',b'k',b'l',b'm',b'n',b'o',b'p',b'q',b'r']
			for i in range (3):
				A[i]+= i*6
			for k in range (3):
				a=A[k]
				A[k]=alphabet[a]

			print(A)

			def send_cmd(x):
				 ser.write(x)
				 if ser.readline(2).decode(encoding)=="OK":
					 return 1
				 else:
					 return 0
			for i in range (3):
				status = send_cmd(A[i])
				if not status:
					print("fail")
				else:
					print("ok")
			ser.close() #on ferme le port serie
		else:
			print("[*] End of test job skipping sound play")
	else:
		print("[x] Work does not exist")

