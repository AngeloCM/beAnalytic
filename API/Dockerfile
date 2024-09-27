# Base image
FROM python:3.12

# Set working directory
WORKDIR /code

# Copy only requirements.txt first to leverage caching
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy application code and models
COPY ./app /code/app
COPY models /code/models

# Expose the port Uvicorn will run on
EXPOSE 8080

# Start Uvicorn server
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8080"]