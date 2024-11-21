FROM python:3.13

WORKDIR /APP

COPY ./requirements.txt /APP/

RUN pip install -r /APP/requirements.txt 

COPY ./spell_check /APP

ENV HOST_IP=0.0.0.0
ENV IMAGE_PORT_NUM=5000

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]


