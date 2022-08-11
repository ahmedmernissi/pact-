from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
browser = Firefox(options=opts)

irish_coast = 'https://mynoise.net/NoiseMachines/windSeaRainNoiseGenerator.php'
cafe_restaurant = 'https://mynoise.net/NoiseMachines/cafeRestaurantNoiseGenerator.php'

def jouer(ambiance):
    browser.get(ambiance)