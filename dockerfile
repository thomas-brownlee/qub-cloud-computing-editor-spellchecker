FROM python:3.13

WORKDIR /APP

COPY ./ /APP/
COPY ./requirement.txt /APP/

#RUN "pip install -r /APP/requirement.txt" 

#EXPOSE 5000

#ENTRYPOINT ["python3"]
#CMD ["app.py"]


