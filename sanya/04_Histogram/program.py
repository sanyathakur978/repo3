import cv2
import matplotlib.pyplot as plt

# Read grayscale image
image = cv2.imread("input.jpg", 0)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Find intensity with highest frequency
highest = histogram.argmax()

print("Intensity with highest frequency:", highest)

# Plot histogram
plt.plot(histogram)
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.title("Image Histogram")

# Save histogram
plt.savefig("output.png")
plt.close()

print("Output saved as output.png")
