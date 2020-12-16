
from flask import Flask, request, make_response
from icalendar import Calendar, Event
from calScraping import get_cal
import os.path
import logging
from datetime import datetime

app = Flask(__name__)
logger = logging.getLogger('scraperApi')
hdlr = logging.FileHandler('/var/log/scraperApi.log')
formatter = logging.Formatter(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ' %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)


@app.route('/scrap')
def launch_scrap():
    """
        To launch website scraping manually
    """
    get_cal()
    return "Done"


@app.route('/ics')
def get_ics_file():
    """
        To get last ics file with lastest datas
    """
    try:
        with open('/home/scraper/last/calendarCnamI2.ics') as calendarCnamFile:
            text = calendarCnamFile.read()

    except Exception as e:
        cal = Calendar()
        cal.add("summary", "Imported from Cnam edt, but failed.")
        cal.add('version', '2.0')
        text = cal.to_ical()
        logger.error("error /ics")

    
    res = make_response(text)
    res.headers.set('Content-Disposition', 'attachment;filename=calendar.ics')
    res.headers.set('Content-Type', 'text/calendar;charset=utf-8')

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000, debug=True)