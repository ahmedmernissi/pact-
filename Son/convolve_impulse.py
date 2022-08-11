import numpy as np 

###Convolve

def treatSignal(signal, filePathLeft, filePathRight):
    responseLeft = np.fromfile(filePathLeft, dtype = 'int16')
    responseRight = np.fromfile(filePathRight, dtype = 'int16')
    length = np.shape(response)
    resultLeft = np.zeros(length, dtype = float) 
    resultRight = np.zeros(length, dtype = float)
    for ind in range(length) :
        resultLeft[i] = convolution(length, signal, responseLeft, ind)
        resultRight[i] = convolution(length, signal, responseRight, ind)
    return(resultLeft, resultRight)

### Implement discrete convolution

def convolution(length,a1,a2, index):
    sum = 0
    for i in range(length):
        sum += a1[index-i] * a2[i]
    return(sum)
    
    