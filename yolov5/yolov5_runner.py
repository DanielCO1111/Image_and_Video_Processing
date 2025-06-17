from yolov5.detect import run
from pathlib import Path
import shutil
import subprocess
import importlib.util
import sys
from pathlib import Path

# הכנס את הנתיב לתיקייה R&D
rnd_path = Path(__file__).resolve().parents[1] / "R&D"
sys.path.append(str(rnd_path))

# טען את הקובץ analyze_confidence.py
spec = importlib.util.spec_from_file_location("analyze_confidence", rnd_path / "analyze_confidence.py")
analyze_confidence_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analyze_confidence_module)



def run_detection(video_path: str, weights_path='yolov5s.pt'):
    # Step 1: Run YOLO detection
    yolov5_output_dir = Path("yolov5/output")
    yolov5_output_dir.mkdir(parents=True, exist_ok=True)

    print("🔎 Running YOLOv5 detection...")
    run(
        weights=weights_path,
        source=video_path,
        project=str(yolov5_output_dir),
        name='exp',
        exist_ok=True,
        save_csv=True  # חשוב: ודא שזה מופעל ב-detect.py
    )

    # Step 2: Rename output video to *_detected.mp4
    result_dir = yolov5_output_dir / "exp"
    original_name = Path(video_path).stem
    raw_output_video = result_dir / f"{original_name}.mp4"
    final_output_video = result_dir / f"{original_name}_detected.mp4"

    if raw_output_video.exists():
        try:
            shutil.move(str(raw_output_video), str(final_output_video))
            print(f"✅ Renamed output to: {final_output_video}")
        except Exception as e:
            print(f"⚠️ Failed to rename video: {e}")
    else:
        print("⚠️ Detection video not found.")

    # Step 3: Copy CSV to R&D/output/yolo_in_csv
    csv_in_result = result_dir / "predictions.csv"
    if not csv_in_result.exists():
        print("❌ CSV file not found after detection.")
        return str(result_dir)

    csv_output_dir = Path("R&D/output/yolo_in_csv")
    csv_output_dir.mkdir(parents=True, exist_ok=True)

    renamed_csv_path = csv_output_dir / f"{original_name}_detected.csv"
    shutil.copy(csv_in_result, renamed_csv_path)
    print(f"✅ CSV saved to: {renamed_csv_path}")

    # Step 4: Run confidence analysis on that CSV
    print("📊 Running confidence analysis...")
    analyze_confidence_module.analyze_confidence(str(renamed_csv_path))


    # Done
    return str(result_dir)
