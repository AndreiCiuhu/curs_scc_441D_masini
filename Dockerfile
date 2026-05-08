FROM python:3.10-alpine

ENV FLASK_APP masini
RUN adduser -D masini

USER masini

WORKDIR /home/masini/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY masini.py masini.py
RUN mkdir static
RUN mkdir static/imagini
RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/masini/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh