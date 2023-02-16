import cv2

# Charger les deux images
img1 = cv2.imread('solo-256px.png')
img2 = cv2.imread('logo.png')

# Assurez-vous que les deux images ont la même taille
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Mélanger les deux images avec un facteur de fusion de 0.5
add_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

