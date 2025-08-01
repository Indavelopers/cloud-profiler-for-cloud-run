# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10

# Set environment variables for Python and the application.
ENV PYTHONUNBUFFERED=True
WORKDIR /app

# Install production dependencies.
# We copy the requirements file first to leverage Docker's layer caching.
# This means Docker will only re-run this step if requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code.
COPY . .

# Run the web service on container startup.
# Gunicorn is a production-ready WSGI server.
# The --bind :$PORT flag tells Gunicorn to listen on all IP addresses
# on the port specified by the PORT environment variable, which Cloud Run sets.
# We use `exec` to ensure Gunicorn runs as PID 1 and receives signals correctly.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 120 --access-logfile - main:app
