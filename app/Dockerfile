FROM python:3.8.2-buster

WORKDIR /

COPY . /

EXPOSE 3000 3000

RUN pip install --upgrade pip &&  pip install -r requirements.txt

CMD ["python", "app.py"]