from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

### Opening thunder link ###
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://mynoise.net/noiseMachines.php')
thunder_link = browser.find_element_by_link_text('Distant Thunder')
thunder_link.click()

#if you want to change the volume (values must be set to True for a change)
moveup = True
movedown = False
resetVolume = False

## Change the volume ###


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