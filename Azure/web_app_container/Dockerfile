FROM python:3.10.16-alpine3.21

RUN python -m pip install flask
RUN python -m pip install sqlalchemy
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN python -m pip install psycopg2

COPY flaskr /root/flaskr

ENV FLASK_ENV=development
ENV FLASK_APP=flaskr

CMD ["/bin/sh", "-c", "cd /root && python -m flask run --host=0.0.0.0"]
