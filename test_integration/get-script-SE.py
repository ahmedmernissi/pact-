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
		else:
			print("[*] End of test job skipping sound play")
		
	else:
		print("[x] Work does not exist")

