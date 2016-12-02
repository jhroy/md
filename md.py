# -*- coding: utf-8 -*-
# ©2016 Jean-Hugues Roy. GNU GPL v3.

import requests, csv, os, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

n = 0

yo = webdriver.Chrome("/usr/local/bin/chromedriver")
# Normalement, j'ajoute une entête quand je me connecte à un site web par le biais d'un script, afin de m'identifier.
# Mais selenium ne permet pas d'envoyer des entêtes dans une requête à un site...
yo.get("http://www.cmq.org/bottin/index.aspx?lang=fr&a=1")

for a in reversed(range(1930,2017)): # Boucle qui passe toutes les années en ordre inverse, de 2016 à 1930
	fich1 = "cmq-{0}.csv".format(str(a)) # Après avoir terminé de moissonner les données sur une année, on crée un fichier CSV
	tout = []
	for x in range(1001,2000): # Boucle qui passe les 1000 numéros de permis possible à chaque année 

		n += 1
		noPermis = str(a)[2:]+str(x)[1:]
		print("On recherche le permis {0}".format(noPermis)) # Affichage à l'écran pour chacun des numéros de permis potentiels vérifiés
		# Ici, selenium fait deux choses
		# D'abord, il clique sur une case demandant de rechercher aussi les ex-membres du Collège des médecins (il est important, ici, de recueillir des données sur tous les médecins ayant intégré le Collège, même s'ils ont, depuis, démissionné, pris leur retraite ou s'ils sont décédés)
		boite = yo.find_element_by_id("cbxExMembres")
		boite.click()
		# Ensuite, il entre le numéro de permis dans le champ prévu à cet effet et appuie sur «RETURN»
		champ = yo.find_element_by_id("txbNoPermis")
		champ.send_keys(noPermis, Keys.RETURN)

		resultats = yo.page_source
		res = BeautifulSoup(resultats,"html.parser") # On utilise BeautifulSoup pour analyser la page de résultats retournée par le Collège

		# On vérifie maintenant si le numéro de permis recherché existe.
		# S'il n'existe pas, selenium clique sur un bouton rouge intitulé «Nouvelle recherche»
		if res.b != None:
			print("Le permis {0} n'existe pas".format(noPermis))
			suite = yo.find_element_by_name("btSubmit")
			suite.click()

		# Si le numéro existe, on moissonne toutes les informations que la page retournée contient
		else:
			print("Le permis {0} existe".format(noPermis))

			element = yo.find_element_by_partial_link_text(noPermis)
			element.click()

			resultat = yo.page_source
			pageMD = BeautifulSoup(resultat,"html.parser")

			md = {}
			md["ID"] = n
			md["Numéro de permis"] = noPermis

			medecin = pageMD.th.text
			medecin = medecin.replace("({0})".format(noPermis),"")
			nomPrenom = medecin.split(",")
			prenom = nomPrenom[1].strip()
			nom = nomPrenom[0].strip()
			md["Prénom"] = prenom
			md["Nom"] = nom
			print("Le permis {0} est celui de {1} {2}".format(noPermis,prenom,nom))

			genre = pageMD.find_all("td",string="Genre")[0].findNext("td").text.strip()
			md["Genre"] = genre

			typePermis = pageMD.find_all("td",string="Permis")[0].findNext("td").text.strip()
			md["Type de permis"] = typePermis

			statut = pageMD.find_all("td",string="Statut")[0].findNext("td").text.strip()
			md["Statut"] = statut

			specialites = pageMD.find_all("td",string="Spécialité(s)")[0].findNext("td").text
			if specialites == "":
				md["Nombre de spécialités"] = 0
				md["Spécialités"] = ""
			elif "," in specialites:
				specialites = specialites.split(",")
				nbSpecialites = len(specialites)
				print(nbSpecialites)
				md["Nombre de spécialités"] = nbSpecialites
				md["Spécialités"] = specialites
			else:
				md["Nombre de spécialités"] = 1
				md["Spécialités"] = specialites

			activites = pageMD.find_all("td",string="Activité(s)")[0].findNext("td").text
			md["Activités"] = activites
			if "=>" in activites:
				specialite = activites.split("=>")
				md["Spécialités"] = specialite[0].strip()
				md["Nombre de spécialités"] = 1

			habilitations = pageMD.find_all("td",string="Habilitation(s)")[0].findNext("td").text
			md["Habilitations"] = habilitations

			adresse = pageMD.find_all("td",string="Adresse")[0].findNext("td").text
			md["Adresse"] = adresse

			tel = pageMD.find_all("td",string="Téléphone")[0].findNext("td").text
			md["Numéro de téléphone"] = tel

			horo = pageMD.find("span",class_="dt").text
			md["Date et heure du moissonnage"] = horo

			print(md) # Affichage de toutes les données moissonnées aux fins de vérification
			tout.append(md)

			suite = yo.find_element_by_name("btNewsearch")
			suite.click()

	entetes = tout[0].keys()
	entetes = sorted(entetes)
	x = 0

	for ligne in tout:
		with open(fich1, 'a') as f:
			w = csv.DictWriter(f, entetes)
			if x == 0:
				w.writeheader()
			w.writerow(ligne)
		x += 1