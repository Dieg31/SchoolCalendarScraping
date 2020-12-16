FROM python:3
WORKDIR /home/scraper/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calScraping.py calScraping.py
COPY showScrapLog.sh showScrapLog.sh

RUN apt-get update
RUN apt-get install -y cron 
COPY crontab-edt-scrap /etc/cron.d/crontab-edt-scrap
RUN chmod 0644 /etc/cron.d/crontab-edt-scrap
RUN crontab /etc/cron.d/crontab-edt-scrap
RUN touch /var/log/scraper.log
RUN cron

# ENTRYPOINT ["python3", "webapp.py", ">>", "/var/log/scraperApi.log", "2>&1"]
CMD ["tail", "-f", "/var/log/scraper.log"]
# ENTRYPOINT python3 webapp.py >> /var/log/scraperApi.log 2>&1 