# Base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt

# Installs all Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (Flask default is 5000)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
