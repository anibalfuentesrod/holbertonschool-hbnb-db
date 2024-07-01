# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-alpine

# Set environment variables to prevent Python from writing pyc files to disc
# and to prevent Python from buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add --no-cache postgresql-dev

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy project
COPY . /app
WORKDIR /app

# Expose port 5002 for the Flask app
EXPOSE 5002

# Run the Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5002", "hbnb:app"]