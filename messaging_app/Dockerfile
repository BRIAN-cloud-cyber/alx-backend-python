FROM python:3.10
#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app 

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . . 


EXPOSE 8000

#command to run on container start
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

