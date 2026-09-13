# Computer Vision Unit II
# 08_Median_Filter
# Task: Apply median filtering to the salt-and-pepper noisy image.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.

import cv2
import numpy as np



# Read noisy image
image = cv2.imread("input.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Apply median filter
result = cv2.medianBlur(image, 5)

# Save result
cv2.imwrite("output.png", result)

print("Median filtering applied.")
print("Output saved as output.png")
