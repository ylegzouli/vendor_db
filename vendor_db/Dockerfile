# Use an official Python runtime as a base image
FROM python:3.9

# Sets the container's working directory to /app
WORKDIR /app

# Copies the local requirements.txt file to the container
COPY requirements.txt ./

# Installs the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copies the local app directory to the container
COPY . ./app

# Exposes port 8000 to other Docker containers, not to the host
EXPOSE 8000

# The command to run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
