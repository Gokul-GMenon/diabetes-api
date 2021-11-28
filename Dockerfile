# FROM python:3.8.1

# ENV APP_HOME /app
# WORKDIR $APP_HOME

# COPY . /app

# RUN pip install -r requirements.txt

# ENTRYPOINT ["python model_api.py"]
FROM python:3.8.1-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "model_api.py"]