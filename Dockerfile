FROM python:3.11.5


SHELL ["/bin/bash", "-c"] 

WORKDIR /DENTAL_CRM

COPY requirements.txt /DENTAL_CRM/
RUN pip install -r requirements.txt

COPY . /DENTAL_CRM/