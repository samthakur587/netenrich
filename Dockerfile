# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY  requirement.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test.py file to the container
COPY test.py .

# Expose the port on which your FastAPI app listens (if applicable)
EXPOSE 8000

# Set the entrypoint command to run your FastAPI app
CMD ["uvicorn", "test:app","--reload"]
