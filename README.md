edtScraping.py 
A script to scrap my shool's calendar

webapp.py 
A webapp to create a flux


To build images :
```
docker build -t cal-scrap-app .
```

To run applications :
```
docker-compose -f app.yml up
```

To see cron log :
```
tail -f /var/log/crontab-edt-scrap.log
```