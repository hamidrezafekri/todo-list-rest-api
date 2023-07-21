FROM python:3.10 AS cache

WORKDIR /srv
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

FROM cache AS build

COPY . .

FROM build

EXPOSE 8000

CMD python manage.py migrate  && python manage.py runserver 0.0.0.0:8000
