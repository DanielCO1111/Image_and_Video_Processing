# app.py
import streamlit as st
from pathlib import Path
import sys

# כדי לאפשר ייבוא מקומי sys.path הוספת הנתיב של הפרוייקט
sys.path.append(str(Path(__file__).resolve().parent))

from main import run_pipeline

st.set_page_config(page_title="Video Processing App", layout="centered")

st.title("🎥 Video Processing Pipeline")
st.markdown("Select a video and a blur level, and the system will run all the steps and display the result.")

# --- Input video selection ---
input_videos = list(Path("inputs").glob("*.mp4"))
video_options = [v.name for v in input_videos]

video_file = st.selectbox("Select a video:", video_options)

# --- Blur level selection ---
blur_level = st.select_slider("Select blur level:", options=[0, 5, 10, 20])

# --- Start button ---
if st.button("▶️ Run Pipeline"):
    st.info("Running video processing...")
    try:
        result_dir = run_pipeline(video_file, blur_level)
        st.success(f"✅ Pipeline completed! Outputs saved in: {result_dir}")

        output_video = Path(result_dir) / f"{Path(video_file).stem}_detected.mp4"
        if output_video.exists():
            st.video(str(output_video))
        else:
            st.warning("⚠️ Output video not found.")

    except Exception as e:
        st.error(f"❌ Pipeline failed: {e}")
