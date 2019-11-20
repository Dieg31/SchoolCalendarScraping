from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time
from icalendar import Calendar, Event
import locale
import dateparser # $ pip install dateparser

def ucours(dateDebut, dateFin, matiere, enseignant, commentaire):
    uncours = []
    uncours.append(dateDebut)
    uncours.append(dateFin)
    uncours.append(matiere)
    uncours.append(enseignant)
    uncours.append(commentaire)
    return uncours


#launch url
url = "http://www.ipst-info.net/consultation/default_stage.aspx?stage=aisl"

# create a new Firefox session

#driver = webdriver.Firefox()
driver = webdriver.Remote(
   command_executor='http://172.17.0.2:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)
driver.implicitly_wait(30)
driver.get(url)

# date matiere enseignant commentaire
cours = []

for i in range(20):


    #get year
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ligne = soup.find('select', id=re.compile("Planning_stage1_select_semaine")).find('option', selected=True)
    year = ligne.get_text()
    year = year[-5:] # avoir les 5 dernier caractère : 2019) ou 2020)
    year = year[:4] # enleve les parentheses

    #get week
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ligne = soup.find('table', id=re.compile(    "Planning_stage1_tab_emploi_du_temps_semaine")).find('tr')
    ligne = ligne.find_all('td')
    semaine = []

    for col in ligne:
        semaine.append(col.text)

    #get data
    soup = BeautifulSoup(driver.page_source, 'lxml')

    cours.append(ucours(
    semaine[1] + " " + year + " 9:00",
    semaine[1] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_matin")).get_text() ))

    cours.append(ucours(
    semaine[1] + " " + year + " 13:30",
    semaine[1] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_apres_midi")).get_text() ))

    cours.append(ucours(
    semaine[2] + " " + year + " 9:00",
    semaine[2] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_matin")).get_text() ))

    cours.append(ucours(
    semaine[2] + " " + year + " 13:30",
    semaine[2] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_apres_midi")).get_text() ))

    cours.append(ucours(
    semaine[3] + " " + year + " 9:00",
    semaine[3] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_matin")).get_text() ))

    cours.append(ucours(
    semaine[3] + " " + year + " 13:30",
    semaine[3] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_apres_midi")).get_text() ))

    cours.append(ucours(
    semaine[4] + " " + year + " 9:00",
    semaine[4] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_matin")).get_text() ))

    cours.append(ucours(
    semaine[4] + " " + year + " 13:30",
    semaine[4] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_apres_midi")).get_text() ))

    cours.append(ucours(
    semaine[5] + " " + year + " 9:00",
    semaine[5] + " " + year + " 12:30", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_matin")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_matin")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_matin")).get_text() ))

    cours.append(ucours(
    semaine[5] + " " + year + " 13:30",
    semaine[5] + " " + year + " 17:00", 
    soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_apres_midi")).get_text(),
    soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_apres_midi")).get_text() ))
   
   #click
    python_button = driver.find_element_by_id('Planning_stage1_semaine_suivante')
    python_button.click() 
    time.sleep(.300) # pour que la page est le temps de charge

    print("------------------------------------- semaine", i)
    for l in cours :
        print("")
        print("", l)
        

print("fin")

print("creation calendrier")

#pour parser des dates en français
#locale.setlocale(locale.LC_ALL, 'fr_FR')

cal = Calendar()
cal.add("summary", "Calendrier Cnam I2")
cal.add('version', '2.0')

for c in cours :
    
    dateDebut = dateparser.parse(c[0])
    dateFin = dateparser.parse(c[1])

    if 'En entreprise' not in c[2] and  'nondéfini' not in c[2] and 'Férié' not in c[2]:
        event = Event()
        event.add('dtstart', dateDebut)
        event.add('dtend', dateFin)
        
        if 'En entreprise' in c[2] or  'nondéfini' in c[2] or 'Férié' in c[2]:
            matiere = c[2]
        else: 
            matiere = c[2][:6] + " " + c[2][6:]

        event.add('summary', matiere) #matiere
        event.add('description', 'Enseignant : ' + c[3] + "\nCommentaire : " + c[4]) #enseignant + commentaire
        cal.add_component(event)
        print(c[2])
    # if 'En entreprise' in c[2] or  'nondéfini' in c[2] or 'Férié' in c[2]:
    #         print('---------------pasCours')

with open('calendarCnamI2.ics', 'wb') as f:
    f.write(cal.to_ical())
    f.close


###################################################################################@

    # print("lundi matin enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_matin")).get_text() )
    # print("lundi matin matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_matin")).get_text() )
    # print("lundi matin commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_matin")).get_text() )
    # print("")
    # print("lundi après midi enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_lundi_apres_midi")).get_text() )
    # print("lundi après midi matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_lundi_apres_midi")).get_text() )
    # print("lundi après midi commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_lundi_apres_midi")).get_text() )
    # print("")
    # print("mardi matin enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_matin")).get_text() )
    # print("mardi matin matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_matin")).get_text() )
    # print("mardi matin commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_matin")).get_text() )
    # print("")
    # print("mardi après midi enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mardi_apres_midi")).get_text() )
    # print("mardi après midi matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mardi_apres_midi")).get_text() )
    # print("mardi après midi commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mardi_apres_midi")).get_text() )
    # print("")
    # print("mercredi matin enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_matin")).get_text() )
    # print("mercredi matin matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_matin")).get_text() )
    # print("mercredi matin commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_matin")).get_text() )
    # print("")
    # print("mercredi après midi enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_mercredi_apres_midi")).get_text() )
    # print("mercredi après midi matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_mercredi_apres_midi")).get_text() )
    # print("mercredi après midi commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_mercredi_apres_midi")).get_text() )
    # print("")
    # print("jeudi matin enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_matin")).get_text() )
    # print("jeudi matin matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_matin")).get_text() )
    # print("jeudi matin commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_matin")).get_text() )
    # print("")
    # print("jeudi après midi enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_jeudi_apres_midi")).get_text() )
    # print("jeudi après midi matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_jeudi_apres_midi")).get_text() )
    # print("jeudi après midi commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_jeudi_apres_midi")).get_text() )
    # print("")
    # print("vendredi matin enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_matin")).get_text() )
    # print("vendredi matin matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_matin")).get_text() )
    # print("vendredi matin commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_matin")).get_text() )
    # print("")
    # print("vendredi après midi enseignant  : ",  soup.find('span', id=re.compile(    "Planning_stage1_label_matiere_vendredi_apres_midi")).get_text() )
    # print("vendredi après midi matière     : ",  soup.find('span', id=re.compile( "Planning_stage1_label_enseignant_vendredi_apres_midi")).get_text() )
    # print("vendredi après midi commentaire : ",  soup.find('span', id=re.compile("Planning_stage1_label_commentaire_vendredi_apres_midi")).get_text() )
    # print("")


#######################################################################@
#     Planning_stage1_label_matiere_lundi_matin
#  Planning_stage1_label_enseignant_lundi_matin
# Planning_stage1_label_commentaire_lundi_matin 

#     Planning_stage1_label_matiere_lundi_apres_midi
#  Planning_stage1_label_enseignant_lundi_apres_midi
# Planning_stage1_label_commentaire_lundi_apres_midi


#     Planning_stage1_label_matiere_mardi_matin
#  Planning_stage1_label_enseignant_mardi_matin
# Planning_stage1_label_commentaire_mardi_matin 

#     Planning_stage1_label_matiere_mardi_apres_midi
#  Planning_stage1_label_enseignant_mardi_apres_midi
# Planning_stage1_label_commentaire_mardi_apres_midi

#     Planning_stage1_label_matiere_mercredi_matin
#  Planning_stage1_label_enseignant_mercredi_matin
# Planning_stage1_label_commentaire_mercredi_matin 

#     Planning_stage1_label_matiere_mercredi_apres_midi
#  Planning_stage1_label_enseignant_mercredi_apres_midi
# Planning_stage1_label_commentaire_mercredi_apres_midi

#     Planning_stage1_label_matiere_jeudi_matin
#  Planning_stage1_label_enseignant_jeudi_matin
# Planning_stage1_label_commentaire_jeudi_matin 

#     Planning_stage1_label_matiere_jeudi_apres_midi
#  Planning_stage1_label_enseignant_jeudi_apres_midi
# Planning_stage1_label_commentaire_jeudi_apres_midi

#     Planning_stage1_label_matiere_vendredi_matin
#  Planning_stage1_label_enseignant_vendredi_matin
# Planning_stage1_label_commentaire_vendredi_matin 

#     Planning_stage1_label_matiere_vendredi_apres_midi
#  Planning_stage1_label_enseignant_vendredi_apres_midi
# Planning_stage1_label_commentaire_vendredi_apres_midi