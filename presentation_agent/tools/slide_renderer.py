import os
import logging
from PIL import Image, ImageDraw, ImageFont

# Setup logging
logger = logging.getLogger("slide_renderer")
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Constants
WIDTH = 1280
HEIGHT = 720
BACKGROUND_COLOR = (255, 255, 255)
TITLE_COLOR = (0, 0, 0)
TEXT_COLOR = (50, 50, 50)

TITLE_SIZE = 60
TEXT_SIZE = 40

OUTPUT_DIR = "presentation_agent/workspace/output"


def render_slides(slides):
    """
    Generate slide images from slide data.

    Args:
        slides (list of dict): [{"title": str, "bullets": [str]}]

    Returns:
        List of generated image paths
    """
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        logger.info(f"Output directory ready: {OUTPUT_DIR}")
    except Exception as e:
        logger.error(f"Failed to create output directory: {e}")
        raise

    image_paths = []

    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", TITLE_SIZE)
        text_font = ImageFont.truetype("DejaVuSans.ttf", TEXT_SIZE)
    except Exception as e:
        logger.warning(f"Failed to load TTF fonts, using default: {e}")
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    for index, slide in enumerate(slides):
        try:
            img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
            draw = ImageDraw.Draw(img)

            y = 100

            # Draw title
            draw.text((100, y), slide["title"], fill=TITLE_COLOR, font=title_font)
            y += 120

            # Draw bullets
            for bullet in slide["bullets"]:
                draw.text((150, y), f"• {bullet}", fill=TEXT_COLOR, font=text_font)
                y += 60

            file_path = os.path.join(OUTPUT_DIR, f"slide_{index}.png")
            img.save(file_path)
            logger.info(f"Slide saved: {file_path}")

            image_paths.append(file_path)

        except Exception as e:
            logger.error(f"Failed to render slide {index} ({slide.get('title')}): {e}")

    if not image_paths:
        logger.error("No slides were generated!")
        raise RuntimeError("Slide rendering failed for all slides")

    logger.info(f"Total slides generated: {len(image_paths)}")
    return image_paths
