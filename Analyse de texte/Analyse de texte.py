# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Training of the network
#############################################################################

import numpy as np
import matplotlib.pyplot as plt

ponctuation = [" ",",",";",":","!","'","(",")","?",".","/","%","$","£","€","-","_","0","1","2","3","4","5","6","7","8","9",'"']

def sigmoide(x):
    return(1/(1 + np.exp(-x)))
    
def desigmoide(x):
    return((np.exp(-x))/((1+np.exp(-x))**2))   

def pretreatment(text):
    Listword=[]
    dic_indice = {}
    word = ""
    compteur = 0
    for character in text.lower() :
        if character in ponctuation :
            if word != "" :
                Listword += [word]
                if word in dic_indice :
                    dic_indice[word] += ',' + str(compteur)
                else :
                    dic_indice[word] = str(compteur)
                word = ""
                compteur += 1
        else :    
            word+=character
    
    return(Listword,dic_indice)

def training_data(token,window_size) :
    data=[]
    n=len(token)
    for i in range(n) :
        data_word = []
        for j in range(i-window_size,i+window_size+1) :
            if j<0 or j>=n :
                data_word += [-1]
            elif j != i :
                data_word += [j]
        data += [data_word]
    return(np.array(data))

def initialisation(word_number,vector_size) :
    #return(network_weight)
    return(np.random.randn(vector_size,word_number)*0.01)

def propagation(vector, network_weight) :
    matrix_dot = np.dot(vector,network_weight)
    probability = []
    
    for i in matrix_dot:
        probability += [sigmoide(i)]
        
    return(np.array(probability),matrix_dot)

def retro_propagation(vector,network_weight,matrix_dot,probability,window_size) :
    correction_weight = []
    correction_vector = []
    n,m = np.shape(network_weight)
    for i in range(n) :
        Ai = vector[i]
        sum_vector = 0
        for k in range(m) :
            Zk = matrix_dot[k]
            Lk = probability[k]
            Wik = network_weight[i][k]
            Yk = 0
            if np.abs(k-i) <= window_size and k != i :
                Yk = 1
            delta =  desigmoide(Zk) * 2*(Lk - Yk)
            sum_vector += Wik * delta
            correction_weight += [Ai * delta]
        correction_vector += [sum_vector]
    return(np.array(correction_weight).reshape(n,m),np.array(correction_vector))

def correction(vector,network_weight,correction_weight,correction_vector,alpha) :
    new_network_weight = network_weight - alpha * correction_weight
    new_vector = vector - alpha * correction_vector
    return(new_network_weight,new_vector)

def find_indice(chain) :
    L=[]
    indice=""
    for i in chain :
        if i == "," :
            L += [int(indice)]
            indice=""
        else :
            indice += i
    L += [int(indice)]
    return(L)

def cost_function(window_size,probability,i):
    cost=0
    for k in range(len(probability)) :
        Yk = 0
        if np.abs(k-i) <= window_size and k != i :
            Yk = 1
        cost += (probability[k]-Yk)**2
    return(cost)
        
        
    

def training(text,vector_size,window_size,alpha,initialize) :
    ListWord , dic_indice = pretreatment(text)
    word_number = len(ListWord)
    
    global List_cost
    global network_weight
    global word_dictionary
    
    if initialize :
        network_weight = initialisation(word_number,vector_size)
    
    for key , value in dic_indice.items() :
        List_indice = find_indice(value)
        correction_weight = np.array(vector_size*word_number*[0.0]).reshape(vector_size,word_number) 
        correction_vector = np.array(vector_size*[0.0])
        if key in word_dictionary :
            vector = word_dictionary[key]
        else : 
            vector = np.random.randn(vector_size)*10
        for i in List_indice :
            probability , matrix_dot = propagation(vector,network_weight)
            List_cost += [cost_function(window_size,probability,i)]
            new_correction_weight , new_correction_vector = retro_propagation(vector,network_weight,matrix_dot,probability,window_size)
            correction_weight += new_correction_weight
            correction_vector += new_correction_vector
        
        network_weight,vector=correction(vector,network_weight,correction_weight,correction_vector,alpha*(1/len(List_indice)))
        word_dictionary[key]= vector
    

##############################################################################
#Generating Corpus
##############################################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen

def extract_wiki(url):

    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')
    all_p=soup.find_all("p")
    text=""
    write = True
    crochet = False
    ref = ""
    refB = False
    refBwrite = False
    for p in all_p :
        p=str(p)
        for char in p :
            if type(char) != str :
                break
            if char == "<":
                write = False
                
            if char == "[" :
                crochet = True
           
            if write and not crochet :
                text += char
                
            if char == "]" :
                crochet = False
                
            if char == ">":
                write = True
                
            if not write :
                ref += char
                if ref == "<a href=" :
                    refB = True
                if refB and 'title="' in ref :
                    refBwrite == True
                if refBwrite :
                    if char == '"' :
                        refB = False
                        refBwrite = False
                        ref=""
                    text += char
                    
    return(text)

##############################################################################
#Try
##############################################################################

List_url = ["https://fr.wikipedia.org/wiki/Lisa_Gherardini#cite_note-33","https://fr.wikipedia.org/wiki/Le_Radeau_de_La_M%C3%A9duse","https://fr.wikipedia.org/wiki/Bonaparte_franchissant_le_Grand-Saint-Bernard","https://fr.wikipedia.org/wiki/La_Jeune_Fille_%C3%A0_la_perle"]
corpus=""
for url in List_url :
    corpus += extract_wiki(url)
    
L,M = pretreatment(corpus)
List = []
compteur=0
list=""
    
for mot in L :
    list += mot + " "
    compteur += 1
    if compteur == 100 :
        List += [list]
        compteur = 0
        list = ""
List += [list]

List_cost = []
network_weight = []
word_dictionary = {}

         
training(List[0],10,5,0.01,True)


cpt = 0

for i in range(1,len(L)) :
    training(List[i],10,5,0.01,False)
    cpt += 1
    if cpt == 10 :
        plt.plot([i for i in range(len(List_cost))],List_cost)
        plt.axis([0,len(List_cost),0,100])
        plt.show()
        cpt=0
    



            
            
            
    
        
    
    


    
    
    
    

    



                


        