import cv2

# Charger les deux images
img1 = cv2.imread('contrast.jpg')
img2 = cv2.imread('solo-256px.png')

# Assurez-vous que les deux images ont la même taille
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Soustraire les deux images
sous_img = cv2.absdiff(img1, img2)

# Enregistrer l'image résultante
cv2.imwrite('soustraction.png', sous_img)