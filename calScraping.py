#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import re
import os
import time
from icalendar import Calendar, Event
import dateparser
from datetime import datetime, timedelta
from pytz import timezone
import logging
import requests
import sys



logger = logging.getLogger('scraper')
hdlr = logging.FileHandler('/var/log/scraper.log')


class Cours:
    """
        Class to create a Cours
    """
    def __init__(self, dateDebut, dateFin, matiere, enseignant, commentaire):
        """
            Constructor 
                dateDebut
                dateFin
                matiere
                enseignant
                commentaire
        """
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.matiere = matiere
        self.enseignant = enseignant
        self.commentaire = commentaire

    def __str__(self):
        return "date debut : " + self.dateDebut + "\ndate de fin : " + self.dateFin + "\nmatiere : " + self.matiere + "\nenseignant : " + self.enseignant + "\ncommentaire : " + self.commentaire + "\n"
    
    def __repr__(self):
        return "Cours()"

def scrapCours(driver, cours, year, semaine):
    """
        To only scrap table of classes of a week
    """
    soup = BeautifulSoup(driver.page_source, 'lxml')

    cours.append(Cours(
    semaine[1] + " " + year + " 9:00",
    semaine[1] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_matin")).get_text() ))

    cours.append(Cours(
    semaine[1] + " " + year + " 13:30",
    semaine[1] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_apres_midi")).get_text() ))

    cours.append(Cours(
    semaine[2] + " " + year + " 9:00",
    semaine[2] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_matin")).get_text() ))

    cours.append(Cours(
    semaine[2] + " " + year + " 13:30",
    semaine[2] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_apres_midi")).get_text() ))

    cours.append(Cours(
    semaine[3] + " " + year + " 9:00",
    semaine[3] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_matin")).get_text() ))

    cours.append(Cours(
    semaine[3] + " " + year + " 13:30",
    semaine[3] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_apres_midi")).get_text() ))

    cours.append(Cours(
    semaine[4] + " " + year + " 9:00",
    semaine[4] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_matin")).get_text() ))

    cours.append(Cours(
    semaine[4] + " " + year + " 13:30",
    semaine[4] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_apres_midi")).get_text() ))

    cours.append(Cours(
    semaine[5] + " " + year + " 9:00",
    semaine[5] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_matin")).get_text() ))

    cours.append(Cours(
    semaine[5] + " " + year + " 13:30",
    semaine[5] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_apres_midi")).get_text() ))

    return cours

def getYear(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ligne = soup.find('select', id=re.compile("Planning_stage1_select_semaine")).find('option', selected=True)
    year = ligne.get_text()
    year = year[-5:] # avoir les 5 dernier caractère : 2019) ou 2020)
    year = year[:4] # enleve les parentheses
    return year

def getDayOfWeek(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ligne = soup.find('table', id=re.compile(    "Planning_stage1_tab_emploi_du_temps_semaine")).find('tr')
    ligne = ligne.find_all('td')

    semaine = []
    for col in ligne:
        semaine.append(col.text)

    return semaine
 
def get_cal():
    formatter = logging.Formatter(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    
    logger.info('--------------------------------')
    now = datetime.now()
    debutTraitement = datetime.now().astimezone(timezone('Europe/Paris'))

    logger.info("🔽  Scrap prepare")

    url = "http://www.ipst-info.net/consultation/default_stage.aspx?stage=aisl"

    try:
        r = requests.head(url)
        if r.status_code != 200: 
            logger.error('⛔️ Site injoignable')
            sys.exit()
    except requests.ConnectionError:
        logger.error('⛔️ failed to connect')
        sys.exit()

    # create a new Firefox session
    #driver = webdriver.Firefox()
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX
    )
    driver.implicitly_wait(30)
    driver.get(url)

    cours = []

    #calcul nombre de semaine avant la fin de l'année
    finAnnee = dateparser.parse("30 octobre 2020 17:00")
    today = datetime.now()

    monday1 = (today - timedelta(days=today.weekday()))
    monday2 = (finAnnee - timedelta(days=finAnnee.weekday()))

    numberOfWeekUntilEndOfYear = int(((monday2 - monday1).days / 7) + 1)
    
    logger.info("⏺  Scrap started")
    for i in range(numberOfWeekUntilEndOfYear):
        year = getYear(driver)
        week = getDayOfWeek(driver)        
        cours = scrapCours(driver, cours, year, week)

        #click
        python_button = driver.find_element_by_id('Planning_stage1_semaine_suivante')
        python_button.click() 
        time.sleep(.300) # pour que la page est le temps de charger

    driver.quit()

    cal = Calendar()
    cal.add("summary", "Calendrier Cnam I2")
    cal.add('version', '2.0')

    for cour in cours :
        dateDebut = dateparser.parse(cour.dateDebut)
        dateFin = dateparser.parse(cour.dateFin)

        if 'En entreprise' not in cour.matiere and  'nondéfini' not in cour.matiere and 'Férié' not in cour.matiere:
            event = Event()
            event.add('dtstart', dateDebut)
            event.add('dtend', dateFin)
            
            # si je veux garder les jour entreprise, férié et non défini
            # if 'En entreprise' in cour[2] or  'nondéfini' in cour[2] or 'Férié' in cour[2]:
            #     matiere = cour.matiere
            # else: 
            matiere = cour.matiere[:6] + " " + cour.matiere[6:]

            event.add('summary', matiere) 

            desc =  "Enseignant : " + cour.enseignant
            desc += "\nCommentaire : " + cour.commentaire
            desc += "\n\nDate de scan : " + datetime.now().strftime("%d/%m/%Y %H:%M")
            event.add('description', desc ) 
            
            event.add('url', "http://www.ipst-info.net/consultation/default_stage.aspx?stage=aisl")
            
            
            cal.add_component(event)
    
    logger.info("⏺  Scrap ended")

    #comparaison avec le dernier calendrier enregistré
    
    #on tranforme le cal en text et on enlève les \r pour la comparaison avec fichier enregistrer (\r en trop)
    # print(repr(calText)) #pour afficher les \n et \r

    calText = cal.to_ical().decode("utf-8").split("\r")
    calText = ''.join(calText)

    # on recupere le dernier fichier recupéré
    calendarLast = open('/home/scraper/last/calendarCnamI2.ics')
    calendarLastText = calendarLast.read()

    cal1 = Calendar.from_ical(calendarLastText).walk()
    cal2 = Calendar.from_ical(calText).walk()

    save = False
    # si la longueur des cal ≠ : sauvegarde
    if( len(cal1) != len(cal2)):
        save = True
        logger.info('⏺  Sauvegarde : size ≠')
    else:
        # element 0 = tout le calendrier
        for i in range(1, len(cal1)):
            # si les startdate ≠ ou resumé ≠ : sauvegare
            if( cal1[i].get('dtstart').dt != cal2[i].get('dtstart').dt or cal1[i].get('summary') != cal2[i].get('summary')):
                logger.info("⏺  Sauvegarde : content ≠")
                save = True
                break

   
    if save:
        logger.info("✅  Enregistrement du nouveau ics : ")

        # sauvegarde du .ics historique
        dateForIcsName = today.strftime('%Y-%m-%d_%H:%M')
        with open('/home/scraper/history/calendarCnamI2'+ dateForIcsName +'.ics', 'wb') as f:
            f.write(cal.to_ical())
            f.close
            logger.info('❕  /home/scraper/history/calendarCnamI2' + dateForIcsName +'.ics Saved')

        # ecrasement de l'ancien sauvegarde du nouveau
        with open('/home/scraper/last/calendarCnamI2.ics', 'wb') as f:
            f.write(cal.to_ical())
            f.close
            logger.info("❕  /home/scraper/last/calendarCnamI2.ics Saved")

    else:
        logger.info("❎  Nouveau calendrier identique au précédent, pas de sauvegarde")

    finTraitement = datetime.now().astimezone(timezone('Europe/Paris'))
    logger.info('⏺  End')

    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(finTraitement.strftime("%H:%M:%S"), FMT) - datetime.strptime(debutTraitement.strftime("%H:%M:%S") , FMT)
    logger.info('⏺  Durée : ' +  str(tdelta))
    logger.info('--------------------------------')

    return cal
