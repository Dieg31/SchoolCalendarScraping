FROM python:3
WORKDIR /root/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY edtScraping.py edtScraping.py

EXPOSE 5000