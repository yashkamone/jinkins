FROM python:3.9.21-alpine
WORKDIR /src
COPY . .
RUN pip3 install flask
EXPOSE 4000
CMD python3 server.py