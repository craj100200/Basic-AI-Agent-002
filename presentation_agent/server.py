from fastapi import FastAPI
from presentation_agent.tools.text_parser import parse_slides
from presentation_agent.tools.slide_renderer import render_slides
from presentation_agent.tools.video_renderer import create_video


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


@app.get("/testSlides")
def test_slides():

    file_path = "presentation_agent/workspace/input/test.txt"

    slides = parse_slides(file_path)

    images = render_slides(slides)

    return {
        "images": images,
        "count": len(images)
    }


@app.get("/testVideo")
def test_video():
    try:
        slides_file = "presentation_agent/workspace/input/test.txt"
        slides = parse_slides(slides_file)
        images = render_slides(slides)
        output_file = create_video(images, output_filename="presentation_agent/workspace/output/test_video.mp4")
        return {"video_file": output_file, "slides": len(images)}
    except Exception as e:
        return {"error": str(e)}
