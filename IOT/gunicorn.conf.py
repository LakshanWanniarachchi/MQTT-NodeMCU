# gunicorn.conf.py
bind = "0.0.0.0:8000"
workers = 4  # Adjust the number of workers based on your application's needs
accesslog = "-"  # Log access to stdout
errorlog = "-"  # Log errors to stdout
loglevel = "info"
