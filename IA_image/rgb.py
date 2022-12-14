# -*- coding: utf-8 -*-
"""RGB

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iAqeWGQzgvRpB7azW2uy9jGZESnlFm8
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

print("BDD =", BDD)

# Import package to make web request
import urllib.request

import imageio
import numpy as np

from PIL import Image

from sklearn import linear_model




def model():
    # Try to create a folder of paintings
    try:
      os.mkdir("paintings")
    except:
      print("[x] Couldn't create folder ")

    # Download some paintings

    urllib.request.urlretrieve("https://assets.paintbasket.com/wp-content/uploads/how-to-paint-dogs-acrylic-banner-500-80.jpg","paintings/painting.jpg")
    urllib.request.urlretrieve("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/gracie-mae-cat-painting-dora-hathazi-mendes.jpg","paintings/painting2.jpg")
    urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/d/d7/Meisje_met_de_parel.jpg","paintings/painting3.jpg")
    urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/9/91/David_napoleon.jpg","paintings/painting4.jpg")
    urllib.request.urlretrieve("https://fr.wahooart.com/Art.nsf/O/8LT3A9/$File/Otto-Dix-Hugo-Erfurth-with-a-dog.JPG","paintings/painting5.jpg")
    urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/d/d7/Meisje_met_de_parel.jpg","paintings/painting6.jpg")
    urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/1/15/JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg","paintings/painting7.jpg")

    # List available paintings in our folder
    print(os.listdir("paintings"))
    
    RGB_image("paintings/painting2.jpg")
    RGB_folder("paintings")



def RGB_folder(folder):
  """

  Parameters
  ----------
  folder : link
      Link which leads to the folder which contains every (n) paintings, ex: "../paintings"

  Returns
  -------
  Matrix (n,3) of the average value between [-1,1] of colors reb, green, blue in each paintings.

  """
  AVG = []
  image_files = os.listdir(folder)
  for image in image_files:
    image_file = os.path.join(folder, image)
    try:
      # opening image
      im = Image.open(image_file)
      # Resize image
      new_image = im.resize((image_size, image_size))
      # Saving new image
      new_image.save(image_file)
      # Reading image as a matrix
      image_data = (imageio.imread(image_file).astype(float) - 
                    pixel_depth / 2) / pixel_depth
      # Printing image matrix shape
      print("size : ", image_data.shape)
      avg_r = np.sum(image_data[:,:,0])/(image_size*image_size)
      avg_g = np.sum(image_data[:,:,1])/(image_size*image_size)
      avg_b = np.sum(image_data[:,:,2])/(image_size*image_size)
      AVG.append([avg_r,avg_g,avg_b])
    except (IOError, ValueError) as e:
      print('Could not read:', image_file, ':', e, '- it\'s ok, skipping.')
      return [0,0,0]
  return AVG

def RGB_image(image):
    """

    Parameters
    ----------
    Image : link
        Link which leads to the paintings, ex: "../paintings/painting7.jpg"

    Returns
    -------
    Matrix (1,3) of the average value between [-1,1] of colors reb, green, blue in the painting.

    """
    try:
      # opening image
      im = Image.open(image)
      # Resize image
      new_image = im.resize((image_size, image_size))
      # Saving new image
      new_image.save(image)
      # Reading image as a matrix
      image_data = (imageio.imread(image).astype(float) - 
                    pixel_depth / 2) / pixel_depth
      # Printing image matrix shape
      print("size : ", image_data.shape)
      if(len(image_data.shape) == 3):
        avg_r = np.sum(image_data[:,:,0])/(image_size*image_size)
        avg_g = np.sum(image_data[:,:,1])/(image_size*image_size)
        avg_b = np.sum(image_data[:,:,2])/(image_size*image_size)
      else:
        print("[x] Error image is black and white ...")
        return [0, 0, 0]
    except (IOError, ValueError) as e:
      print('Could not read:', image, ':', e, '- it\'s ok, skipping.')
      return [0, 0, 0]
    return [avg_r,avg_g,avg_b]



def vibreurs(image):
  """

  Parameters
  ----------
  Image : link
      Link which leads to the paintings, ex: "../paintings/painting7.jpg"

  Returns
  -------
  Matrix (1,3) of the vibrators intensity.

  """
  etat = []
  predict = reg.predict([RGB_image(image)])
  print(predict)
  for i in range (6):
    predict[0,i] -= 0.5
    if predict[0,i] < 0:
      etat.append(0)
    else:
      predict[0,i] *= 10
      etat.append(np.round(predict[0,i]))
  print(etat)
  return etat
  
  
  
def matrice_ambiance_sonore(image):
  """

  Parameters
  ----------
  Image : link
      Link which leads to the paintings, ex: "../paintings/painting7.jpg"

  Returns
  -------
  Matrix (1,10) of the intensity of the musical ambiance parameters .

  """
  if RGB_image(image) != [0,0,0]:

    avg_rgb = np.ones((1,3))*RGB_image(image)

    

    v0 = max (min (int((0.5 - avg_rgb[0][0])*10) , 10) , 0)
    v1 = max (min (int((0.5 + avg_rgb[0][1] + 0.1)*10) , 10) , 0)
    v2 = max (min (int((0.5 + avg_rgb[0][2] + 0.1)*10) , 10) , 0)
    return([v0, v0, v0, v0, v1, v1, v1, v2, v2, v2])
  else:
    return [0]




############## IMAGE INFORMATION ##############
pixel_depth = 255.0  # Number of levels per pixel.
image_size = 800  # Pixel width and height.

############## GET DATASET ##############
model()

############## DEFINE AI MODEL ##############
reg = linear_model.Ridge(alpha=.5)
reg.fit(RGB_folder("paintings"), [[1,0,0,0,0,1],[0,0,0,0,0,0],[1,0,1,1,0,1],[0,1,1,0,0,1],[0,1,1,0,1,1],[0,0,1,0,0,1],[0,1,1,1,0,1]])


vibreurs("paintings/painting7.jpg")

if BDD:
  works = Library.getAllWork()
  for work in works:
    Library.writeFile(work.imgData, "image.jpg")
    print("vibreur in bdd : ", vibreurs("image.jpg"))
    script = Library.Script(work)
    script.matrixES = vibreurs("image.jpg")
    script.matrixSoundAtmosphere = matrice_ambiance_sonore("image.jpg")
    print("script : ", script.matrixSoundAtmosphere)
    script.push()
