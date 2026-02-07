FROM python:3.12-slim

# Install system dependencies first
RUN apt-get update && \
    apt-get install -y ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY presentation_agent/ ./presentation_agent

# Expose port
EXPOSE 10000

# Start server
CMD ["uvicorn", "presentation_agent.server:app", "--host", "0.0.0.0", "--port", "10000"]
