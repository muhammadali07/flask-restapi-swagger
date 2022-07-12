
FROM python:3.8


COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt


WORKDIR /app

# ENV FLASK_APP=/app/main
# ENV FLASK_DEBUG=1
# ENV FLASK_ENV=development

# EXPOSE 5001:5000

# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["python", "main.py"]