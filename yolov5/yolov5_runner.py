from yolov5.detect import run
from pathlib import Path
import shutil
import subprocess
from pathlib import Path



def run_detection(video_path: str, weights_path='yolov5s.pt'):
    # Define output base dir
    output_dir = Path("yolov5/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run YOLO detection
    print("🔎 Running YOLOv5 detection...")
    run(
        weights=weights_path,
        source=video_path,
        project=str(output_dir),
        name='exp',
        exist_ok=True
    )

    # Path to YOLO output folder (usually yolov5/output/exp/)
    result_dir = output_dir / "exp"

    # Find the output video YOLO generated
    original_name = Path(video_path).stem
    yolov5_output_video = result_dir / f"{original_name}.mp4"

    # Define renamed output: add "_detected"
    renamed_output_video = result_dir / f"{original_name}_detected.mp4"

    # Rename the file

    # אחרי שמועבר ל־output/exp ונשמר כ-*_detected.mp4
    if yolov5_output_video.exists():
        try:
            shutil.move(str(yolov5_output_video), str(renamed_output_video))
            print(f"✅ Renamed output to: {renamed_output_video}")
            
            # 🔁 NEW: run CSV script automatically
            print("📊 Running detection-to-CSV conversion...")
            result = subprocess.run(
                ['python3', 'R&D/detect_and_save_csv.py', renamed_output_video.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Show output from script
            print(result.stdout)
            if result.returncode != 0:
                print("❌ CSV conversion failed:")
                print(result.stderr)

        except Exception as e:
            print(f"⚠️ Failed to rename output video: {e}")
    else:
        print("⚠️ Warning: Detection video not found for renaming.")


    return str(result_dir)