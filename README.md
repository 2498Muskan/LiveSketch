🖼️ ✏️ Live Sketch Animation Generator
What if a computer could sketch a picture exactly like an artist drawing it by hand?

This project explores how computer vision can transform a simple image into a live sketch animation, where the drawing is recreated step-by-step instead of being generated instantly.

🎯 Features
📸 Upload any image
⚡ Real-time sketch animation
🔍 Edge detection using Canny algorithm
🧠 Contour extraction for drawing paths
✏️ Simulated pencil-style sketching effect
🎬 Side-by-side live visualization (Original vs Sketch)
🧠 How It Works
1. Image Input
The user selects an image using a file picker.

2. Preprocessing
The image is resized for faster processing
Converted to grayscale for better edge detection
3. Edge Detection
Canny Edge Detection is applied to find strong boundaries in the image.

4. Contour Detection
Contours are extracted from the detected edges.

These contours represent continuous object boundaries.

5. Sketch Animation
A blank canvas is created
Contour points are drawn one by one
A moving cursor simulates real pencil drawing


🛠️ Tech Stack
Python 🐍
OpenCV 👁️
NumPy 🔢
Tkinter 🖼️
