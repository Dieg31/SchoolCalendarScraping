FROM python:3

RUN pip3 install --no-cache-dir bs4 dateparser icalendar lxml selenium

WORKDIR /home/python/

COPY scrapper.py /home/python/

CMD ["python3", "/home/python/scrapper.py"]
