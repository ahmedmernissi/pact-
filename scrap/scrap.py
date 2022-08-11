#!/usr/bin/env python3
import requests
import re
from time import sleep

# Painting object with name and image data in it
class Painting:
	# Init the object with None value
	def __init__(self):
		self.name = None
		self.img = None
	# Set name could also use object.name = value
	def set_name(self, name):
		self.name = name
	# Set image could also use object.img = value
	def set_img(self, img):
		self.img = img
	# Return a list object with data in it 
	def get_data(self):
		return [self.name, self.img]

# Function to scrap data from wikipedia page
def scrap(url):
	# Http get request to wikipedia
	r = requests.get(url)
	# Data = http text response
	data = r.text
	# Find all table with a header of size 2 before it
	# data without \n (raw text)
	regex = re.findall(r'(<h2><span .*?></span></h2><table .*?>.*?</table>)',data.replace('\n','').lower())
	# for each table found
	for i in range(0,len(regex)):
		if("peinture" in regex[i]) or ("tableau" in regex[i]):
			data = regex[i]
	if not data:
		print("[x] Error no paintings found")
		exit(1)
	# For each line of the table get data
	# Regex: for each unique string between two tr balise
	regex = re.findall(r'<tr>(.*?)</tr>', data)
	data = regex
	# create list of all paintings
	liste_of_paint = []
	# Create regex to match html tag
	sanitize = re.compile(r'<.*?>')
	# For each painting
	for painting in data:
		# creating an object painting
		paint = Painting()
		# Find every data in each cell
		regex = re.findall(r'<td>(.*?)</td>', painting)
		# if it is a real painting not a title cell
		if len(regex) != 0:
			# Removing 
			regex[0] = sanitize.sub('', regex[0])
			# set name of this painting object
			paint.set_name(regex[0])
			# Try to find url if it exist
			try:
				# Find url of the image
				regex[-1] = re.findall(r'src=\"(.*?)\"', regex[-1])[0]
				# Replace double / to get normal url
				regex[-1] = regex[-1].replace("//","")
				# Add url to paint object
				paint.set_img(regex[-1])
				liste_of_paint.append(paint.get_data())
			# in case it has no image
			except IndexError:
				print("[x] Error no image for : ", paint.name)
				paint.set_name(None)
				paint.set_img(None)
	# TODO : Decode image url to get data in base64 or blob
	# TODO: add json structure with name of artist and list of all paintings
	# TODO: ADD text data for each painting (see if there is a link on the name and scrap it
	# TODO : Test this code with other artists
	return liste_of_paint

if __name__ == "__main__":
	data = scrap("https://fr.wikipedia.org/wiki/Liste_des_%C5%93uvres_de_Michel-Ange")
	print("Final output = ")
	print(data)
