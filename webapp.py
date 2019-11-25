
from flask import Flask, request, make_response
from icalendar import Calendar, Event
from edtScraping import get_cal

app = Flask(__name__)

@app.route('/scrap')
def launch_scrap():
    get_cal()
    return "Done"


@app.route('/ics')
def get_ics_file():
    try:
        with open('last/calendarCnamI2.ics', 'w') as calendarCnamFile:
          text = calendarCnamFile  
    except Exception as e:
        cal = Calendar()
        cal.add("summary", "Imported from Cnam edt, but failed.")
        cal.add('version', '2.0')
        text = cal.to_ical()
        print("error /ics")
    
    res = make_response(text)
    res.headers.set('Content-Disposition', 'attachment;filename=calendar.ics')
    res.headers.set('Content-Type', 'text/calendar;charset=utf-8')
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000, debug=True)