# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:02:27 2020

@author: quent
"""

# IMPORT BDD MODULE
import os
# Condition if we ar in dev branch
if 'BDD' in os.listdir('..'):
    # Import module
    import Library
    # Set imported to True
    BDD = True
else:
    BDD = False

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import logging

def MakeNoise(Noise,ListIntensity,timer) :
    """

    Parameters
    ----------
    Noise : Str
        Name of the Noise, ex: Irish Coast
    ListIntensity : int list (len 10)
        Percentage of the intensity of each cursor of the noise, ex: [0, 53, 96, 42, 11, 100, 100, 9, 87, 0]
    timer : int
        Length of the noise in seconds, ex: 120

    Returns
    -------
    None.

    """
    
    #Create page in headless mode
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    
    print("J'ai chargé firefox")
    
    #Launch the page of MyNoise and get the sound
    browser.get('https://mynoise.net/noiseMachines.php')
    browser.find_element_by_link_text(Noise).click()
    
    print("J'ai chargé la page")
    
    volDown=browser.find_element_by_css_selector('#volDown')
    while(volDown.get_attribute('style')=="pointer-events: none;"):
        time.sleep(1)
        print("chargement en cours")

    print("J'ai fini de chargé la page")
    
    
    # Set the volume
    for i in range(0,len(ListIntensity)):
        idcursor = str(i)
        link='#s'+ idcursor +' span.ui-slider-handle.ui-corner-all.ui-state-default'
        cursor = browser.find_element_by_css_selector(link)
        browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);",cursor,'style',"bottom: "+str(ListIntensity[i])+"%;")
        cursor.click()
        cursor.click()
        cursor.click()
        print(browser.find_element_by_css_selector('#s'+ idcursor +' div.ui-slider-range.ui-corner-all.ui-widget-header.ui-slider-range-min').get_attribute('style'))
        print("J'ai modifié le volume"+idcursor)
        
    time.sleep(timer)
    
    #Reset the volume
    for i in range(50):
        volDown.click()
        
    print("J'ai reset les volumes")

    browser.close()
    print("J'ai fermé firefox")
    print("Bonne Journée")


if __name__ == "__main__":
    if BDD:
        
        
    

