#!/usr/bin/bash

read -p "[Press enter to start] " # étape 1&2

echo "[*] Updating dependencies ..."
pip3 install $(cat */requirements.txt)
python3 test_integration/bdd-import.py


echo "[*] Checking for env variables ..."
echo "[*] Your host is $HOST"
echo "[*] Your password is $PASS"

read -p "[BDD - Ahmed]" # fin partie 3
clear

echo "[*] Creating the server localy"
sudo docker run --rm -d -p 5432:5432 -e POSTGRES_PASSWORD=$PASS --name postgres postgres

echo "[*] Waiting for server to be up and running ..."
sleep 20

echo "[*] Init database on the server ..."

# Create database in postgres
sudo docker exec postgres psql -U postgres -c "CREATE DATABASE sens_art;"

echo "[*] Create BDD table ..."
python3 BDD/Library.py
read -p "[Scraping - Théophile] " # fin étape 4
clear

echo "[*] Add data in the DATABASE ..."
cd scrap
python3 scrap-selenium.py
cd ..
read -p "[Analyse d'image - Laure-Amélie] " # fin étape 5
clear

echo "[*] Analyze images ..."
cd IA_image
python3 rgb.py
cd ..
read -p "[Analyse de texte - Quentin Ra] " # fin étape 6
clear

echo "[*] Analyze text description ..."
cd 'Analyse de texte'
python3 Vector.py
cd ..
read -p "[Récupération données - Ahmed] " # fin étape 7
clear

echo "[*] Testing getting the data back for one work ..."
cd test_integration
python3 get-script-SE.py
cd ..
read -p "[Nettoyer le répo - Basile] " # fin étape 8
clear

echo "[*] Cleaning the repo"
git clean -f
git clean -fd
read -p "[Press enter to finish] " # fin étape 9
clear

echo "[*] Every data has been processed"
echo "[*] Having a Good Day :-)"
