import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ---------------------------------
# Select Image
# ---------------------------------
Tk().withdraw()

file_path = askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

if not file_path:
    print("No image selected!")
    exit()

# ---------------------------------
# Load Image
# ---------------------------------
img = cv2.imread(file_path)

if img is None:
    print("Failed to load image!")
    exit()

# ---------------------------------
# Convert to Gray and Find Edges
# ---------------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

# ---------------------------------
# Create Blank Canvas
# ---------------------------------
canvas = np.zeros_like(img)

height, width = img.shape[:2]

# ---------------------------------
# Create Video Writer
# ---------------------------------
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video = cv2.VideoWriter(
    "color_sketch_animation.mp4",
    fourcc,
    30,
    (width, height)
)

# ---------------------------------
# Progress Setup
# ---------------------------------
total_points = sum(len(c) for c in contours)
current = 0

print("Starting Color Animation...\n")

# ---------------------------------
# Draw Using Original Colors
# ---------------------------------
for contour in contours:

    for point in contour:

        x, y = point[0]

        # Copy original pixel color
        canvas[y, x] = img[y, x]

        current += 1
        progress = (current / total_points) * 100

        print(
            f"\rProgress: {progress:.1f}%",
            end=""
        )

        cv2.imshow(
            "Color Drawing Animation",
            canvas
        )

        video.write(canvas)

        if cv2.waitKey(1) == 27:
            break

# ---------------------------------
# Show Final Image For 2 Seconds
# ---------------------------------
for _ in range(60):
    video.write(img)

video.release()

print("\n\nVideo Saved Successfully!")
print("File: color_sketch_animation.mp4")

cv2.waitKey(5000)
cv2.destroyAllWindows()