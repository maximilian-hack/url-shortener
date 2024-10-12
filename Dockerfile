# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
