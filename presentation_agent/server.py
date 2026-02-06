from fastapi import FastAPI
from presentation_agent.tools.text_parser import parse_slides
import os

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Presentation Agent API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/testParser")
def test_parser():
    file_path = "presentation_agent/workspace/input/test.txt"

    if not os.path.exists(file_path):
        return {
            "error": "test.txt not found"
        }

    slides = parse_slides(file_path)

    return {
        "slides": slides,
        "count": len(slides)
    }
