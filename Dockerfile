# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY . .

# Expose both ports: 5000 (admin) and 8080 (user)
EXPOSE 5000
EXPOSE 8080

# Start both servers with gunicorn, one on port 5000 and one on 8080
CMD gunicorn --workers=1 --bind 0.0.0.0:5000 app:app & gunicorn --workers=1 --bind 0.0.0.0:8080 app:app
