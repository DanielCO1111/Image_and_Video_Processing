import cv2
from PIL import Image, ImageFilter
import numpy as np
from pathlib import Path  # ✅ חשוב!
import os


def find_video_file(video_name: str):
    inputs_dir = Path("inputs")  # path relative to where main.py is run
    direct_path = inputs_dir / video_name

    # Try as-is
    if direct_path.is_file():
        return direct_path

    # Try with common extensions
    for ext in [".mp4", ".mov", ".avi", ".mkv"]:
        alt_path = inputs_dir / (video_name + ext)
        if alt_path.is_file():
            return alt_path

    return None


def blur_video(video_name: str, blur_level: int):
    input_path = find_video_file(video_name)
    if input_path is None:
        print(f"❌ Error: Video file not found in inputs/: {video_name}")
        return None

    # Define output directory inside blurring/output/
    output_dir = Path("blurring") / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Construct output filename
    output_name = f"{input_path.stem}_blur{blur_level}.mp4"
    output_path = output_dir / output_name

    # Open video
    cap = cv2.VideoCapture(str(input_path))
    if not cap.isOpened():
        print("❌ Error: Cannot open video file.")
        return None

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(str(output_path), cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if blur_level == 0:
            blurred_frame = frame
        else:
            pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            blurred_pil = pil_frame.filter(ImageFilter.GaussianBlur(radius=blur_level))
            blurred_frame = cv2.cvtColor(np.array(blurred_pil), cv2.COLOR_RGB2BGR)

        out.write(blurred_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"✅ Blurred video saved to: {output_path}")
    return str(output_path)
