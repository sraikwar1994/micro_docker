# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define environment variable
ENV NAME app_3

# Run main.py when the container launches
CMD ["python", "main.py"]