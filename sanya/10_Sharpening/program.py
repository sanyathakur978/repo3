import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Custom sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply sharpening
result = cv2.filter2D(image, -1, kernel)

# Save result
cv2.imwrite("output.png", result)

print("Sharpened image saved as output.png")