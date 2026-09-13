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

# Shift frequency to center
dft_shift = np.fft.fftshift(dft)

# Create low-pass mask
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

mask = np.zeros((rows, cols, 2), np.float32)
mask[crow-50:crow+50, ccol-50:ccol+50] = 1

# Apply mask
filtered = dft_shift * mask

# Shift back
filtered = np.fft.ifftshift(filtered)

# Inverse DFT
result = cv2.idft(filtered)

# Get magnitude
result = cv2.magnitude(result[:, :, 0], result[:, :, 1])

# Normalize result
result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)

# Save output
cv2.imwrite("output.png", np.uint8(result))

print("Low-pass filtered image saved as output.png")