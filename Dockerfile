FROM ubuntu
RUN mkdir Market
RUN apt-get update
RUN apt-get -y install python3-pip
WORKDIR Market
COPY . / Market/
RUN pip install -r Market/requirements.txt
CMD ['python manage.py runserver 8081']
