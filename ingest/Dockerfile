# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory (ingest) into the container
COPY . .

# Set the command to run the ingestion script
CMD ["python", "ingest/ingest.py"]
