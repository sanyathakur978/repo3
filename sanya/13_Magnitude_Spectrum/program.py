import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("input.jpg", 0)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Calculate DFT
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to center
dft_shift = np.fft.fftshift(dft)

# Calculate magnitude spectrum
magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

# Apply log scaling
magnitude = np.log(magnitude + 1)

# Normalize for display
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Save magnitude spectrum
cv2.imwrite("output.png", magnitude)

print("Magnitude spectrum saved as output.png")