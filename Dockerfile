FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements from root
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project folder
COPY presentation_agent/ ./presentation_agent

# Expose port for Render
EXPOSE 10000

# Start the server
CMD ["uvicorn", "presentation_agent.server:app", "--host", "0.0.0.0", "--port", "10000"]
