FROM python:3.7-slim

#Install libs and tools needed for building python wheels
RUN apt-get update
RUN yes | apt-get install build-essential
RUN yes | apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN yes | apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev

#Install python dependencies
COPY requirements.txt /app/
RUN cd /app && pip install -r requirements.txt

#Copy application to /app
COPY data/* /app/data/
COPY helper/* /app/helper/
COPY images/* /app/images/
COPY *.py /app/

#Change working directory to /app
WORKDIR /app

#Run server
ENTRYPOINT [ "python", "server.py" ]
