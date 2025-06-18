import streamlit as st
from pathlib import Path
import sys

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


sys.path.append(str(Path(__file__).resolve().parent))

from main import run_pipeline

st.set_page_config(page_title="Video Processing App", layout="centered")
st.title(" Video Processing Pipeline 🎥")
st.markdown("Select a video and a blur level, and the system will run all the steps and return the result.")

# --- Input video selection ---
input_videos = list(Path("inputs").glob("*.mp4"))
video_options = [v.name for v in input_videos]

video_file = st.selectbox("Select a video:", video_options)


# --- Blur level selection ---
blur_options = {
    "Vision of an adult - No blur": 0,
    "Vision of a two-year-old baby - Light blur": 5,
    "Vision of a one-year-old baby - Medium blur": 10,
    "Vision of a six-month-old baby - Strong blur": 20

}
blur_choice = st.selectbox("Select blur level:", list(blur_options.keys()))
blur_level = blur_options[blur_choice]


# --- Start button ---
if st.button(" Run ▶️ "):
    st.info("Running video processing...")
    try:
        detection_dir, analysis_path = run_pipeline(video_file, blur_level)
        st.success(f"✅ Pipeline completed! Outputs saved in:\n- {detection_dir}\n- {analysis_path}")

        output_video = Path(detection_dir) / f"{Path(video_file).stem}_detected.mp4"
        if output_video.exists():
            st.video(str(output_video))

        if analysis_path and Path(analysis_path).exists():
            st.success(f"📊 Confidence analysis saved to:\n{analysis_path}")
        else:
            st.warning("⚠️ Video processed, but confidence analysis CSV not found.")

    except Exception as e:
        st.error(f"❌ Pipeline failed: {e}")
