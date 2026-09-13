import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("input.jpg", 0)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to float32
image_float = np.float32(image)

# Calculate 2D DFT
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
dft_shift = np.fft.fftshift(dft)

# Print shapes
print("Original Image Shape:", image.shape)
print("DFT Result Shape:", dft.shape)
print("Shifted DFT Shape:", dft_shift.shape)

# Save shifted DFT result
magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

cv2.imwrite("output.png", np.uint8(magnitude))

print("Output saved as output.png")