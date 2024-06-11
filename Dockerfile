# Your Python version
FROM python:3.10 as taipy

# Web port of the application
EXPOSE 5000

# Create taipy user for security
RUN groupadd -r taipy && useradd -r -m -g taipy taipy
USER taipy

# Go to the dedicated folder and add the python corresponding folder in PATH
WORKDIR /home/taipy
ENV PATH="${PATH}:/home/taipy/.local/bin"

# Update pip and install Gunicorn with a suitable worker
RUN python -m pip install --upgrade pip
RUN python -m pip install gunicorn gevent-websocket

# Install your application
COPY app/ .
RUN python -m pip install -r requirements.txt

# Start up command
CMD [ "gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind=0.0.0.0:5000", "--timeout", "1800", "--module", "main:web_app " ]
#CMD [ "main:run" ]