FROM python:3.6

RUN mkdir -p /flask-app
WORKDIR /flask-app


# Install packages
RUN pip install flask
RUN pip install psycopg2

# Run flask app
EXPOSE 5000
ENV FLASK_APP="src/main.py" FLASK_DEBUG=1 FLASK_ENV=docker
CMD ["flask", "run", "-h", "127.0.0.1"]