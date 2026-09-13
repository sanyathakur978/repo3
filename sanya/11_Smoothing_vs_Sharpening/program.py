import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Smooth the image
smooth = cv2.GaussianBlur(image, (5, 5), 0)

# Sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Sharpen the image
sharp = cv2.filter2D(image, -1, kernel)

# Save outputs
cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)

print("Smooth image saved as output_smooth.png")
print("Sharp image saved as output_sharp.png")