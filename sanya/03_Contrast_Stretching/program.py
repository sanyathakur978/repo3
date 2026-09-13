# Computer Vision Unit II
# 03_Contrast_Stretching
# Task: Perform contrast stretching on the low-contrast grayscale image.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.

import cv2
import numpy as np

# TODO: Write your implementation here.
# Example:
# image = cv2.imread("input.jpg")
# ...



import cv2
import numpy as np

# Read low-contrast grayscale image
image = cv2.imread("input.jpg", 0)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Find minimum and maximum intensity
min_value = np.min(image)
max_value = np.max(image)

print("Minimum intensity:", min_value)
print("Maximum intensity:", max_value)

# Perform contrast stretching
result = ((image.astype(np.float32)-min_value)/(max_value-min_value)*255);

# Save enhanced image
cv2.imwrite("output.png", result)

print("Output saved as output.png")