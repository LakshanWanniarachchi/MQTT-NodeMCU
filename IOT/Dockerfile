# Use the official Python image from the Docker Hub
FROM python:3.9

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Install Gunicorn
RUN pip install gunicorn

# Expose the port Gunicorn will run on
EXPOSE 8000

# Command to run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "IOT.wsgi:application"]
# CMD ["gunicorn", "--config", "gunicorn.conf.py", "IOT.wsgi:application"]