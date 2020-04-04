FROM python:3
WORKDIR /home/scraper/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calScraping.py calScraping.py
COPY webapp.py webapp.py

# RUN apt-get install -y cron 
# COPY crontab-edt-scrap /etc/cron.d/crontab-edt-scrap
# RUN chmod 0644 /etc/cron.d/crontab-edt-scrap
# RUN crontab /etc/cron.d/crontab-edt-scrap
# RUN touch /var/log/crontab-edt-scrap.log
# RUN cron

EXPOSE 5000

CMD [ "python3", "./webapp.py" ]
