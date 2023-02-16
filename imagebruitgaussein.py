import cv2
import numpy as np

# Charger l'image
img = cv2.imread('solo-256px.png')

# Ajouter le bruit gaussien pixel par pixel
rows, cols, channels = img.shape
mean = 0
stddev = 50
for row in range(rows):
    for col in range(cols):
        for channel in range(channels):
            pixel = img[row, col, channel]
            noise = np.random.normal(mean, stddev)
            noisy_pixel = pixel + noise
            if noisy_pixel < 0:
                noisy_pixel = 0
            if noisy_pixel > 255:
                noisy_pixel = 255
            img[row, col, channel] = noisy_pixel

# Afficher l'image bruitée
cv2.imwrite('Noisy.png', img)

