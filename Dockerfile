# Dockerfile

FROM python:3.11-slim

# Prevent .pyc files & enable logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Entrypoint to run migrations & server
ENTRYPOINT ["./entrypoint.sh"]
