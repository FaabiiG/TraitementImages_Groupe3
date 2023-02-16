import cv2


# Chargement de l'image originale
img = cv2.imread('contrast.jpg')

# Définition des paramètres de la transformation linéaire
alpha = 1.2 # coefficient de gain
beta = 50  # coefficient de décalage

# Transformation linéaire
img_transform = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

cv2.imwrite('img_transform.jpg',img_transform)