FROM python:3.7

WORKDIR /home/application

COPY requirements.txt requirements.txt
COPY app.py ./

ENV FLASK_APP app.py
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn" , "-b", "0.0.0.0:8000", "app:app"]
