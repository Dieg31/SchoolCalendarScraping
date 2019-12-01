FROM python:3
WORKDIR /home/scraper/

RUN apt-get -y update && apt-get -y upgrade


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calScraping.py calScraping.py
COPY webapp.py webapp.py


RUN apt-get install -y cron 
RUN touch /var/log/crontab-edt-scrap.log
COPY crontab-edt-scrap /etc/cron.d/crontab-edt-scrap
RUN chmod 0644 /etc/cron.d/crontab-edt-scrap
RUN cron

EXPOSE 5000

RUN  bash -c 'mkdir -p vol/last'
RUN  bash -c 'mkdir -p vol/history'

CMD [ "python3", "./webapp.py" ]
