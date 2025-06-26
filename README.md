# Image_and_Video_Processing

## Infant Visual Recognition Analysis


## Overview
This project analyzes infant visual recognition behavior from video data using a fully automated image processing and machine learning pipeline.
The pipeline combines video frame extraction, object detection with YOLOv5, feature engineering, and statistical comparison of experimental conditions (such as blurred vs. unblurred video). The codebase leverages Python, Pandas, NumPy, and OpenCV for robust, reproducible analysis.


## Main Components

### Frame Extraction:
Automated splitting of video files into frames for downstream analysis.

### Object Detection (YOLOv5):
Using YOLOv5 to identify and locate relevant features in each frame (such as faces or specific visual targets).

### Feature Engineering:
Extracting and aggregating key data points from detected objects (e.g., position, size, detection confidence).

### Statistical Analysis:
Using Pandas and NumPy to compare visual behavior across different experimental setups (e.g., blurred vs. unblurred videos), generating clear visualizations and CSV reports.

### Automation:
Scripts and notebooks for running the full pipeline in batch mode, supporting reproducibility for future experiments.


### Visual Examples of the functionalities:
---

#### Example of output from running the YOLO algorithm on a simple image

The image shows the output of a YOLO object detection model, which has identified and labeled a dog, a teddy bear, a potted plant, and a person (partially visible), each with a bounding box and a confidence score.

![image](https://github.com/user-attachments/assets/7bcb3088-160c-4081-bc9f-7b3b4e012a06)



#### From the user interface I created for the system:
The first step is to upload a video on which the analysis will be performed.
![image](https://github.com/user-attachments/assets/63d82cfd-00a6-44b6-8d56-e413624d590f)

Next, you will need to set the blur level:

Without Gaussian blur, simulates the vision of an adult.

Gaussian blur level 5 simulates the vision of a 2-year-old baby.

Gaussian blur level 10 simulates the vision of a 1-year-old baby.

Gaussian blur level 20 simulates the vision of a 6-month-old baby.

![image](https://github.com/user-attachments/assets/b0f1cb4c-a8e6-439d-9ab0-7348bdecf8a4)

After processing, you can watch the video after it has been blurred according to the selected level and identify the objects:

You can directly view the results of the calculations, the average confidence levels and the number of objects detected in that video.

Or download the analysis results to a CSV file.

![image](https://github.com/user-attachments/assets/98dda894-ebb7-4d50-aa0a-39ba18c38795)

----

![image](https://github.com/user-attachments/assets/7f9d9ada-3135-4530-a81e-5a92d74a4e8a)
![image](https://github.com/user-attachments/assets/a5bfd3aa-389e-4651-ba29-02ae2bd48ab9)

In these two images, the top photo is clear (unblurred) and the bottom photo is blurred before running the object detection algorithm.
This simulates the difference between adult vision (sharp) and infant vision (blurred).
You can see that the detection confidence scores (the numbers above each box) are lower in the blurred image, showing that the algorithm finds it harder to recognize objects when the image is blurry—just like it’s more difficult for infants to recognize objects due to their limited vision.

----

![image](https://github.com/user-attachments/assets/9cd6e5e3-b0c6-45ef-9292-612c4b134261)

![image](https://github.com/user-attachments/assets/31e0645d-a03f-4961-be7e-f448ac0de56f)


## Technologies
Python 3.x

YOLOv5 (Ultralytics, PyTorch-based)

OpenCV, Pillow

Pandas, NumPy

Matplotlib

Jupyter Notebooks
