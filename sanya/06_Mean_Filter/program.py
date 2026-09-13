# Computer Vision Unit II
# 06_Mean_Filter
# Task: Apply mean/average filtering with at least two kernel sizes.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.

import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Apply mean filter with two kernel sizes
result1 = cv2.blur(image, (3, 3))
result2 = cv2.blur(image, (5, 5))

# Save final result using larger kernel
cv2.imwrite("output.png", result2)

print("Mean filter applied using 3x3 and 5x5 kernels.")
print("Output saved as output.png")
