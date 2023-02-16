import cv2

# Charger l'image
img = cv2.imread('Noisy.png')

# Appliquer le filtre médian
filtered_img = cv2.medianBlur(img, 5)

# Afficher l'image d'origine et l'image filtrée
cv2.imwrite('filtre.png', img)

