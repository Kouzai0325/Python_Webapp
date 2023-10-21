# syntax=docker/dockerfile:1
From python:3.10-slim-buster
Workdir /app
Copy requirements.txt requirements.txt
Run pip3 install -r requirements.txt
Copy static static
Copy templates templates
Copy app.py app.py
Copy test_db test_db
Copy test_model.py test_model.py
CMD [ "python3","-m","flask","run","--host=0.0.0.0" ]