import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt
import io
from urllib.request import urlopen
import sounddevice as sd
import random

# On copie l'emplacement du lien
lien = r'C:\Users\HAMON\Desktop\horse-gallop.wav'

def spatialization(link, spatialization):
    """

    Parameters
    ----------
    Noise : Str
        Name of the Noise ex: Irish Coast
    ListIntensity : int list (len 10)
        DESCRIPTION.
    timer : int
        DESCRIPTION.

    Returns
    -------
    None.

    """

    
    if (spatialization not in ["rl" , "lr"]):
        print("This spatialization doesn't exist")
        return
            
    # We create the sample
    s, Fe = sf.read(link)
    N = s.shape[0]
    te = np.arange(0,N)/ Fe
    
    # Plotting the sample to check if it has worked
    # fig, ax = plt.subplots(nrows=1, ncols=1)
    # ax.plot(te, s, marker='+',label='y=son')
    # ax.grid(True)
    # ax.set(xlabel='temps(s)', ylabel='fréquence(Hz)', title='Echantillonage du signal')
    # ax.legend(loc='lower right')
    # plt.show()

    #Creating two outputs
    
    l = len(s)
    l_side = []
    right_s = []
    S = np.transpose(s)
    if (spatialization == "rl"):
        r_gain = np.linspace(1, 0, l)
        l_gain = np.linspace(0, 1, l)
            
    if (spatialization == "lr"):
        r_gain = np.linspace(0, 1, l)
        l_gain = np.linspace(1, 0, l)
    
    # Plotting both ouput to check if it has worked
    # fig, ax = plt.subplots(nrows=1, ncols=1)
    # ax.plot(te, cote_g, marker='+',label='y=son')
    # ax.grid(True)
    # ax.set(xlabel='temps(s)', ylabel='fréquence(Hz)', title='Echantillonage du signal')
    # ax.legend(loc='lower right')
    # plt.show()

    #Opening the file
    data = np.transpose(np.array([l_gain * S[0], r_gain * S[1]]))
    sd.play(data, Fe)
    
