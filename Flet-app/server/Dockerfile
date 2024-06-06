FROM python:3.12

ADD main.py /server/

RUN pip install flet

WORKDIR /server/

CMD [ "python", "./main.py" ]

EXPOSE 80