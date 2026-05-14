FROM python:3.10-alpine

ENV FLASK_APP=masini
ENV VIRTUAL_ENV=/home/masini/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN adduser -D masini
WORKDIR /home/masini

COPY quickrequirements.txt .
COPY masini.py .
COPY pytest.ini .
COPY dockerstart.sh .
COPY app app

RUN python3 -m venv "$VIRTUAL_ENV" \
    && "$VIRTUAL_ENV/bin/pip" install --no-cache-dir -r quickrequirements.txt \
    && chmod +x dockerstart.sh

USER masini

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh