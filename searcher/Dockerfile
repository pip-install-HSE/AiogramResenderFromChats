# Dockerfile
# Pull base image
FROM python:3.8.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD ./app /app
ADD ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD ["python3", "./main.py"]
