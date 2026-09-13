import cv2

# Read the input image
image = cv2.imread("input.jpg")

# Check whether image was loaded successfully
if image is None:
    print("Error: input.jpg not found!")
    exit()

# Convert color image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display image information
print("Original Image Shape:", image.shape)
print("Grayscale Image Shape:", gray.shape)
print("Height:", gray.shape[0])
print("Width:", gray.shape[1])

# Save grayscale image
success = cv2.imwrite("output.png", gray)

if success:
    print("Grayscale image saved successfully as output.png")
else:
    print("Error: Could not save output.png")

