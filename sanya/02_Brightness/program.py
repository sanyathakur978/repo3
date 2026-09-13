# Computer Vision Unit II
# 02_Brightness
# Task: Increase brightness of the dark input image.
#
# Develop and run your own implementation here using Python + OpenCV.
# Use relative paths so the program runs from this folder.
#
# Required input: input.jpg
# Required output filename(s): see the assignment PDF.

import cv2

# Read dark image
image = cv2.imread("input.jpg")

# Increase brightness using add()
brightness = 50
result = cv2.add(image, brightness)

# Compare one pixel before and after
print("Before:", image[100, 100])
print("After:", result[100, 100])

# Save enhanced image
cv2.imwrite("output.png", result)

print("Output saved as output.png")

