# Computer Vision Unit II
# 05_Histogram_Equalization
# Task: Perform histogram equalization and compare histograms.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
image = cv2.imread("input.jpg", 0)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Histogram equalization
equalized = cv2.equalizeHist(image)

# Save equalized image
cv2.imwrite("output.png", equalized)

# Create comparison plot
plt.figure()

plt.subplot(1, 2, 1)
plt.hist(image.ravel(), 256, [0, 256])
plt.title("Before Equalization")

plt.subplot(1, 2, 2)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("After Equalization")

plt.savefig("histogram_comparison.png")
plt.close()

print("Equalized image saved as output.png")
print("Comparison saved as histogram_comparison.png")