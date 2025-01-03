# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory's contents into the container
COPY . .

# Install the dependencies
RUN pip install flask werkzeug jwt datetime

# Expose the service's port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
