FROM python:3
WORKDIR /home/test/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY calScraping.py calScraping.py
COPY webapp.py webapp.py

EXPOSE 5000

RUN mkdir last
RUN mkdir history

CMD [ "python3", "./webapp.py" ]
