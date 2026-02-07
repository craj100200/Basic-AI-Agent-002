import os
import logging
from moviepy import ImageClip, concatenate_videoclips

# Setup logging
logger = logging.getLogger("video_renderer")
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

DEFAULT_OUTPUT_DIR = "presentation_agent/workspace/output"
DEFAULT_DURATION = 3  # seconds per slide

def create_video(image_paths, output_filename=None, duration_per_slide=DEFAULT_DURATION):
    """
    Generate a video from slide images.

    Args:
        image_paths (list of str): Paths to slide images
        output_filename (str, optional): Full path for the output MP4
        duration_per_slide (int): Duration of each slide in seconds

    Returns:
        str: Path to the generated video
    """
    try:
        if not image_paths:
            raise ValueError("No images provided for video generation")

        if not output_filename:
            os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
            output_filename = os.path.join(DEFAULT_OUTPUT_DIR, "output_video.mp4")

        clips = []
        for img_path in image_paths:
            if not os.path.exists(img_path):
                logger.warning(f"Image not found, skipping: {img_path}")
                continue
            clip = ImageClip(img_path).set_duration(duration_per_slide)
            clips.append(clip)

        if not clips:
            raise RuntimeError("No valid slide images found for video")

        video = concatenate_videoclips(clips, method="compose")
        video.write_videofile(output_filename, fps=24)
        logger.info(f"Video generated: {output_filename}")

        return output_filename

    except Exception as e:
        logger.error(f"Video generation failed: {e}")
        raise
