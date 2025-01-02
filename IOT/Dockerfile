# Use the official Python slim image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=IOT.settings

# Upgrade pip
RUN pip install --upgrade pip

# Set environment variable for Django
# ENV DJANGO_SETTINGS_MODULE=IOT.settings

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file to leverage Docker cache
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port for Daphne
EXPOSE 8000

# Command to run Daphne for WebSockets
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "IOT.asgi:application"]
