# Use an official Python runtime as a parent image
FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
# Set the working directory to /app
#RUN apk add --no-cache curl make gcc libc-dev linux-headers musl-dev tk-dev tcl-dev openssl-dev libffi-dev mysql-client mariadb-dev python3-dev jpeg-dev zlib-dev freetype-dev lcms2-dev tiff-dev openjpeg-dev


RUN mkdir /app
WORKDIR /app
COPY . .

RUN python3 setup.py install
RUN python3 /app/manage.py makemigrations && python3 /app/manage.py migrate

# Make port 8080 available to the world outside this container
EXPOSE 3000

ENTRYPOINT ["python3", "/app/manage.py", "runserver", "0.0.0.0:3000"]