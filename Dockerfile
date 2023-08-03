#use pyhton image 
FROM python:3.11.3

#working directory
WORKDIR /app

#copy the file form main
COPY . /app

#installing library
RUN pip install -r requirements.txt

#rest api will run on 5000
EXPOSE 8000

#command to run
CMD ["flask","run"]