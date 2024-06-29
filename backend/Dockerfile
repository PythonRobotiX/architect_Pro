# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory contents into the container
COPY backend/ /app/backend

# Copy the config.py into the container
COPY backend/config.py /app/config.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run database migrations before starting the server
CMD ["sh", "-c", "flask db upgrade && gunicorn --bind 0.0.0.0:5000 backend.app:app"]
