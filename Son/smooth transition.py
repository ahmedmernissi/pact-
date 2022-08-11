from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

### Opening thunder link ###
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://mynoise.net/noiseMachines.php')
thunder_link = browser.find_element_by_link_text('Distant Thunder')
thunder_link.click()

## Moving the cursor ###

cursor_rain = browser.find_element_by_css_selector('#s8 span.ui-slider-handle.ui-corner-all.ui-state-default')
#in css selector syntax, "#" finds an ID 

action = ActionChains(browser)

for i in range(20):
    time.sleep(1) #wait 1 secondes before increasing
                 #so it's not instantaneous
    action.drag_and_drop_by_offset(cursor_rain, 0, -5).perform()

### REMEMBER TO CLOSE THE WINDOW ###
browser.close()