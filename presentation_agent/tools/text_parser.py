def parse_slides(file_path: str):
    slides = []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    slide_blocks = content.split("[SLIDE_START]")

    for block in slide_blocks:
        block = block.strip()

        if not block:
            continue

        if "[SLIDE_END]" not in block:
            raise ValueError("Missing [SLIDE_END]")

        block = block.split("[SLIDE_END]")[0].strip()

        if "[TITLE_START]" not in block or "[TITLE_END]" not in block:
            raise ValueError("Missing TITLE tags")

        title_part = block.split("[TITLE_START]")[1].split("[TITLE_END]")[0].strip()

        body_part = block.split("[TITLE_END]")[1].strip()

        bullets = [
            line.strip()
            for line in body_part.split("\n")
            if line.strip()
        ]

        slides.append({
            "title": title_part,
            "bullets": bullets
        })

    return slides
