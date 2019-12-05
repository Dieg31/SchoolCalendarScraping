FROM python:3-alpine

RUN pip3 install --no-cache-dir flask

RUN pip3 install --no-cache-dir flask icalendar

WORKDIR /home/python/

COPY index.py /home/python/

CMD ["python", "/home/python/index.py"]
