FROM python:3.10


WORKDIR /app
COPY pod-usage-web-eks.py /app/
COPY requirements.txt /tmp/

RUN pip3 install --requirement /tmp/requirements.txt 

EXPOSE 8000
CMD ["python3", "/app/pod-usage-web-eks.py"]
