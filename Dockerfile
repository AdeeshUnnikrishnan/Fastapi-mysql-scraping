# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        default-libmysqlclient-dev \
        python3-dev \
        chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

EXPOSE 8081

# Set the entrypoint command
CMD ["uvicorn", "app.api.endpoints:app", "--host=0.0.0.0", "--port=8081"]
