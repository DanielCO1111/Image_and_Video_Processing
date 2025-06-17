import torch
import pandas as pd
import cv2
import os
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("❌ Usage: python detect_and_save_csv.py <video_filename>")
    exit()

video_filename = sys.argv[1]
video_path = Path("yolov5/output/exp") / video_filename
video_name = Path(video_filename).stem

output_csv_path = Path("R&D/output/yolo_in_csv") / f"{video_name}.csv"
output_csv_path.parent.mkdir(parents=True, exist_ok=True)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
model.eval()

# Open the video
cap = cv2.VideoCapture(str(video_path))
if not cap.isOpened():
    print("❌ Error: Cannot open video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

frame_number = 0
all_detections = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(rgb_frame)
    detections = results.pandas().xyxy[0]
    detections['time'] = frame_number / fps
    detections['frame'] = frame_number
    all_detections.append(detections)

    frame_number += 1

cap.release()
cv2.destroyAllWindows()

# Save all detections
if all_detections:
    final_detections = pd.concat(all_detections, ignore_index=True)
    final_detections.to_csv(output_csv_path, index=False)
    print(f"✅ YOLO detections saved to: {output_csv_path}")
else:
    print("⚠️ No detections found. CSV not created.")
