FROM python:3.12-slim

# system dependencies
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY presentation_agent/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY presentation_agent/ ./presentation_agent

EXPOSE 10000

CMD ["uvicorn", "presentation_agent.server:app", "--host", "0.0.0.0", "--port", "10000"]
