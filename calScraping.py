from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import re
import os
import time
from icalendar import Calendar, Event
import dateparser # $ pip install dateparser
from datetime import datetime, timedelta

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
    now = datetime.now()
    print("edtScraping ", now.strftime("%d/%m/%Y %H:%M"))
    
    url = "http://www.ipst-info.net/consultation/default_stage.aspx?stage=aisl"

    # create a new Firefox session
    #driver = webdriver.Firefox()
    driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)
    driver.implicitly_wait(30)
    driver.get(url)

    cours = []

    #calcul nombre de semaine avant la fin de l'année
    finAnnee = dateparser.parse("30 octobre 2020 17:00")
    today = datetime.now()

    monday1 = (today - timedelta(days=today.weekday()))
    monday2 = (finAnnee - timedelta(days=finAnnee.weekday()))

    numberOfWeekUntilEndOfYear = int(((monday2 - monday1).days / 7) + 1)

    print("Scrap starting ...")
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
            event.add('description', 'Enseignant : ' + cour.enseignant + "\nCommentaire : " + cour.commentaire) 
            cal.add_component(event)
    
    print("Scrap end")

    # sauvegarde du .ics historique
    dateForIcsName = today.strftime('%Y-%m-%d_%H:%M')
    with open('/home/scraper/vol/history/calendarCnamI2'+ dateForIcsName +'.ics', 'wb') as f:
        f.write(cal.to_ical())
        f.close
        print('/home/scraper/vol/history/calendarCnamI2' + dateForIcsName +'.ics Saved')


    # ecrasement de l'ancien sauvegarde du nouveau
    with open('/home/scraper/vol/last/calendarCnamI2.ics', 'wb') as f:
        f.write(cal.to_ical())
        f.close
        print("/home/scraper/vol/last/calendarCnamI2.ics Saved")


    return cal

get_cal()