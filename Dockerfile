# Start with a Python 3.11 slim base image
FROM python:3.11-slim

# Set environment variables for better container performance
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install SQLite3 for direct database inspection if needed
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Create an empty SQLite database file and set permissions
RUN touch /app/db.sqlite3 && chmod 666 /app/db.sqlite3


# Run Django commands to set up the application
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput


# Expose port 8001 for Django or Gunicorn to listen on inside the container
EXPOSE 8001

# Run Gunicorn, a WSGI HTTP server for running Django in production
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "portfolio_backend.wsgi:application"]