FROM python:2.7-alpine3.7
WORKDIR /usr/src/app
ADD app.py .
EXPOSE 8080
CMD ["python", "-u", "app.py"]
