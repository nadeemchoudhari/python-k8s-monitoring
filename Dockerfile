FROM nach1116/python-web:v1


WORKDIR /app
COPY pod-usage-web.py /app/

EXPOSE 8000
CMD ["python3", "/app/pod-usage-web.py"]
