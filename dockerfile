FROM python:3.13

ENV PYTHONPATH=/APP/src/spell_check:$PYTHONPATH

WORKDIR /APP

COPY ./requirements.txt /APP/

RUN pip install -r /APP/requirements.txt 

COPY ./spell_check /APP

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["src/app.py"]


