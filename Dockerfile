FROM python:3
WORKDIR /home/test/

RUN apt-get -y update && apt-get -y upgrade


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calScraping.py calScraping.py
COPY webapp.py webapp.py

RUN apt-get install -y cron 
RUN touch /var/log/crontab-edt-scrap.log
COPY crontab-edt-scrap /etc/cron.d/crontab-edt-scrap
RUN chmod 0644 /etc/cron.d/crontab-edt-scrap

EXPOSE 5000

RUN mkdir last
RUN mkdir history
CMD ./start.sh
