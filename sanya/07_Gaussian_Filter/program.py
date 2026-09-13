# Computer Vision Unit II
# 07_Gaussian_Filter
# Task: Apply Gaussian smoothing to the noisy image.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.

import cv2
import numpy as np

import cv2

# Read noisy image
image = cv2.imread("input.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian smoothing
# 5x5 is an odd kernel size suitable for smoothing
result = cv2.GaussianBlur(image, (5, 5), 0)

# Save result
cv2.imwrite("output.png", result)

print("Gaussian smoothing applied.")
print("Output saved as output.png")
