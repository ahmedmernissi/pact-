from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

### Opening thunder link ###
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts) 
#opening a Firefox browser, don't do it repeatedly without closing it 
browser.get('https://mynoise.net/noiseMachines.php') #site web location
thunder_link = browser.find_element_by_link_text('Distant Thunder') 
#noises are found thanks to a hyperlink

thunder_link.click()

## Moving the cursor ###

cursor_rain = browser.find_element_by_css_selector('#s8 span.ui-slider-handle.ui-corner-all.ui-state-default')
#in css selector syntax, "#" finds an ID 
#here we select the 8th cursor

action = ActionChains(browser)
action.drag_and_drop_by_offset(cursor_rain, 0, -100).perform()

#moves the selected cursor by the offset value
#1st argument : the source you want to move 
#2nd : number of pixels movement on x-axis
#3rd : numer of pixels movement on y-axis
#Negative numbers mean you move upward and leftward

time.sleep(5)
action.drag_and_drop_by_offset(cursor_rain, 0, 100).perform()
#above line lowers the rain sound after the 5-seconds pause

## Change the volume ###

#if you want to change the volume (values must be set to True for a change)
moveup = False
movedown = False
resetVolume = True

if (moveup):
    browser.find_element_by_css_selector('#volUp').click()
    moveup=False

if (movedown):
    browser.find_element_by_css_selector('#volDown').click()
    movedown=False
    
if (resetVolume):
    browser.find_element_by_css_selector('#reset').click()
    resetVolume=False

### REMEMBER TO CLOSE THE WINDOW ###
browser.close()