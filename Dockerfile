# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY  requirement.txt .

RUN pip install --upgrade pip

# Install the Python dependencies
RUN pip install -r requirement.txt

# Copy the test.py file to the container
COPY test.py .



# Set the entrypoint command to run your FastAPI app
CMD ["uvicorn", "test:app","--reload"]
