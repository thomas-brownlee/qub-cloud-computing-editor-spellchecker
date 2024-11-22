FROM python:3.13

WORKDIR /APP

COPY ./requirements.txt /APP/

RUN pip install -r /APP/requirements.txt 

COPY ./spell_check /APP

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]


