import cv2
import numpy as np

# Chargement de l'image originale
img = cv2.imread('contrast.jpg')

# Définition des paramètres de la transformation non linéaire
gamma = 1.5

# Transformation non linéaire
img_transform = np.power(img / 255.0, gamma) * 255

cv2.imwrite('img_nonLineaire.jpg',img_transform)