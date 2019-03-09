FROM python:3.7.2-alpine3.9

COPY data/* /app/data/
COPY helper/* /app/helper/
COPY images/* /app/images/
COPY *.py /app/
COPY requirements.txt /app/

#RUN cd /app && ./install_packages.sh

RUN cd /app && pip install -r requirements.txt
