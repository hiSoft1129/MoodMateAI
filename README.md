<img width="1402" height="1122" alt="Ad" src="https://github.com/user-attachments/assets/c7403072-970b-4118-9891-d78443dc9588" />

# 🧠 MoodMate AI Desktop (Python 3.14 Compatible)

A Windows desktop AI mood assistant rebuilt without TensorFlow/DeepFace.

## Features

- PySide6 modern desktop UI
- Dark dashboard
- Webcam support
- ONNX Runtime AI architecture
- Offline-ready design
- SQLite mood history
- EXE packaging support

## Install

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python app/main.py
```

Build EXE:

```bash
build_exe.bat
```

## Architecture

PySide6 UI
↓
OpenCV Camera
↓
ONNX Emotion Model
↓
SQLite Database
