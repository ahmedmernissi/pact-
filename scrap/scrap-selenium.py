# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
import urllib.request
import numpy as np
import base64
import json
from IPython.display import display, Image
"""
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024,728))
display.start()
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



def url_to_image(url):
	#Download image, convert it to numpy array
	resp = urllib.request.urlretrieve(url,"temp.jpg")
	f = open("temp.jpg","rb")
	image = f.read()
	f.close()
	# Decode image to opencv
	Image(filename="temp.jpg")
	image = base64.b64encode(image)
	image = image.decode("utf-8")
	
	# return result
	return image

def write_image(image):
	print("[*] Painting name : ", image[0])
	img = image[1].encode("utf-8")
	img = base64.b64decode(img)
	f=open("image.jpg", "wb")
	f.write(img)
	f.close()

def write_data(tab):
	data = json.dumps(tab)
	f = open("data.json","w+")
	f.write(data)
	f.close()

def get_description(url):
	# Browser creation
	browser = webdriver.Firefox()
	# Browser waiting between actions
	browser.implicitly_wait(5)
	if("edit" not in url):
		browser.get(url)
		description = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/main/div[3]/div[4]/div[1]/p[1]')
		description = description.text
	else:
		print("[X] Not a valid url for description")
		description = ""
	# Finish by closing the browser
	browser.close()
	if description == "":
		description = "Error"
	return description



def scrap_michel_ange():
	# Browser creation
	print("[*] Create Browser ...")
	browser = webdriver.Firefox()

	# Browser waiting between actions
	browser.implicitly_wait(5)

	# Send request to izly.fr website
	print("[*] Starting website ...")
	browser.get('https://fr.wikipedia.org/wiki/Liste_des_%C5%93uvres_de_Michel-Ange')

	#user_nav = browser.find_element_by_xpath('/html/body/header/nav/a')
	#user_nav.click()

	tab = []
	# Because the first line is title
	i = 2

	while True:
		try:
			paint = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/main/div[3]/div[4]/div[1]/table[2]/tbody/tr['+str(i)+']/td[1]/i/a')
			img = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/main/div[3]/div[4]/div[1]/table[2]/tbody/tr['+str(i)+']/td[6]/a/img')
			src = img.get_attribute('src')
			img = url_to_image(src)
			description = get_description(paint.get_attribute('href'))
			tab.append([paint.text,img,description])
			i = i + 1
		except NoSuchElementException: 
			print("[x] End of table")
			break



	# Wait to let dev see the result
	sleep(5)

	# Finish by closing the browser
	browser.close()

	return tab
if not BDD:
	tab = scrap_michel_ange()
	write_data(tab)


if BDD:
	f = open("data.json", "r")
	data = f.read()
	f.close()
	tab = json.loads(data)
	artist = Library.Artist("Michel Ange", "Renaissance")
	for item in tab:
		write_image(item)
		work = Library.Work(item[0], "1574", "image.jpg", item[2], artist)
		work.push()

