FROM python:3
WORKDIR /home/scraper/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["tail", "-f", "/dev/null"]