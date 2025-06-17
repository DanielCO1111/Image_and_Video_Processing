import sys
from blurring.video_blur import blur_video
from yolov5.yolov5_runner import run_detection



def main():
    # Validate argument count
    if len(sys.argv) != 2:
        print("Usage: python main.py <video_name>")
        print("Example: python main.py hello or hello.mp4")
        return

    video_name = sys.argv[1]

    # Get blur level from user
    print("Choose blur level:")
    print("0 = no blur")
    print("5 = light blur")
    print("10 = medium blur")
    print("20 = strong blur")
    blur_input = input("Enter blur level (0, 5, 10, 20): ")

    try:
        blur_level = int(blur_input)
        assert blur_level in [0, 5, 10, 20]
    except:
        print("❌ Invalid blur level. Please enter 0, 5, 10, or 20.")
        return

    # Run blur process
    output_path = blur_video(video_name, blur_level)
    if output_path is None:
        print("❌ Blurring failed.")
    else:
        print(f"✅ Blurring successful. Output saved to: {output_path}")

    # Step 2: Run YOLO detection
    detection_dir = run_detection(output_path)
    print(f"✅ Detection completed. Results saved to: {detection_dir}")


if __name__ == "__main__":
    main()
