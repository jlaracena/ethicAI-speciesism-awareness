# Multi-stage Dockerfile for FastAPI + Streamlit
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose ports for both services (though Cloud Run usually only exposes one)
# We will use a startup script to run both
EXPOSE 8000
EXPOSE 8501

# Scripts for execution
RUN echo '#!/bin/bash\nuvicorn backend.main:app --host 0.0.0.0 --port 8000 & \nstreamlit run frontend/app.py --server.port 8080 --server.address 0.0.0.0' > start.sh
RUN chmod +x start.sh

# Cloud Run uses PORT env var, we'll map streamlit to it
CMD ["./start.sh"]
