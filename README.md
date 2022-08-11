<<<<<<< HEAD
# Sens_art

## Description
Ce projet a pour but d'analyser des oeuvres picturales afin de les reproduires par le biais de sensations diverses telles que le toucher et l'ouie. Il consiste en le traitement en amont des oeuvres afin d'en déduire un script qui actionnera a posteriori divers modules (comme des vibreurs, un ventilateur, un tissu chauffant) contrôlé par une carte électronique. 

# Installation
You just need to install all packages for each modules :
- `$ pip3 install $(cat */requirements.txt)`

If you want to get the database on your local computer then install docker
- ([**Install docker**] (https://docs.docker.com/get-started/))

# Run the project

## Automaticly

If you want to start a server automaticly using docker then just use the script **sens_art.sh**

`$ bash sens_art.sh`

Or you can run each part seperately

## Manually

Run the script init_bdd_docker.sh with bash
- `$ cd BDD`
- `# bash init_bdd_docker.sh`

It will start a docker image of postgresql with local port 5432 open to access the database. And it will create the database named **sens_art**.

Then you can run the script **Library.py** from the BDD directory. This will start create all tables in the databases.

`$ python3 Library.py`

Then run the scraping script **scrap-selenium.py** to add data into the databases.

`$ python3 scrap-selenium.py`

Then you can run the first script of data treatment **rgb.py** in IA_image folder. This will create a **Script** for each **Work** present in the database.

`$ python3 rgb.py`

Finally you can run the script **Vector.py** to associate a sound ambiance to each **Work**.

`$ python3 Vector.py`

After that everything is set up you have your data treated in the database and you can run the code from the module Système embarqués.

`$ python3 matrice_systeme_embarque.py`

=======
# pact
>>>>>>> e6fb1a22d12301e7e6f2b36adcd322f2320e9bf9
