# 🖼️ LiveSketch – AI-Powered Drawing Animation System

### 🎯 Project Overview

LiveSketch is a computer vision application that converts ordinary images into realistic hand-drawn sketch animations. Instead of displaying the final sketch instantly, the system reconstructs the drawing process stroke-by-stroke, creating the visual effect of an artist sketching in real time.

---

## ✨ Key Features

🔹 Upload images from local storage

🔹 Automatic image-to-sketch conversion

🔹 Real-time drawing animation

🔹 Dynamic pencil cursor simulation

🔹 Edge and contour-based sketch generation

🔹 Side-by-side comparison view

🔹 Lightweight and fast processing

🔹 User-friendly graphical interface

---

## 🧠 Working Process

### 1️⃣ Image Acquisition

The user selects an image through the application interface.

The system loads and prepares the image for processing.

---

### 2️⃣ Image Enhancement

The uploaded image is:

* Resized to improve performance
* Converted to grayscale
* Smoothed using Gaussian Blur to reduce noise

This helps generate cleaner sketch outlines.

---

### 3️⃣ Edge Extraction

The application applies Canny Edge Detection to identify important image boundaries.

These edges form the foundation of the sketch.

---

### 4️⃣ Path Generation

Detected edges are converted into contour paths.

The contours represent the sequence of strokes required to recreate the image.

---

### 5️⃣ Sketch Rendering

A blank white canvas is created.

The system gradually draws contour points one after another while displaying a moving pencil cursor.

This creates a realistic hand-sketching animation effect.

---

### 6️⃣ Live Visualization

The original image and generated sketch are displayed simultaneously.

Users can observe how the sketch evolves from start to finish.

---

## 🚀 Applications

🎨 Digital Art Creation

📚 Educational Demonstrations

🎬 Animation & Content Creation

🖥️ Computer Vision Learning

📱 Interactive Media Projects

🧩 Creative Design Prototyping

---

## 🛠️ Technology Stack

* Python 🐍
* OpenCV 👁️
* NumPy 🔢
* Tkinter 🖼️
* Computer Vision Techniques 🧠
