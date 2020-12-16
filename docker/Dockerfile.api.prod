FROM python:3
WORKDIR /home/scraper/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY webapp.py webapp.py
COPY calScraping.py calScraping.py
COPY showScrapApiLog.sh showScrapApiLog.sh

EXPOSE 5000

# ENTRYPOINT ["python3", "webapp.py", ">>", "/var/log/scraperApi.log", "2>&1"]
# CMD ["tail", "-f", "/var/log/scraperApi.log"]
CMD python3 webapp.py >> /var/log/scraperApi.log 2>&1 