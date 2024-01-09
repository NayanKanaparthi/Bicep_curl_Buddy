# Bicep Curl Buddy


This Python application utilizes OpenCV and MediaPipe for real-time pose estimation. The primary goal is to count repetitions based on the angle between the shoulder, elbow, and wrist landmarks.

### Features

- **Real-time Pose Estimation:** Utilizes the `mediapipe` library to estimate key landmarks of the human pose.
- **Rep Counting:** Counts repetitions based on the angle between specific body landmarks.
- **Stage Detection:** Detects stages of the movement (up/down).

### Usage

1. **Clone the repository:**
    ```bash
    https://github.com/NayanKanaparthi/Bicep_curl_Buddy.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd pose-estimation-rep-counter
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script:**
    ```bash
    python rep_counter.py
    ```

5. **Interpretation:**
    - The application will display the video feed with pose estimation overlays.
    - Rep count and movement stages (up/down) will be shown on the video.

### Dependencies

- **OpenCV:** A powerful computer vision library for image and video processing.
- **MediaPipe:** A library for face, hand, and pose detection.

### Contributing

Contributions are welcome! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)

Feel free to customize and expand this overview based on your specific project details.
