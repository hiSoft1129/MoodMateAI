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