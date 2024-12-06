FROM python:3.13

ENV PYTHONPATH=/APP

WORKDIR /APP

COPY ./requirements.txt /APP/

RUN pip install -r /APP/requirements.txt 

COPY ./spell_check /APP/spell_check

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["/APP/spell_check/src/app.py"]


