FROM python:3.10


WORKDIR /app
COPY pod-usage-web-v2.py /app/
COPY requirements.txt /tmp/

RUN pip3 install --requirement /tmp/requirements.txt 


CMD ["python3", "/app/pod-usage-web-v2.py"]
