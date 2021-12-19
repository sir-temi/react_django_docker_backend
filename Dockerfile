FROM python:3.8-slim

# enable logging to container interface
ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

# dir where all excutives will be ran
WORKDIR /app

# uodate the linux server
RUN apt-get update
RUN apt-get upgrade

COPY requirements.txt /app

RUN pip install --upgrade pip

# install requirements
RUN pip3 install -r requirements.txt

# copy all in root directory to app folder in container
COPY . /app


# RUN python3 manage.py migrate && python3 manage.py makemigrations

# expose port
# EXPOSE 8000

# do not use run again, use CMD for what you want executed
# when you start container
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tifesallure.wsgi"
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]






