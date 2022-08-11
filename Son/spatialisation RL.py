# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:06:43 2021

@author: -
"""

### UTILISER CE LIEN http://perso.univ-lemans.fr/~berger/CoursPython/co/LecWav.html

import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt
import io
from urllib.request import urlopen
import sounddevice as sd

# On copie l'emplacement du lien
lien = r'D:\Users\quent\Downloads\fast-baby-scratch_E_minor.wav'
    
def spacialisation(son, spacialisation): # On peut faire "dg" ou "gd"
    
    if (spacialisation != "gd"):
        if (spacialisation != "dg"):
            print("Cette spacialisation n'existe pas")
            return
            
    """Etape 1 : Echantillonement"""

    # On échantillone
    s, Fe = sf.read(son)
    N = s.shape[0]
    te = np.arange(0,N)/ Fe

    
    # On trace la graphique
    """fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(te, s, marker='+',label='y=son')
    ax.grid(True)
    ax.set(xlabel='temps(s)', ylabel='fréquence(Hz)', title='Echantillonage du signal')
    ax.legend(loc='lower right')
    plt.show()"""

    """Etape 2 : Transformation du son mono en stéréo"""
    
    l = len(s)
    cote_g = []
    cote_d = []
    if (spacialisation == "dg"):
        for i in range (l):
            cote_g.append(s[i][0] * te[i])
            cote_d.append(s[i][1] * te[l-i-1])
            
    if (spacialisation == "gd"):
        for i in range (l):
            cote_g.append(s[i][0] * te[l-i-1])
            cote_d.append(s[i][1] * te[i])
    
    """fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.plot(te, cote_g, marker='+',label='y=son')
    ax.grid(True)
    ax.set(xlabel='temps(s)', ylabel='fréquence(Hz)', title='Echantillonage du signal')
    ax.legend(loc='lower right')
    plt.show() """

    """Etape 3 : Ouverture du fichier"""
    
    data = [[cote_g[i], cote_d[i]] for i in range (l)]
    sd.play(data, Fe)
    
