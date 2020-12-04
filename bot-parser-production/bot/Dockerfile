# Dockerfile
# Pull base image
FROM python:3.8.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD ./app /app
ADD ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["python3", "run.py"]
