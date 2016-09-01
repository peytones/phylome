FROM ubuntu


RUN apt-get update

RUN apt-get install -y python python-dev python-pip

RUN pip install flask && pip install biopython && pip install ete2 && pip install cherrypy

EXPOSE 80

ADD /app /app

WORKDIR /app

CMD python server.py
