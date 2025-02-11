# Face Recognition System

A simple face recognition system built using Python, `face_recognition`, and `OpenCV`. This system captures real-time video from your webcam, detects faces, and matches them with known faces.

## Features
- Real-time face detection.
- Face recognition with known face encodings.
- Displays the recognized name above the detected face.
- Easily extensible to handle multiple faces.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/face-recognition-system.git
cd face-recognition-system
```

### 2. Install dependencies:

Make sure you have Python installed, then install the required libraries using pip:

```bash
pip install face_recognition opencv-python
```

## Usage

1. **Prepare a known face image:**

   Replace `known_face.jpg` in the code with the image file of the person you want to recognize.

2. **Run the face recognition system:**

   Execute the script:

   ```bash
   python face_recognition_system.py
   ```

3. **Test it:**

   - The system will start capturing video from your webcam.
   - If a face matches the known one, it will label it with the corresponding name.
   - Press `q` to stop the program.

## Notes
- Ensure you have a working webcam connected to your computer.
- You can add multiple faces by adding more known face encodings and names in the code.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

