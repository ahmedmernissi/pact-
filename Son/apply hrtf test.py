import numpy as np
import soundfile as sf
import wavio


##constants
s, Fe = sf.read(lien)
sig = s[:,0]
lien = r'C:\Users\Loïc\Music\Chevaux_au_pas.wav'

###Functions to apply HRTF

def treatSignal(signal, filePathLeft, filePathRight):
    responseLeft = np.fromfile(filePathLeft, dtype = 'int16')
    responseRight = np.fromfile(filePathRight, dtype = 'int16')
    length = responseLeft.size // 2
    resultLeft = np.zeros(length, dtype = float) 
    resultRight = np.zeros(length, dtype = float)
    for ind in range(length) :
        resultLeft[ind] = convolution(length, signal, responseLeft, ind)
        resultRight[ind] = convolution(length, signal, responseRight, ind)
    return(resultLeft, resultRight)
    
def treatSignal2(signal, filePathLeft, filePathRight):
    responseLeft = np.fromfile(filePathLeft, dtype = 'int16')
    responseRight = np.fromfile(filePathRight, dtype = 'int16')
    length = responseLeft.size // 2
 
    for ind in range(length) :
        resultLeft = np.convolve( signal, responseLeft)
        resultRight = np.convolve(signal, responseRight)
    return(resultLeft, resultRight)

### Implement discrete convolution

def convolution(length,a1,a2, index):
    sum = 0
    for i in range(length):
        sum += a1[length + index-i] * a2[i]
    return(sum)
    
### Test apply

a1, a2 = treatSignal(sig, 'H-10e100a.wav', 'H-10e100a.wav')

###Save to a wav

wavio.write("C:\Users\Loïc\Desktop\myfile.wav", a1, fs, sampwidth=2)