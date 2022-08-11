import numpy as np

### ###

np.fromfile(filePath, dtype = 'int16');
### ex ###

np.fromfile('H0e005a.wav', dtype = 'int16');

### get the shape

array = np.fromfile('H-10e100a.wav', dtype = 'int16')
print(np.shape(array))

### HRTF database and explanations :
## https://sound.media.mit.edu/resources/KEMAR.html