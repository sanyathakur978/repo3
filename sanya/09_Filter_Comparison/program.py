# Computer Vision Unit II
# 09_Filter_Comparison
# Task: Apply Mean, Gaussian and Median filters to the same noisy image.
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

# Apply three filters
mean = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)

# Save all three results
cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)

print("Mean, Gaussian and Median filters applied.")
print("All three outputs saved successfully.")
