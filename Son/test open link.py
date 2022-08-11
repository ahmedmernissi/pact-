from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

###Opening thunder link
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://mynoise.net/noiseMachines.php')
thunder_link = browser.find_element_by_link_text('Distant Thunder')
thunder_link.click()


###REMEMBER TO CLOSE THE WINDOW
browser.close()