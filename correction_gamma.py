import cv2
import numpy as np

# Charger l'image
#img = cv2.imread('image1.jpg')

# Convertir l'image en niveaux de gris
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer la correction gamma
#gamma = 0.5
#corrected_img = np.power(gray_img / 255.0, gamma) * 255

# Enregistrer l'image corrigée
#cv2.imwrite('corrected_image.jpg', corrected_img)

import numpy as np

# Chargement de l'image
img = cv2.imread('solo-256px.png')

# Diminution du contraste de l'image
alpha = 0.5  # coefficient de gain inférieur à 1
beta = 50   # coefficient de décalage

img_contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

cv2.imwrite('contrast.jpg',img_contrast)