#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install psycopg2-binary

import psycopg2
import sys
import os

# Pour tout le monde


# Pour Test et intégration
ourHost = os.getenv('HOST') # L'hôte auquel on ce connecte
ourPort = "5432"      # Le port auquel on ce connecte, par défaut
ourDatabase = "sens_art"


# In[2]:


def connect():
	user = "postgres"
	pwd = os.getenv('PASS')
	conn = psycopg2.connect(database = ourDatabase, user = user, password = pwd, host = ourHost, port = ourPort)
	cur = conn.cursor()
	return conn, cur

def close(conn, cur):
	conn.commit()
	cur.close()
	conn.close()


# In[3]:


class BDD(): 
	def __enter__(self): 
		self.conn, self.cur = connect()
		return self.cur
	  
	def __exit__(self, exc_type, exc_value, exc_traceback): 
		close(self.conn, self.cur)




# In[4]:


def init():
	with BDD() as cur :
		
		cur.execute("""CREATE TABLE artist (
			id integer PRIMARY KEY,
			name varchar(60),
			movement varchar(60),
			complete bool
		);""")

		cur.execute("""CREATE TABLE work (
			id integer PRIMARY KEY,
			title varchar(60), 
			artist integer,
			date varchar(10),
			image bytea,
			text text,
			label text,
			complete bool
		);""")

		cur.execute("""CREATE TABLE script (
			id integer REFERENCES work,
			matrixES text,
			nameSoundAtmosphere varchar(60),
			matrixSoundAtmosphere text,
			soundEffectFile bytea,
			complete bool
		);""")
		
		cur.execute("""CREATE TABLE soundEffects (
			id integer PRIMARY KEY,
			name varchar(60),
			soundFile bytea,
			complete bool
		);""")


# In[5]:


### Stolen sur https://zetcode.com/python/psycopg2/ + ctflF(Image)

def readFile(pathFile):

	fin = None

	try:
		fin = open(pathFile, "rb")
		data = fin.read()
		return data

	except IOError as e:

		print(f'Error {e.args[0]}, {e.args[1]}')
		sys.exit(1)

	finally:

		if fin:
			fin.close()
			

def writeFile(data, name):

	fout = None

	try:
		fout = open(name, 'wb')
		fout.write(data)

	except IOError as e:

		print(f"Error {0}")
		sys.exit(1)

	finally:

		if fout:
			fout.close()




# In[6]:


def getWork(ID):
	with BDD() as cur:
		a = Work(None, None, None, None, None)
		cur.execute("""SELECT * FROM work WHERE id = %s;""", (ID,))
		a.ID, a.title, a.artist, a.date, a.imgData, a.txt, a.labels, a.complete = cur.fetchone()
	a.img = a.title + " Image"
	#writeFile(a.imgData, a.img)
	a.artist = getArtist(a.artist)
	return a
		
def getAllWork():
	with BDD() as cur:
		cur.execute("""SELECT MAX(id) FROM work""")
		maxID = cur.fetchone()[0]
		listWork = []
		if maxID != None:
			for i in range(maxID+1):
				temp = getWork(i)
				if(temp != None):
					listWork.append(temp)
	return listWork

def getArtist(ID):
	with BDD() as cur:
		a = Artist(None, None)
		cur.execute("""SELECT * FROM artist WHERE id = %s;""", (ID,))
		a.ID, a.name, a.movement, a.complete = cur.fetchone()
	return a


# In[7]:


class Work:
	def __init__(self, title, date, img, txt, artist):
		self.title = title
		self.img = img
		if img:
			self.imgData = readFile(self.img)
		self.date = date
		self.txt = txt
		self.artist = artist

	ID = None #ID unique de l'oeuvre
	title = None #string
	artist = None #objet artist
	date = None  #string au format AAAA/SS, avec des chiffres arabes, mettre "X" si inconnu (exemple pour une oeuvre du XIIIeme dont on ne connais pas la date exacte : XXXX/13)
	img = None #nomDuFicbier
	imgData = None # donnée pour python 
	txt = None #le texte en temps que tel
	labels = None #hashmap de labal-score (inutilisé)
	complete = False #booletan l'objet est-il complet ?    
	

	def isFull(self):
		if(self.labels != None):
			self.complete = True
		return self.complete
	
	def createID(self):
		if(self.ID == None):
			with BDD() as cur:
				cur.execute("""SELECT EXISTS(SELECT 1 FROM work WHERE title = %s);""", (self.title,))
				if(cur.fetchone()[0]):
					cur.execute("""SELECT id FROM work WHERE title = %s;""", (self.title,))
					self.ID = cur.fetchone()[0]
				else:
					cur.execute("""SELECT MAX(id) FROM work;""")
					IDmax = cur.fetchone()[0]
					if IDmax is not None:
						self.ID = IDmax + 1
					else:
						self.ID = 0
	
	def getScript(self):
		a = Script(self)
		with BDD() as cur:
			cur.execute("""SELECT EXISTS(SELECT 1 FROM script WHERE id = %s)""",
					   (self.ID,))
			if(cur.fetchone()[0]):
				cur.execute("""SELECT * FROM script WHERE id = %s""",
						   (self.ID, ))
				a.ID, a.matrixES, a.nameSoundAtmosphere, a.matrixSoundAtmosphere, a.soundEffectFile, a.complete = cur.fetchone()
		return a
			
	
	def push(self):
		self.isFull()
		self.createID()
		self.artist.push()
		with BDD() as cur:
			cur.execute("""SELECT EXISTS(SELECT id FROM work WHERE id = %s)""", (self.ID,))
			if(cur.fetchone()[0]):
				cur.execute("""UPDATE work SET 
							title = %s,
							artist = %s,
							date = %s,
							image = %s,
							text = %s,
							label = %s,
							complete = %s
							WHERE id = %s;""", 
							(self.title, self.artist.ID, self.date, psycopg2.Binary(self.imgData), self.txt, self.labels, self.complete, self.ID))
			else:
				cur.execute("""INSERT INTO work (id, title, artist, date, image, text, label, complete) 
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """,
				(self.ID, self.title, self.artist.ID, self.date, psycopg2.Binary(self.imgData), self.txt, self.labels, self.complete))


# In[8]:


class Artist:
	def __init__(self, name, movement):
		self.name = name
		self.movement = movement
		
	name = None #Nom d'artiste, format String
	movement = None #nom du mouvement, format String
	ID = None #ID unique de l'oeuvre
	complete = True #booletan l'objet est-il complet ? (oui dès qu'il est créé)
	
	def isFull(self):
		return self.complete
	
	def createID(self):
		if(self.ID == None):
			with BDD() as cur:
				cur.execute("""SELECT EXISTS(SELECT 1 FROM artist WHERE name = %s);""", (self.name,))
				if(cur.fetchone()[0]):
					cur.execute("""SELECT id FROM artist WHERE name = %s;""", (self.name,))
					self.ID = cur.fetchone()[0]
				else:
					cur.execute("""SELECT MAX(id) FROM artist;""")
					IDmax = cur.fetchone()[0]
					if IDmax:
						self.ID = IDmax + 1
					else:
						self.ID = 0

	def push(self):
		self.isFull()
		self.createID()
		with BDD() as cur:
			cur.execute("""SELECT EXISTS(SELECT id FROM artist WHERE id = %s)""", (self.ID,))
			if(cur.fetchone()[0]):
				cur.execute("""UPDATE artist SET (name, movement, complete) = (%s, %s, %s) WHERE id = %s;""",(self.name, self.movement, self.complete, self.ID))
			else:
				cur.execute("""INSERT INTO artist (id, name, movement, complete)  
					VALUES (%s, %s, %s, %s); """,
				(self.ID, self.name, self.movement, self.complete))


# In[9]:


class Script:
	def __init__(self, work):
		self.work = work
		self.ID = self.work.ID
	
	matrixES = None
	nameSoundAtmosphere = None
	matrixSoundAtmosphere = None
	soundEffectFile = None
	work = None #objet work
	ID = None #ID unique de l'oeuvre
	complete = False #booletan l'objet est-il complet ?
	


	def isFull(self):
		if (None in [self.matrixES, self.nameSoundAtmosphere, self.matrixSoundAtmosphere, self.soundEffectFile, self.work]):
			self.complete = True
		return self.complete
	
	def createID(self):
		if(self.ID == None):
			self.work.createID()
			self.ID = self.work.ID

	def push(self):
		self.isFull()
		self.createID()
		self.work.push()
		with BDD() as cur:
			cur.execute("""SELECT EXISTS(SELECT id FROM script WHERE id = %s)""", (self.ID,))
			if(cur.fetchone()[0]):
				cur.execute("""UPDATE script SET (matrixES, nameSoundAtmosphere, soundEffectFile, complete, matrixSoundAtmosphere) = (%s, %s, %s, %s, %s) WHERE id = %s;""", (self.matrixES, self.nameSoundAtmosphere, self.soundEffectFile, self.complete, self.matrixSoundAtmosphere, self.ID))
			else:
				cur.execute("""INSERT INTO script (id, matrixES, nameSoundAtmosphere, soundEffectFile, complete, matrixSoundAtmosphere) 
					VALUES (%s, %s, %s, %s, %s, %s); """,
				(self.ID, self.matrixES, self.nameSoundAtmosphere, self.soundEffectFile, self.complete, self.matrixSoundAtmosphere))


# In[10]:

def getSoundEffects(ID):
	with BDD() as cur:
		a = SoundEffects(None, None)
		cur.execute("""SELECT * FROM soundEffects WHERE id = %s;""", (ID,))
		a.ID, a.name, a.soundFileData, a.complete = cur.fetchone()
	a.soundFile = a.title + " Audio"
	writeFile(a.soundFileData, a.soundFile)
	return a



class SoundEffects:
	def __init__(self, name, soundFile):
		self.name = name
		self.soundFile = soundFile
		if soundFile:
			self.soundFileData = readFile(self.soundFile)
	
	name = None #String
	soundFile = None #Nom du fichier
	soundFileData = None
	ID = None #ID unique de l'oeuvre
	complete = True#booletan l'objet est-il complet ? (oui dès qu'il est créé)
	
	
	
	def isFull(self):
		return self.complete
	
	def createID(self):
		if(self.ID == None):
			with BDD() as cur:
				cur.execute("""SELECT EXISTS(SELECT 1 FROM soundEffects WHERE name = %s);""", (self.name,))
				if(cur.fetchone()[0]):
					cur.execute("""SELECT id FROM soundEffects WHERE name = %s;""", (self.name,))
					self.ID = cur.fetchone()[0]
				else:
					cur.execute("""SELECT MAX(id) FROM soundEffects;""")
					IDmax = cur.fetchone()[0]
					if IDmax:
						self.ID = IDmax + 1
					else:
						self.ID = 0
	def push(self):
		self.isFull()
		self.createID()
		with BDD() as cur:
			cur.execute("""SELECT EXISTS (SELECT id FROM soundEffects WHERE id = %s)""", (self.ID,))
			if cur.fetchone()[0]:
				cur.execute("""UPDATE soundEffects SET (name, soundFile, complete) = (%s, %s, %s) WHERE id = %s""", (self.name, self.soundFileData, self.complete, self.ID))
			else:
				cur.execute("""INSERT INTO soundEffects 
				(id, name, soundFile, complete) 
				VALUES (%s %s %s %s);""", 
				(self.ID, self.name, self.soundFileData, self.complete))

# In[11]:
# If Library is not imported
# Then init database
if __name__ == '__main__':
	print("BDD Host : ", ourHost)
	init()
