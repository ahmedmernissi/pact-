from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

Irish_Coast = 'https://mynoise.net/NoiseMachines/windSeaRainNoiseGenerator.php'
Cafe_Restaurant = 'https://mynoise.net/NoiseMachines/cafeRestaurantNoiseGenerator.php'
Distant_Thunder = 'https://mynoise.net/NoiseMachines/thunderNoiseGenerator.php'
Autumn_Walk = 'https://mynoise.net/NoiseMachines/autumnWalkSoundscapeGenerator.php'

ListAmbiance = [Distant_Thunder, Cafe_Restaurant, Irish_Coast, Autumn_Walk]

"""ListIntensity refers to the volum level of each component in the atmosphere, Timer refers to the duration of the sound"""

def Play(Noise,ListIntensity,timer) : 

    
    ### Checking if the Noise is correct
    if Noise not in ListAmbiance:
        return "The noise isn't correct"
    
    ### Create page in headless mode
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    action = ActionChains(browser)
    
    print("J'ai chargé firefox")
    
    ### Open the page
    browser.get(Noise)
    time.sleep(20)
    
    print("J'ai chargé la page")

    ### Reset the volume
    for i in range(50):
        browser.find_element_by_css_selector('#volDown').click()
        
    print("J'ai reset les volumes")
    
    ### Set the volume
    for i in range(0,len(ListIntensity)):
        idcursor = str(i)
        link='#s'+ idcursor +' span.ui-slider-handle.ui-corner-all.ui-state-default'
        cursor_rain = browser.find_element_by_css_selector(link)
        action.drag_and_drop_by_offset(cursor_rain, 0, -ListIntensity[i]*100).perform()
        print("J'ai modifié le volume"+idcursor)
        
    time.sleep(timer)
    
    ### Reset the volume
    for i in range(50):
        browser.find_element_by_css_selector('#volDown').click()
        
    print("J'ai reset les volumes")
    

    browser.close()
    print("J'ai fermé Firefox")
    print("Bonne Journée")