FROM python:3.7.2-alpine3.9

#Install gcc, musl-dev & make (needed for building python wheels)
RUN apk add gcc musl-dev make

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
