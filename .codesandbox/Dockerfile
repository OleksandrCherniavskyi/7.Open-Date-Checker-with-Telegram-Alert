# Base image
FROM ubuntu:latest

# Update and upgrade the system
RUN apt-get update && apt-get upgrade -y

# Install required packages
RUN apt-get install -y python3-pip python3-venv

# Set the working directory
WORKDIR /workspace

# Set up a virtual environment
RUN python3 -m venv /workspace/venv

# Activate the virtual environment
ENV PATH="/workspace/venv/bin:$PATH"

RUN /workspace/venv/bin/pip install --upgrade pip

# Copy requirements.txt file to the container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN /workspace/venv/bin/pip install -r requirements.txt

# Copy the main.py file to the container
COPY main.py .

# Set the entry point to run the main.py script
CMD ["python", "main.py"]