# Dockerfile
FROM python:3.11

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure start.sh is executable
RUN chmod +x start.sh

# Cloud Run uses PORT environment variable
EXPOSE 8080

CMD ["./start.sh"]
